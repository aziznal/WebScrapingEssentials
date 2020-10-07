import unittest
from BasicSpider import BasicSpider
from time import sleep, perf_counter

from selenium.webdriver.firefox.options import Options


# # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # 

# dev_note:
#     This file is meant to include only the tests that are currently
#     being worked on, which avoids having to run the entire test suite
#     during development of a new feature.
#     
#     launch this file using: `npm run qtests`

# # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # 


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


class TestSpider(unittest.TestCase):

    @classmethod
    def setUpClass(cls):
        make_spider(cls)
        make_test_urls(cls)

        cls.checked_tests = []

    @classmethod
    def tearDownClass(cls):
        sleep(3)
        cls.spider._browser.close()
        
    def setUp(self):
        self.spider.buffer_time = 1
        self.spider.goto(base_url)

        self.spider.instant_vscroll_to(0)

        self.check_tests()


    def unimplemented__test_select_from_combobox(self):
        self.assertEqual(1, 0)


    def unimplemented__test_toggle_checkbox(self):
        self.assertEqual(1, 0)

    def unimplemented__test_tick_checkbox(self):
        self.assertEqual(1, 0)

    def unimplemented__test_untick_checkbox(self):
        self.assertEqual(1, 0)


if __name__ == "__main__":
    unittest.main()
