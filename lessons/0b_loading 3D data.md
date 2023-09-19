# Loading 3D microscopy data

Blender's volumetric rendering is primarily used for fog and fire animations, we can use the same framework for 3D microscopy data.

The blender volume data format is a [.vdb](https://www.openvdb.org/forum/), which is a tree-like data format, so the standard tif-grid data needs to first be restructured to be able to load into blender. For this we use the downloaded utility `zstacker`.

## Running zstacker

Move to the `scripting` tab of blender. This shows the blender-python interface. We'll run a python script [zstacker_wrapper.py](../scripts/zstacker_wrapper.py) from this interface, that will automatically call `zstacker`. Load in the script from the file explorer at the top, or just copy and paste the text.
- <details><summary>Blender tabs?</summary>tabs are located at the top of the screen, and allow different workflows. The default is 'layout', each tab has a different purpose. For the purposes of this tutorial, we will stay between the layout, scripting and shading tabs. Any tab's windows can also be edited and customized. </details>

\
Before running `zstacker`, the input values to `input_file` and `zstacker_path` to the appropriate paths for a tif file and the zstacker executable, respectively. Also put in the correct physical size of your pixels in for the `xy_size` and `z_size` fields. 

There is an example tif stack we will use in the course [here]().

Notes on input data:
- Data should be a .tif zstack in RGB Color mode
- Any vdb > 450 MB [will crash blender](https://projects.blender.org/blender/blender/issues/107252) currently
- <details><summary>Advanced</summary> The vdb format is optimized for sparse volumes with big empty areas, and making your volumes sparse allows you to load in bigger data. This is changed by thresholding your data with the -t flag in the zstacker utility </details>

With the paths set to the correct filepaths, run the script by pressing the play button in the top row.

This should yield a big gray box of data. In here is your volume, it is just not rendered yet! For this: go to the [rendering lesson 1a](./1a_eevee_emission.md) :yum:.

- <details><summary>Advanced info on the zstacker_wrapper script</summary>This wrapper script installs tifffile python library, unpacks a tif into an image sequence, and then calls zstacker via subprocess on the folder with tifs. Hereby it thresholds none of the data away, and sets a z scale into the vdb file. It then deletes the created temporary files and loads the vdb automatically and scales it down.  </details>