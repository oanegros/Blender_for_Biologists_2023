# Output figures

Up til now, we've been using the interactive render mode `Eevee`. This uses [OpenGL](https://en.wikipedia.org/wiki/OpenGL), a rasterization pipeline that estimates how things will look through a variety of algorithms. `Eevee` has significant [limitations](https://docs.blender.org/manual/en/latest/render/eevee/limitations.html). 
The other major render engine of blender is `Cycles`. This is a ray-tracing engine simulating rays of light that hit the camera or viewport. This takes more time to render, but can yield prettier results, and you can be assured that your entire volume was sampled.

You can change the render engine in the `Render Properties`.

 <img src="../figures/render properties cycles.png" width="200"/>

 Here the default `Max Samples` for both `Viewport` and `Render` is very high for this type of data (this high number is mostly relevant for complicated refractive surfaces such as glass). Usually I use 32 or 64 `Max Samples`.

 It is often necessary to rescale the `Map Range` nodes in your shaders to make `Cycles` look good. 

 **Note:** Sometimes `Eevee` looks better! And it is a lot less finicky to get it pretty. In this case it is also a good choice to just use `Eevee` in `Render` :blush:.

## Setting up a Camera

To use the `Render` mode of rendering, we have to add a camera. This can be done easiest in the `Layout` tab. 
Here press `Add` or `Shift+A` and add a camera.

You can look through the current `Active Camera` by clicking the camera icon in the `3D viewport` panel (`Active Camera` is settable in the `Outliner` panel by clicking the green camera, if only one camera is present, this is the active camera)

**For an easy top view:**
In `Object Properties` set the camera `Location` to 0 in `X`/`Y` and above the volume in `Z`, and `Rotation` to 0 for all. 

 <img src="../figures/camera data properties.png" width="200"/>

Then in `Object Data Properties` set the camera to `Orthographic` and the `Orthographic Scale` to encompass the volume. 

 <img src="../figures/orthographic camera.png" width="200"/>

This is similar to a Z projection, alghough the precise type of Z projection depends on the implemented shaders/materials.
<details><summary>Orthographic vs Perspective cameras</summary> Orthographic cameras show all objects at the same scale, in perspective cameras, objects which are far away are smaller than those nearby. Orthographic projections are standard in microscopy (for Z projections, for example). Perspective projections are default in many other cases, as this is how we view the world usually. </details>

\
**Making a side view:**
Here the location and rotation depends a lot more on your data :D. You can move the camera by the input values in `Object Properties` of the camera, or by pressing `G` and moving the mouse (constrain movement along an axis with `X` `Y` `Z` keys). `Rotation` and `Scale` can be done similarly with `R` and `S`.

## Output

Change the pixel number in x and y of the cameras under `Output Properties`, and with this the aspect ratio. Here you can also find where animations are being stored.

Render an image with `Render > Render Image` or `F12`.

---

Until now we've been rendering the data as a volume, we can also convert the volume to a mesh to render it as a surface. To learn this go to [lesson 1c](./1c_volume_to_mesh.md). Or [go back to main](../README.md).