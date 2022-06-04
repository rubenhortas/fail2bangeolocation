import unittest


class AllOk(unittest.TestCase):
    def set_ip(self):
        """Call before every test case."""
        pass

    def tear_down(self):
        """Call after every test case."""
        pass

    def test_a(self):
        pass


if __name__ == "__main__":
    unittest.main()  # run all tests
