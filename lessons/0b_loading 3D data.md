# Loading 3D microscopy data

Blender's volumetric rendering is primarily used for fog and fire animations, we can use the same framework for 3D microscopy data. 3D data is in microscopy often saved as a .tif, saving all voxels (volume pixels) values in order on the disk. 

<img src="../figures/neubias 3ddata.png" alt="isolated" width="300"/>

(image from [NEUBIAS](https://neubias.github.io/training-resources/multidimensional_image_basics/index.html))

The blender volume data format is a [.vdb](https://www.openvdb.org/forum/), which is a tree-like data format, so the standard tif-grid data needs to first be restructured to be able to load into blender. For this we use the downloaded utility `zstacker`.
<details><summary>About the vdb data structure</summary>VDBs contain multiple scales of voxels, where the larger ones mostly contain whether there is data in its lower nodes. In this way, when a lightray traverses a large volume, it does not have to check every voxel for an intersection. 
<br>

<img src="../figures/vdb museth.png" alt="isolated" width="300"/> 

Image from Ken Museth (2013), showing the depth of saving of a 2D circle in a vdb, green being root nodes, orange and blue internal nodes and red leaf nodes.  </details>

## Running zstacker

Move to the `scripting` tab of blender. This shows the blender-python interface. 

<img src="../figures/scripting tab.png" alt="isolated" width="100"/>

- <details><summary>Blender tabs?</summary>tabs are located at the top of the screen, and allow different workflows. The default is 'layout', each tab has a different purpose. For the purposes of this tutorial, we will stay between the layout, scripting and shading tabs. Any tab's windows can also be edited and customized. </details>

We'll run a python script [zstacker_wrapper.py](../scripts/zstacker_wrapper.py) from this interface, that will automatically call `zstacker`. Load in the script from the file explorer at the top, or just copy and paste the text.

\
Before running `zstacker`, the input values to `input_file` and `zstacker_path` to the appropriate paths for a tif file and the zstacker executable, respectively. Also put in the correct physical size of your pixels in for the `xy_size` and `z_size` fields. 

There is an example tif stack we will use in the course [here](../data/RPE1_Expansion_MeOH_405DAPI_488alphabetaTubulin_zstack_40x_Proc.tif.zip). This first needs to be unzipped.
- <details><summary>About the example data</summary> The example data is a human retinal pigment epithelial (RPE-1) cell line, stained for microtubules (green) and DAPI (blue). Pixel size is 0.207 µm in Z, and 0.170 in X/Y. To achieve better resolution, the cell was imaged with Ultrastructure Expansion Microscopy (U-ExM), where the sample is physically expanded through a chemical process, enabling nanoscale imaging with standard microscopes, while preserving ultrastructure. See also <a href="../data/materials_methods_RPE1.md">full materials and methods</a>. The data was contributed by Granita Lokaj. </details>

**Notes on input data**:
- Data should be a .tif zstack in RGB Color mode
- It is easier to work with if your data is already normalized before running `zstacker_wrapper` 
- Any vdb >2048 axis length will load into separate chunks of volumes. You may need to apply some of the settings to all of the separate subvolumes separately.  <details><summary> details</summary> This is a workaround for <a href="https://projects.blender.org/blender/blender/issues/83942">a known issue</a> with the Eevee volume render pipeline, which has a max size. Thus, Cycles can actually handle bigger datasets, but this can be very inconvenient as blender will crash immediately when accidentally opening a non-cycles viewport. </details>
- <details><summary>Advanced</summary> The vdb format is optimized for sparse volumes with big empty areas. This is changed by thresholding your data with the -t flag in the zstacker utility, however, full sparse volume support in Blender is not enabled, and most of the gain will probably be in Cycles. </details>

With the paths set to the correct filepaths, run the script by pressing the play button in the top row.

This should yield a big gray box of data. In here is your data, it is just not rendered yet! For this: go to the [rendering lesson 1a](./1a_eevee_emission.md) :yum:.
Or go [back to main](../README.md)

- <details><summary>Advanced info on the zstacker_wrapper script</summary>This wrapper script installs tifffile python library, unpacks a tif into an image sequence, and then calls zstacker via subprocess on the folder with tifs. Hereby it thresholds none of the data away, and sets a z scale into the vdb file. It then deletes the created temporary files and loads the vdb automatically and scales it down. It then assigns an Empty as a parent and moves this to center (to move the pivot point to the center in xy) </details>