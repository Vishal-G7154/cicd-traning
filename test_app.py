import unittest
from app import greet


class TestApplication(unittest.TestCase):

    def test_greet(self):
        expected = "Hello, DevOps Vishal!"

        self.assertEqual(greet(), expected)


if __name__ == "__main__":
    unittest.main()