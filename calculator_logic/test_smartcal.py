from smartcal import Smartcal


class TestSmartcal:

    def test_addition(self):
        assert Smartcal.addition(5, 5) == 10

    def test_subtract(self):
        assert Smartcal.subtract(10, 3) == 7

    def test_multiply(self):
        assert Smartcal.multiply(5, 5) == 25

    def test_divide(self):
        assert Smartcal.divide(25, 5) == 5

    def test_indices(self):
        assert Smartcal.indices(5, 4) == 625
