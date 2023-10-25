
## Setting up a Camera

To use the `Render` mode of rendering, we have to add a camera. This can be done easiest in the `Layout` tab. 
Here press `Add` or `Shift+A` and add a camera.

You can look through the current `Active Camera` by clicking the camera icon in the `3D viewport` panel (`Active Camera` is settable in the `Outliner` panel by clicking the green camera, if only one camera is present, this is the active camera)

 <img src="../figures/view through camera.png" width="200"/>

**For an easy top view:**
In `Object Properties` set the camera `Location` to 0 in `X`/`Y` and above the volume in `Z`, and `Rotation` to 0 for all. 

 <img src="../figures/camera data properties.png" width="200"/>

Then in `Object Data Properties` set the camera to `Orthographic` and the `Orthographic Scale` to encompass the volume. 

 <img src="../figures/orthographic camera.png" width="200"/>

This is similar to a Z projection, alghough the precise type of Z projection depends on the implemented shaders/materials.
<details><summary>Orthographic vs Perspective cameras</summary> Orthographic cameras show all objects at the same scale, in perspective cameras, objects which are far away are smaller than those nearby. Orthographic projections are standard in microscopy (for Z projections, for example). Perspective projections are default in many other cases, as this is how we view the world usually. </details>

\
**Making other angles of view:**
Here the location and rotation depends a lot more on your data :D. 
The easiest way to move your camera is to move your view (`Viewport location`) and snap the camera to this location:

Snap `Active Camera` to Viewport location with `Alt` `Ctrl` `Numpad 0` (check `Emulate Numpad` in `Preferences > Input` if you do not have a numpad), or alternatively, via the menu _View_ -> _Align View_ -> _Align Active Camera to View_.

Alternatively, you can move the camera by the input values in `Object Properties` of the camera, or by pressing `G` and moving the mouse (constrain movement along an axis with `X` `Y` `Z` keys). `Rotation` can be done similarly with `R`.


## Output

Change the pixel number in x and y of the cameras under `Output Properties`, and with this the aspect ratio. Here you can also find where animations are being stored.

Render an image with `Render > Render Image` or `F12`.

---

Now we have a succesful way to make a full render of your data! But we can also make it move! To learn simple animation, go to [lesson 1f](./1f_animation.md). Or [go back to main](../README.md).