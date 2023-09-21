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

# Tif file with RGB Color dtype (path cannot have spaces)
input_file = "/Users/oanegros/Documents/werk/Blender_for_Biologists_2023/data/RPE1_Expansion_MeOH_405DAPI_488alphabetaTubulin_zstack_40x_Proc.tif"
# path to zstacker executable (path cannot have spaces)
zstacker_path = "/Users/oanegros/Documents/werk/scripts/zstacker_v1.0_macos_1015/zstacker"

# physical size of the pixels in µm
xy_scale = 0.207
z_scale = 0.170

axes_order = 'zyx'
#TODO implement time, channels

tif = Path(input_file)

#print('hey')
print(tif)
with tifffile.TiffFile(input_file) as ifstif:
    imgdata = ifstif.asarray()
    metadata = dict(ifstif.imagej_metadata)


print(metadata)
(tif.parents[0] / "tmp/").mkdir(exist_ok=True)
zax =  axes_order.find('z')
tmpfiles = []
for z in range(imgdata.shape[zax]):
    print(imgdata.take(indices=z,axis=zax).shape)
    print(imgdata.shape, z)
    fname = tif.parents[0] / f"tmp/{z:04}.tif"
    tifffile.imwrite(fname, imgdata.take(indices=z,axis=zax))
    tmpfiles.append(fname)

subprocess.run(" ".join([zstacker_path, "-t 1 -z", str(z_scale/xy_scale) ,str(tif.parents[0] / "tmp"),  str(tif.with_suffix(".vdb"))]), shell=True)

#    
for tmpfile in tmpfiles:
    tmpfile.unlink()

scale = np.array([ xy_scale*imgdata.shape[1], xy_scale*imgdata.shape[2],z_scale*imgdata.shape[0], ]) * 0.001
scale = np.ones(3)*0.02
bpy.ops.object.volume_import(filepath=str(tif.with_suffix(".vdb")), align='WORLD', location=(0, 0, 0), scale=tuple(scale))
print(bpy.context.view_layer.objects.active.name)
print(scale)
bpy.context.view_layer.objects.active.scale = scale

vol= bpy.context.view_layer.objects.active

empty = bpy.ops.object.empty_add(location=tuple((np.array(vol.bound_box[-1][:])/2) *0.02))
empty = bpy.context.object
empty.name = str(tif.name) + " container" 

vol.parent = empty
vol.matrix_parent_inverse = empty.matrix_world.inverted()

empty.location = (0,0,0)

print('done')


