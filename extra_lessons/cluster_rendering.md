# Rendering on a Cluster/HPC node

Some quick tips on rendering on a cluster, and some more specific instructions for rendering on the EMBL HPC. 

For more infomration on headless running see the generic [blender documentation](https://docs.blender.org/manual/en/latest/advanced/command_line/render.html).

Example blender headless render command:
```
blender  -b projectfile.blend -s 0 -o ../renders/frame_##### -a --cycles-device CUDA --cycles-print-stats
```
`-b` is headless (no UI)
`-s` starting frame
`-a` take over all render settings from the project file
Both `--cycles-device CUDA` and `--cycles-print-stats` can be useful for debugging/optimization.

For runnning on the EMBL cluster with `SLURM`, note that there is a blender 3.5 installed Module, you can first load, making sure that you do not have to install your own version. 
Easiest is to start an sbatch on a 3090 node with a bash script containing your render command.
```
module load Blender
sbatch --mail-user=your.email@embl.de --mail-type=END -t 90:00:00 --cpus-per-task 32 -p gpu-el8 --mem=60G -C gpu=3090 run.sh
```


