# Output figures

Up til now, we've been using the interactive render mode `Eevee`. This uses [OpenGL](https://en.wikipedia.org/wiki/OpenGL), a rasterization pipeline that estimates how things will look through a variety of algorithms. `Eevee` has significant [limitations](https://docs.blender.org/manual/en/latest/render/eevee/limitations.html). 
The other major render engine of blender is `Cycles`. This is a ray-tracing engine simulating rays of light that hit the camera or viewport. This takes more time to render, but can yield prettier results, and you can be assured that your entire volume was sampled.

You can change the render engine in the `Render Properties`.

 <img src="../figures/render properties cycles.png" width="200"/>

 Here the default `Max Samples` for both `Viewport` and `Render` is very high for this type of data (this high number is mostly relevant for complicated refractive surfaces such as glass). Usually I use 32 or 64 `Max Samples`.

 It is often necessary to rescale the `Map Range` nodes in your shaders to make `Cycles` look good. 

 **Note:** Sometimes `Eevee` looks better! And it is a lot less finicky to get it pretty. In this case it is also a good choice to just use `Eevee` in `Render` :blush:.

---

Until now we've been rendering only the first channel of the volume. To learn how to show both channels at the same time, go to [lesson 1c](./1c_multichannel.md). Or [go back to main](../README.md).