# Volume to mesh

Add a cube to the scene with `Add` or `Shift+A`.

Add a `Volume to Mesh` `Modifier` to the cube, under the `Modifier Properties` tab in the `Properties` panel. 

 <img src="../figures/volume to mesh properties.png" width="400"/>

 This modifier you can refer to the appropriate volume by assigning the `Object` field to the volume. It will then threshold the volume from the channel `Grid Name` and try to mesh this. For this the `Threshold` value is used (data dependent).

 This should then yield a mesh object under the same `Cube` name. 

 ## Rendering meshes

 Some quick notes on rendering a mesh instead of a volume: 
 - This needs a `Material`, the standard node is `Principled BSDF`. This contains most of what you need
 - If you do not make the object emit light, it needs to be lit by another source, this can be either volumetric emission, another mesh with emission, or a `Light`.
 