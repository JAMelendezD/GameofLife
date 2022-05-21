# Game of Life

The idea is to write my initial Python Game of Life implementation in other
languages as faithful as possible to the Python code.

| Language    | Command                            | Memory   | Lines | Characters | Time         |
| ----------- | -----------------------------------| -------- | ----- | ---------- | ------------ |
| C (O3)      | `./conways 500 500 1000`           | 3 Mb     |  95   |   2883     | 9.35 sec     |
| Fortran (Of)| `./conways 500 500 1000`           | 4 Mb     |  97   |   2770     | 9.94 sec     |
| Rust (O3)   | `./conways 500 500 1000`           | 4 Mb     |  90   |   3088     | 11.71 sec    |
| Java        | `java Conways 500 500 1000`        | 281 Mb   | 103   |   3392     | 13.88 sec    |
| Python (JIT)| `python conways.py 500 500 1000`   | 131 Mb   |  56   |   1688     | 19.76 sec    |
| Julia       | `julia conways.jl 500 500 1000`    | 131 Mb   |  60   |   1751     | 22.72 sec    |
| JavaScript  | `node conways.js 500 500 1000`     | 120 Mb   |  84   |   2445     | 46.46 sec    |
| C#          | `./conways.exe 500 500 1000`       | 40 Mb    |  94   |   3465     | 1 min 13 sec |
| Go          | `./conways 500 500 1000`           | 9 Mb     |  92   |   2680     | 5 min 11 sec |
| Python      | `python conways.py 500 500 1000`   | 85 Mb    |  54   |   1620     | 7 min 15 sec |
| R           | `Rscript conways.r 500 500 1000`   | 86 Mb    |  55   |   1871     | 16 min 11 sec|

## Scalability

<p align="center">
  <img width="700" src="images/programs.png">
</p>

## Random

<p align="center">
  <img width="1000" src="images/random.gif">
</p>

## Glider Gun

<p align="center">
  <img width="1000" src="images/glider_gun.gif">
</p>
