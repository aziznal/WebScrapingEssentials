import unittest
from BaseSpyder import BaseSpyder
from EmailSender import EmailSender

from selenium.webdriver.firefox.options import Options


# IMPORTANT: execute following command in console before running this file:
#   python start_local_server.py 127.1.1.1 7123
_address = "127.1.1.1"
_port = "7123"
mock_page = "mock_webpage.html"


class TestSpyder(unittest.TestCase):

    def setUp(self):

        url = f"http://{_address}:{_port}/mock_webpage/{mock_page}"
        options = Options()
        options.headless = True
        path = "spyder_settings_template.json"

        self.spyder = BaseSpyder(url, options=options, path_to_settings=path)

    def test_page_source(self):
        self.assertIsNotNone(self.spyder.page_source)

    def tearDown(self):
        self.spyder.die()


class TestEmailSender(unittest.TestCase):
    pass


if __name__ == "__main__":
    unittest.main()
