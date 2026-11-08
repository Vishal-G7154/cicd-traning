import unittest
from app import greet


class TestApplication(unittest.TestCase):

    def test_greet(self):
        expected = "Hello Vishal! My second try on CI/CD project."

        self.assertEqual(greet(), expected)


if __name__ == "__main__":
    unittest.main()