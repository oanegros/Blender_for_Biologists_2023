# Downloading, installing and starting

## Download

For this course we need blender, and an addon C++ code package that can do .tif to .vdb (Blender volume file) conversions

- Download the most recent version of blender from https://www.blender.org/download/ 
    - note that Blender 3.5 is the latest version that works on the EMBL cluster, but as long as you don't use newer features you can still render there
- Download one of the zstacker .zip files from https://github.com/GallowayLabMIT/zstacker/releases/tag/v1.0
    - Unzip the folder and note down the full path  (all directories and the filename) to the executable binary file (called zstacker), this cannot contain spaces 
    - if your OS is not supported in zstacker see the documentation at main https://github.com/GallowayLabMIT/zstacker 

## Start

Either start blender from the installed icon, or, if you're more code-adept [start it from the command line](https://docs.blender.org/manual/en/latest/advanced/command_line/launch/index.html) as this makes it easier to troubleshoot Z-stack loading.

You should now see the default Blender start. You can delete the default cube by clicking it and pressing `X`

