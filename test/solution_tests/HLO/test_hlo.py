from solutions.HLO import hello_solution


class TestHello:
    def test(self):
        assert hello_solution.hello("James") == "Hello, James!"
