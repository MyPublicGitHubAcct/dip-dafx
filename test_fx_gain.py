from fx_gain import gain

"""
Tests a gain calculation (simple multiplication).

To run all tests, type pytest at top level like:
    pytest

To run only the tests in this file, do this:
    pytest -q test_fx_gain.py
"""


class TestSimpleGain:

    def test_gain_one(self):
        res = gain(0.4, 0.7)
        assert res == 0.27999999999999997

    def test_gain_two(self):
        res = gain(0.193, 0.963)
        assert res == 0.185859

