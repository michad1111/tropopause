import xarray as xr
from tropopause import io


def test_io_ecmwf():
    assert type(io.read_gridded("ecwmf")) == type(xr.Dataset())


def test_io_metop():
    assert type(io.read_metop()) == type(xr.Dataset())


def test_io_example():
    assert type(io.read_gridded("example_gridded")) == type(xr.Dataset())
