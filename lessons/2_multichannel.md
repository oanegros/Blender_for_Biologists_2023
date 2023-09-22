# Combining everything!

With these basics, there is already a lot possible, but way more to still explore (after all, many people just do Blender rendering full-time :wink:), especially with the help of youtube tutorials.

The way to now explore will depend a lot on your data and what you use blender for. To try to show how you can combine features into a bigger file, and try to find render modes that work for your data, here a more complicated project :D. 

With the [microscopy data](../data/gonad2_rgb-2.tif.zip) and [cellpose mask](../data/gonad_masks_rgb-2.tif.zip), try to recreate this render:

 <img src="../figures/celegans1.png" width="600"/>

This shows the _C. elegans_ gonad in the process of meiosis. Here we find homologous chromosomes assembled into the synaptonemal complex, with two axes and a central region. Thus we get colocalizing signal for DNA (DAPI, channelR), the synaptonemal complex Axis (Htp3, channelG) and the synaptonemal complex Central Region (SYP-2, channelB).
- <details><summary>About the example data</summary> xy_scale is 0.0846 µm, z_scale is 0.2 µm. See also <a href="../data/materials_methods_celegans.md">full materials and methods</a>. The data was contributed by Ana Neves. </details>

As an extra challenge, this also shows the result of a cellpose segmentation pipeline as outlines around the segmented nuclei. Note that outlines are possible in `Cycles`, but easier in `Eevee`. This render was also made with only `Eevee`.

---
<details><summary>Hints for multichannel images</summary> The `Mix Shader` Node allows you to combine multiple shaders together before piping to `Material Output` </details>

<details><summary>Hints for mask renders</summary> Outlines are not very easy to make, other render modes may work easier, such as very transparent or translucent materials. 
For transparency to work in `Eevee`, you need to set `Material Properties > Settings > Blend Mode` to `Alpha Blend`.

To make outlines work, <a href="https://www.youtube.com/watch?v=5wu_SvCCX_U">i followed this youtube tutorial</a>, where you add a solidify modifier to the volume-to-mesh of the masks. This adds a thickness to the mask. You can then give the original shape a transparent Material and the mask an emmission/other Material. 
Note that for this to work you need to flip the normals of the `Solidify Modifier` so that `Backface Culling` in `Material Properties > Settings` effectively becomes front-face culling (`Eevee` only tries to render the back of the object). 
 </details>

