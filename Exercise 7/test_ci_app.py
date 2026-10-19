import unittest

from ci_app import build_message


class BuildMessageTests(unittest.TestCase):
    def test_build_message_uses_name(self):
        self.assertEqual(build_message("Jenkins"), "Hello, Jenkins!")


if __name__ == "__main__":
    unittest.main()
