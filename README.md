# Tropopause

## Michael Hadwiger - 11814638

This repository includes an installable python module for analyzing measurement 
data of the tropopause (ECMWF ERA5 reanalysis and European MMETOP-satellite). 
The module was developed for an exercise within the course
"411.045 Selected Topics in Climate Science (Python for climate and environmental 
scientists)" at the KFU Graz in the winter term 2021/22.

The repository structure is based on the example repository created by Florian 
Ladstädter (https://gitlab.com/flad/minimal_example/)

The package provides a shell script `tropopause` with the following required arguments:
- `--lat`: Two integers as the boundaries of the latitude interval of interest.

Additional optional arguments:
- `--time`: Specify the month of the measurement to be an analyzed from the ECMWF data. Format YYYY-MM. Default: 2020-12

For further information please see `tropopause --help`. 

## Installation

Use the following command in the base directory to install:

```bash
python -m pip install .
```

For an editable ("developer mode") installation, use the following
instead:

```bash
python -m pip install -e .
```

With this, the installation is actually a link to the original source code,
i.e. each change in the source code is immediately available.

## Prerequisites

You need a working Python environment, and `pip` installed.

E.g., with `conda`:

```bash
conda create --name mynewenv python
conda activate mynewenv
python -m pip install -e .
```

## Requirements
- `xarray`
- `numpy`
- `matplotlib`