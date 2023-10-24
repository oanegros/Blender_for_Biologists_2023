# Volume to mesh

With the previous (_volumetric_) renders we have been looking at, data like the microtubules can look sort of murky. This is because there are many fibers that are close together at the same intensity, which can be hard to distinguish. 

Instead, we can do a `Volume to Mesh` operation, where we take all the voxels above a certain `threshold` value intensity, and render these as a `mesh` (i.e. as a surface).

This means that we can have, for all our microtubules that are separated enough, a lot more contrast, as the surface will show the height differences between the separate microtubules more clearly.

---

Activate the _Layout_ tab and add a cube to the scene with `Add` or `Shift+A`.

Add a `Volume to Mesh` `Modifier` to the cube, under the `Modifier Properties` tab in the `Properties` panel. 

 <img src="../figures/volume to mesh properties.png" width="400"/>

 This modifier you can refer to the appropriate volume by assigning the `Object` field to the volume. It will then threshold the volume from the channel `Grid Name` and try to mesh this. For this the `Threshold` value is used (data dependent).

 This should then yield a mesh object under the same `Cube` name. The cube is now gone, but replaced with the meshed volume. 
<details>
<summary>Why the cube is necessary:</summary>
The volume to mesh modifier is only available to meshes, so we need to add a random mesh (here the Cube) to call this on. Thus it also disappears, but keeps its name after the modifier has been added.
</details>



 ## Rendering meshes

 Some quick notes on rendering a mesh instead of a volume (best to switch to the _Shading_ tab):
 - You can give this a new `Material`, by clicking `+ New` in the `Shading` tab with the cube selected in the `Outliner`.  The standard node is `Principled BSDF`. This contains most of what you need, play around with the values to see how the render changes!
 - If you do not make the object emit light, it needs to be lit by another source, this can be either volumetric emission, another mesh with emission, or a `Light`.
 