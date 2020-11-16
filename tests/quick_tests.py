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

        for test_id in cls.checked_tests:
            cls.pass_test(cls, test_id)

        sleep(5)
        cls.spider._browser.close()
        
    def setUp(self):
        self.spider.buffer_time = 1
        self.spider.goto(base_url)

        self.spider.instant_vscroll_to(0)

        # self.check_tests()


    def check_tests(self):
        for test_id in self.checked_tests:
            self.pass_test(test_id)

    def pass_test(self, element_id):
        """
        Check a tickmark on the mockwebpage
        """
        element = self.spider._browser.find_element_by_id(element_id)
        element.click()


    def _assert_valueError_raised(self, method):
        # Negative y
        with self.assertRaises(ValueError):
            method(-500)
        
        # Float y
        with self.assertRaises(ValueError):
            method(213.465)

        # Negative speed
        with self.assertRaises(ValueError):
            method(100, speed=-2)

        # Float speed
        with self.assertRaises(ValueError):
            method(100, speed=3.564)


    def test_get_element_text(self):
        field_id = "slow-input-field"
        field = self.spider._browser.find_element_by_id(field_id)

        starting_text = "Have you ever been to the cloud district?"

        element_y = self.spider.get_element_y(element_id=field_id)

        self.spider.instant_vscroll_to(element_y)
        self.spider.slow_type(text=starting_text, field=field, speed_range=(0.02, 0.08))

        # Confirm field is filled with given text
        current_text = self.spider.get_element_text(element_id=field_id)
        self.assertEqual(current_text, starting_text)

        self.checked_tests.append("get-element-text-test")

if __name__ == "__main__":
    unittest.main()
