# New `tif loader`

The version of `tif loader` we installed in this tutorial is actually not the current version! For didactic purposes, we wanted to show you how to make your own Materials and get used to the Blender user interface. We will now install the latest version of the `tif loader`.

For this we have to `Remove` our current version, which is done in the same `Edit > Preferences > Add-Ons` tab as we installed in:
- unfold the `tif loader` details
- press `(x) Remove`

Restart Blender. 

Download the new version of [tif_loader.zip](https://github.com/oanegros/tif2bpy/blob/main/tif_loader.zip) from the development git repository `tif2bpy`.


</details>

<details>
<summary>Install this similar to how we installed the initial version</summary>
- open <code>Edit > Preferences > Add-Ons</code>
- press <code>Install</code>
- give the new <code>tif_loader.zip</code> file
- check the box next to the new add-on
</details>
We no longer need to install tifffile, as this was done previously.

Now reload the example data, or the [new data of C. elegans meiosis](../data/gonad2_rgb-2.tif.zip).

It already has a material applied! 

This is the end of lesson 1! You've now done most of the basic operations to make a pretty 3D video of microscopy data in blender. For a challenge in rnedering a complicated scene, see [lesson 2](./2_multichannel.md).  Or [go back to main](../README.md) to try the extra lessons.
