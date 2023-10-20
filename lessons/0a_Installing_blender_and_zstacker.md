# Downloading, installing and starting

## Download

For this course we need blender, and zstacker, an addon python package that can do .tif to .vdb (Blender volume file) conversions.

- Download the most recent version of blender from https://www.blender.org/download/. You need version 3.5 or higher for the tif loader Add-On.
    - <details><summary>Advanced</summary>note that Blender 3.5 is the latest version that works on the EMBL cluster, but as long as you don't use newer features you can still render there</details>
  
- Download the [tif loader zip file](../scripts/tif_loader.zip). 
- If you do not have your own .tif files, download the [example data](../data/RPE1_Expansion_MeOH_405DAPI_488alphabetaTubulin_594acetylatTubulin_647NHS_zstack_40x_8bit.tif.zip) and unzip this.


## Start

Start blender.
<details>
  <summary>Advanced</summary>
  To make it easier to troubleshoot Z-stack loading, consider <a href="https://docs.blender.org/manual/en/latest/advanced/command_line/launch/index.html">starting blender from the command line.</a>
</details>

Install the `tif loader` Add-On:
- In Blender go to `Edit > Preferences`
- Go to `Add-Ons` tab in `Preferences`
- Press `Install` and give the `tif_loader.zip` file (as .zip)
- In the added `tif loader` add-on window in `Preferences`: press the tick box to enable, and the arrow to unfold the details
- in the details press `install tifffile`

\
You should now see the default Blender start. You can delete everything in the scene by selecting all with `A` and pressing `X`

Next lesson, loading 3D data: [0b loading 3D data](./0b_loading%203D%20data.md)
Or go [back to main](../README.md)