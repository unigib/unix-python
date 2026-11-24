import unittest
from unittest.mock import patch

import app


class OperatingEnvironmentTests(unittest.TestCase):
    def test_windows(self):
        with patch("app.platform.system", return_value="Windows"), patch.dict(
            "app.os.environ", {"WSL_DISTRO_NAME": "Ubuntu"}, clear=True
        ):
            self.assertEqual(app.operating_environment(), "Windows")

    def test_linux(self):
        with patch("app.platform.system", return_value="Linux"), patch(
            "app.platform.release", return_value="6.8.0"
        ), patch.dict("app.os.environ", {}, clear=True):
            self.assertEqual(app.operating_environment(), "Linux")

    def test_wsl_from_release(self):
        with patch("app.platform.system", return_value="Linux"), patch(
            "app.platform.release", return_value="5.15.0-Microsoft-standard-WSL2"
        ), patch.dict("app.os.environ", {}, clear=True):
            self.assertEqual(app.operating_environment(), "WSL (Linux)")

    def test_wsl_from_environment(self):
        with patch("app.platform.system", return_value="Linux"), patch(
            "app.platform.release", return_value="6.8.0"
        ), patch.dict("app.os.environ", {"WSL_DISTRO_NAME": "Ubuntu"}, clear=True):
            self.assertEqual(app.operating_environment(), "WSL (Linux)")


if __name__ == "__main__":
    unittest.main()
