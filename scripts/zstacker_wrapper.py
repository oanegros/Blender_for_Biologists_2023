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
input_file = "/Users/oanegros/Documents/werk/blender_workshop/3colortif.tif"
# path to zstacker executable (path cannot have spaces)
zstacker_path = "/Users/oanegros/Documents/werk/scripts/zstacker_v1.0_macos_1015/zstacker"

# physical size of the pixels in µm
xy_scale = 0.207
z_scale = 0.190

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

subprocess.run(" ".join([zstacker_path, "-t 1 -z", str(xy_scale/z_scale) ,str(tif.parents[0] / "tmp"),  str(tif.with_suffix(".vdb"))]), shell=True)

#    
for tmpfile in tmpfiles:
    tmpfile.unlink()

scale = np.array([ xy_scale*imgdata.shape[1], xy_scale*imgdata.shape[2],z_scale*imgdata.shape[0], ]) * 0.001
scale = np.ones(3)*0.02
bpy.ops.object.volume_import(filepath=str(tif.with_suffix(".vdb")), align='WORLD', location=(0, 0, 0), scale=tuple(scale))
print(bpy.context.view_layer.objects.active.name)
print(scale)
bpy.context.view_layer.objects.active.scale = scale

