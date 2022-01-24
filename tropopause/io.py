import xarray as xr
import os
from pkg_resources import resource_filename

file_path_ECMWF = resource_filename(
    __name__,
    os.path.join(
        "data",
        "ECMWF_IFS-ea-0051_an_F32-T42_yggdrasil-0.5.0_altitude_10x10_temperature.nc",
    ),
)

file_path_METOP = resource_filename(
    __name__,
    os.path.join("data", "METOP-A_GPS_2020-01-01_OPSv5.6.2_UCAR-2016.0120_L2.nc"),
)

file_path_example_gridded = resource_filename(
    __name__,
    os.path.join("../tests/data", "example_gridded.nc"),
)


def read_gridded(filename):
    """Opens gridded datafile and stores the data in xarray dataset"""
    match filename:
        case "ecwmf":
            filepath = file_path_ECMWF
            print("Read ECMWF")
        case "example_gridded":
            filepath = file_path_example_gridded
            print("Read exmaple_gridded")
        case _:
            raise NameError(f"File {filename} not pre-defined")
    ds = xr.open_dataset(filepath)
    return ds


def read_index_based(filename):
    """Opens index based datafile and stores the data in xarray dataset"""
    match filename:
        case "metop":
            filepath = file_path_METOP
            print("Read METOP")
        case "example_index":
            # filepath = file_path_example_index # TODO: generate example data
            print("Read exmaple_index")
        case _:
            raise NameError(f"File {filename} not pre-defined")
    ds = xr.open_dataset(filepath)
    return ds
