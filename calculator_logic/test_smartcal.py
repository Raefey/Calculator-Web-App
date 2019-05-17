from smartcal import Smartcal


class TestSmartcal:

    def test_addition(self):
        assert Smartcal.addition(5, 5) == 10

    def test_substract(self):
        assert Smartcal.subtract(10, 3) == 7