import xarray as xr
from tropopause import io
from pkg_resources import resource_filename
import os


def test_io_ecmwf():
    assert type(io.read_ecmwf()) == type(xr.Dataset())


def test_io_metop():
    assert type(io.read_metop()) == type(xr.Dataset())


def test_io_example():
    file_path = resource_filename(
        __name__,
        os.path.join("data", "example_gridded.nc"),
    )
    assert type(io.read_ecmwf(file_path)) == type(xr.Dataset())
