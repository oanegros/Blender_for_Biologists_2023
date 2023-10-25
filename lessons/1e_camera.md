
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
Here the location and rotation depends a lot more on your data :D. You can move the camera by the input values in `Object Properties` of the camera, or by pressing `G` and moving the mouse (constrain movement along an axis with `X` `Y` `Z` keys). `Rotation` and `Scale` can be done similarly with `R` and `S`.

Snap `Active Camera` to Viewport location with `Alt` `Ctrl` `Numpad 0` (check `Emulate Numpad` in `Preferences > Input` if you do not have a numpad), or alternatively, via the menu _View_ -> _Align View_ -> _Align Active Camera to View_.

## Output

Change the pixel number in x and y of the cameras under `Output Properties`, and with this the aspect ratio. Here you can also find where animations are being stored.

Render an image with `Render > Render Image` or `F12`.

## Animation

So we now have a pretty still image of our cell! Blender also has a lot of support for making animations, and seeing a 3D image as just a still image often doesn't show the data sufficiently. So now we'll try to animate the position of our camera. 

For this we need to learn about `keyframes` and the `timeline`. You can find the `timeline` at the bottom of the `Layout` tab:

 <img src="../figures/timeline empty.png" width="600"/>

This shows everything that happends over the time of your animation, which is currently nothing. 

To add an animation, we can add `keyframes` these are timepoints where we tell blender what certain values should be at that timepoint. Blender will then interpolate these values for the frames between two `keyframes`. Almost any value in blender can be used as a `keyframe` value, but for simplicity we will start with the camera position and location.

Set your `timeline` to time point `0` by dragging the blue bar (this shows the current frame you're working on). 
We will use the current camera position as the begin of our animation. We do this by adding a `keyframe` to the camera `Position` and `Rotation`: 
- in the `Object Properties` of the camera, right-click the `Position` and press `Insert keyframes` (or mouse over it and press `I`). Do the same for the camera's `Rotation`

This will turn the current values yellow. If you move away in time from the frame at which you set the `keyframe`, they will be green, indicating that they have values set at other frames.

Move to timepoint `100` in the `timeline`. This will be the end of our animation. 

Move the camera to another pretty view, where you want the animation to end. Set another keyframe for `Position` and `Rotation`.

Your timeline should now show this:

 <img src="../figures/timeline with keyframes.png" width="200"/>

(you may have to unfold the left panel to see this). This shows the two keyframes set at time `0` and `100`. To play the animation, set the current timepoint to `0` and play with `Space` or the play button.

Watch out with live playing to do this in light render modes that your system can handle. 

Render the full animation by pressing `Render > Render Animation`. This will automatically write out images for each frame to a `/tmp/` folder, which you can later compile to video using a video compiler like `ffmpeg`.

Alternatively, we can delete the current keyframes, and animate the data! If you enter `#frame / 30` in one of the `Rotation` values of the `Container` of the microscopy data, we will constantly rotate the data (the rotation will be equal to the frame number divided by 30). 


---

Now we have a succesful way to make a full render of your data! However, setting all this up took quite some time. To learn a shortcut, go to [lesson 1f](./1f_new_tif_loader.md). Or [go back to main](../README.md).