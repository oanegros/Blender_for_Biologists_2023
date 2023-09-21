# Downloading, installing and starting

## Download

For this course we need blender, and zstacker, an addon C++ code package that can do .tif to .vdb (Blender volume file) conversions.

- Download the most recent version of blender from https://www.blender.org/download/ 
    - <details><summary>Advanced</summary>note that Blender 3.5 is the latest version that works on the EMBL cluster, but as long as you don't use newer features you can still render there</details>
  

- Download one of the zstacker .zip files from https://github.com/GallowayLabMIT/zstacker/releases/tag/v1.0
    - Unzip the folder and note down the full path  (all directories and the filename) to the executable binary file (called zstacker), this cannot contain spaces 
    - if your OS is not supported see the documentation at main https://github.com/GallowayLabMIT/zstacker 

## Start

Start blender.
<details>
  <summary>Advanced</summary>
  To make it easier to troubleshoot Z-stack loading, consider <a href="https://docs.blender.org/manual/en/latest/advanced/command_line/launch/index.html">starting blender from the command line.</a>
</details>

\
You should now see the default Blender start. You can delete everything in the scene by selecting all with `A` and pressing `X`

Next lesson, loading 3D data: [0b loading 3D data](./0b_loading%203D%20data.md)
Or go [back to main](../README.md)