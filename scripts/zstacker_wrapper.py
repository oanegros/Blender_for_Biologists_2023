# MIT License

# Copyright (c) 2023 Oane Gros

# Permission is hereby granted, free of charge, to any person obtaining a copy
# of this software and associated documentation files (the "Software"), to deal
# in the Software without restriction, including without limitation the rights
# to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
# copies of the Software, and to permit persons to whom the Software is
# furnished to do so, subject to the following conditions:

# The above copyright notice and this permission notice shall be included in all
# copies or substantial portions of the Software.

# THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
# IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
# FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
# AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
# LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
# OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE
# SOFTWARE.


import subprocess
from pathlib import Path
import os
import pip
import numpy as np
try:
    import tifffile
except:
    pip.main(['install', 'tifffile'])
    import tifffile
import bpy

# Tif file with RGB Color dtype (path cannot have spxaces)
input_file = "/Users/oanegros/Documents/werk/blender_workshop/221107_SampleA_SoRA_Gonad1_fused_3.tif"
# input_file = "/Users/oanegros/Documents/werk/blender_workshop/3colortif.tif"
# path to zstacker executable (path cannot have spaces)
zstacker_path = "/Users/oanegros/Documents/werk/scripts/zstacker_v1.0_macos_1015/zstacker"

# physical size of the pixels in µm
xy_scale = 0.0339
z_scale = 0.16

axes_order = 'zyx'

def make_and_load_vdb(imgdata, x_ix, y_ix, z_ix, axes_order, tif):
    tmpfiles = []
    zax =  axes_order.find('z')
    for z in range(imgdata.shape[zax]):
        fname = tif.parents[0] / f"tmp_zstacker/{z:04}.tif"
        plane = imgdata.take(indices=z,axis=zax)

        tifffile.imwrite(fname, plane)
        tmpfiles.append(fname)
    identifier = str(x_ix)+str(y_ix)+str(z_ix)

    subprocess.run(" ".join([zstacker_path, "-t 1 -z", str(z_scale/xy_scale) ,str(tif.parents[0] / "tmp_zstacker"),  str(tif.with_name(tif.stem + identifier +".vdb"))]), shell=True)

    #    
    for tmpfile in tmpfiles:
        tmpfile.unlink()
    
    
    bpy.ops.object.volume_import(filepath=str(tif.with_name(tif.stem + identifier +".vdb")), align='WORLD', location=(0, 0, 0))

    return bpy.context.view_layer.objects.active


tif = Path(input_file)

with tifffile.TiffFile(input_file) as ifstif:
    imgdata = ifstif.asarray()
    print(imgdata.shape)
    imgdata = np.moveaxis(imgdata, 1,2)
    print(imgdata.shape)
    metadata = dict(ifstif.imagej_metadata)


(tif.parents[0] / "tmp_zstacker/").mkdir(exist_ok=True)

n_splits = [(dim // 2048)+ 1 for dim in imgdata.shape]
arrays = [imgdata]
# i know axis order is abc as it is not defined

volumes =[]
a_chunks = np.array_split(imgdata, n_splits[0], axis=0)
for a_ix, a_chunk in enumerate(a_chunks):
    b_chunks = np.array_split(a_chunk, n_splits[1], axis=1)
    
    for b_ix, b_chunk in enumerate(b_chunks):
        c_chunks = np.array_split(b_chunk, n_splits[2], axis=2)
        for c_ix, c_chunk in enumerate(reversed(c_chunks)):
            print(c_chunk.shape)
            vol = make_and_load_vdb(c_chunk, a_ix, b_ix, c_ix, axes_order, tif)
#            bbox = np.array(vol.bound_box[-2][:])
            bbox = np.array([c_chunk.shape[2],c_chunk.shape[1],c_chunk.shape[0]*(z_scale/xy_scale)])
            print(bbox)
            scale = np.ones(3)*0.02
            vol.scale = scale
            print(c_ix, b_ix, a_ix)
            offset = np.array([-c_ix-1,-b_ix-1,-a_ix-1])
            
            vol.location = tuple(offset*bbox*scale)
            volumes.append(vol)


# keep z at bottom
center = np.array([c_chunk.shape[2] * (-len(c_chunks)), c_chunk.shape[1] * (-len(b_chunks)), c_chunk.shape[0] * (-len(a_chunks)*(z_scale/xy_scale))])*np.array([0.5,0.5,1])
empty = bpy.ops.object.empty_add(location=tuple(center*0.02))

empty = bpy.context.object
empty.name = str(tif.name) + " container" 


for vol in volumes:
    vol.parent = empty
    vol.matrix_parent_inverse = empty.matrix_world.inverted()

empty.location = (0,0,0)

print('done')


