from fx_gain import gain

"""
Tests a gain calculation (simple multiplication).

To run all tests, type pytest at top level like:
    (venv) ➜  AnoRack git:(main) ✗ pytest

To run only the tests in this file, do this:
    (venv) ➜  AnoRack git:(main) ✗ pytest -q python/test_gain.py
"""


class TestGain:

    def test_gain_one(self):
        res = gain(0.4, 0.7)
        assert res == 0.27999999999999997

    def test_gain_two(self):
        res = gain(0.193, 0.963)
        assert res == 0.185859

