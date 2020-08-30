import unittest
from BasicSpider import BasicSpider

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


def make_spider(cls):

    options = Options()
    options.headless = False

    cls.spider = BasicSpider(base_url, options=options)


def destroy_spider(cls):
    cls.spider.die()


class TestSpider(unittest.TestCase):

    @classmethod
    def setUpClass(cls):
        make_spider(cls)
        make_test_urls(cls)

    @classmethod
    def tearDownClass(cls):
        destroy_spider(cls)

    def setUp(self):
        self.spider.buffer_time = 1
        self.spider.goto(base_url)

    def test_page_source(self):
        self.assertIsNotNone(self.spider.page_source)
        self.assertIsNotNone(self.spider.page_soup)

    def test_goto(self):

        # Increase wait while testing non-local url
        self.spider.buffer_time = 3

        for url in self.test_urls:
            self.spider.goto(url)
            self.assertEqual(self.spider.url, url)

    def test_url_assignment(self):
        with self.assertRaises(TypeError):
            self.spider.url = "https://www.google.com"

    def test_pagesource_assign(self):
        with self.assertRaises(TypeError):
            self.spider.page_source = "foobar"

    def test_smooth_scroll(self):
        pass

    def test_instant_scroll(self):
        pass

    def test_slow_type(self):
        pass


if __name__ == "__main__":
    unittest.main()
