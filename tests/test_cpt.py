import numpy as np
from tropopause import cpt
from tropopause import io


lat_range = (-50, 50)
time = np.datetime64("2021-12")


def test_cpt_gridded():
    ds = cpt.calc_from_gridded(io.read_gridded("ecwmf"), lat_range, time)
    assert ds.cpt_temp.values > 0
    assert ds.cpt_alt.values > 0
    assert ds.temperature.ndim == 1
    assert ds.altitude.shape == ds.temperature.shape
    assert ds.time.size == 1
    assert ds.lat_limit.size == 2


def test_cpt_index():
    ds = cpt.calc_from_index_based(io.read_index_based("metop"), lat_range)
    assert ds.cpt_temp.values > 0
    assert ds.cpt_alt.values > 0
    assert ds.temperature.ndim == 1
    assert ds.altitude.shape == ds.temperature.shape
    assert ds.time_limit.size == 2
    assert ds.lat_limit.size == 2


def test_cpt_example():
    ds = cpt.calc_from_gridded(io.read_gridded("example_gridded"), lat_range, time)
    assert ds.cpt_temp.values > 0
    assert ds.cpt_alt.values > 0
    assert ds.temperature.ndim == 1
    assert ds.altitude.shape == ds.temperature.shape
    assert ds.time.size == 1
    assert ds.lat_limit.size == 2
