# glxgears

## building

```
mkdir build
cd build
cmake ..
make
```

## running

This repository contains:
1) A modified version of glxgears with logs per-frame timestamp (glxgears.c)
2) A script to launch glxgears process at specified intervals (scripts/launcher.py)
3) Julia scripts (Pluto notebook) to parse, summarize and plot the generated data (scripts/report.jl)

```
vblank_mode=0 scripts/launcher.py 30 200 $HOME/data/instances.csv "build/glxgears -geometry 1280x720 -csv $HOME/data/frametimes_%i.csv"
```

The above command starts a new glxgears instance every 30 seconds, with a total of 200 instances.

# analyzing data

- Install Julia
- Run Julia and add package Pluto to open the notebook `scripts/report.jl`
- Start the notebook

Julia repl session:

```julia
julia> Pkg.add("Pluto")
julia> using Pluto
julia> Pluto.run("scripts/report.jl")
```

In the notebook, change to rootDir variable to point to the directory containing CSV files generated with the launcher command above.
