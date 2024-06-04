from lib.solutions.CHK import checkout_solution
import pytest

class TestCheckout():
    def test_cd(self):
        assert checkout_solution.checkout("CDDC") == 70

    def test_special(self):
        assert checkout_solution.checkout("AAAA") == 180

    def test_empty(self):
        assert checkout_solution.checkout("") == 0

    def test_unkown_sku(self):
        assert checkout_solution.checkout("Z") == -1

