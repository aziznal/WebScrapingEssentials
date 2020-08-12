import unittest
from BaseSpyder import BaseSpyder
from EmailSender import EmailSender

from selenium.webdriver.firefox.options import Options


# IMPORTANT: execute following command in console before running this file:
#   python start_local_server.py 127.1.1.1 7123

_address = "127.1.1.1"
_port = "7123"
mock_page = "mock_webpage.html"

base_url = f"http://{_address}:{_port}/mock_webpage/{mock_page}"


def make_test_urls(cls):
    test_urls = [
        "google.com",
        "youtube.com",
        "bbc.com",
        "wikipedia.org",
        "w3schools.com"
    ]

    test_urls = ["https://www.%s/" % val for val in test_urls]
    
    cls.test_urls = test_urls


def make_spyder(cls):

    options = Options()
    options.headless = False

    path = "test_spyder_settings.json"

    cls.spyder = BaseSpyder(base_url, options=options, path_to_settings=path)


def destroy_spyder(cls):
    cls.spyder.die()


class TestSpyder(unittest.TestCase):

    @classmethod
    def setUpClass(cls):
        make_spyder(cls)
        make_test_urls(cls)

    @classmethod
    def tearDownClass(cls):
        destroy_spyder(cls)

    def setUp(self):
        self.spyder.buffer_time = 1
        self.spyder.goto(base_url)

    def test_page_source(self):
        self.assertIsNotNone(self.spyder.page_source)
        self.assertIsNotNone(self.spyder.page_soup)

    def test_goto(self):

        # Increase wait while testing non-local url
        self.spyder.buffer_time = 3

        for url in self.test_urls:
            self.spyder.goto(url)
            self.assertEqual(self.spyder.url, url)

    def test_url_assignment(self):
        with self.assertRaises(TypeError):
            self.spyder.url = "https://www.google.com"

    def test_pagesource_assign(self):
        with self.assertRaises(TypeError):
            self.spyder.page_source = "foobar"

    def test_smooth_scroll(self):
        pass

    def test_instant_scroll(self):
        pass

    def test_slow_type(self):
        pass


# class TestEmailSender(unittest.TestCase):
#     pass


if __name__ == "__main__":
    unittest.main()
