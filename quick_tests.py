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


    def test_smooth_vscroll_down_to(self):
        """
        Scroll from y = 0 down to 905. must stop at exactly given y.
        """
        expected_y = 357

        self.spider.smooth_vscroll_down_to(expected_y)

        current_y = self.spider.get_page_y_offset()
        self.assertEqual(expected_y, current_y)

        self._assert_valueError_raised(self.spider.smooth_vscroll_down_to)

        self.checked_tests.append('test-vscroll-down-to')
    
    def test_smooth_vscroll_up_to(self):
        """
        Spider will scroll from y = 157 to exactly 0
        """

        starting_y = 157
        expected_y = 0     # Pixels

        self.spider.instant_vscroll_to(157)
        self.spider.smooth_vscroll_up_to(expected_y)

        current_y = self.spider.get_page_y_offset()

        self.assertEqual(expected_y, current_y)

        self._assert_valueError_raised(self.spider.smooth_vscroll_up_to)

        self.checked_tests.append("test-vscroll-up-to")


    def test_smooth_vscroll_down_by(self):
        """
        Spider should arrive at expected_y
        """
        starting_y = 249
        expected_y = 501

        difference = expected_y - starting_y

        self.spider.instant_vscroll_to(starting_y)
        self.spider.smooth_vscroll_down_by(difference)

        actual_final_y = self.spider.get_page_y_offset()

        self.assertEqual(actual_final_y, expected_y)

        # TODO: add test for when given amount exceeds page height

        self._assert_valueError_raised(self.spider.smooth_vscroll_down_by)

        self.checked_tests.append("test-vscroll-down-by")

    def test_smooth_scroll_up_by(self):
        """
        Spider should arrive at expected_y
        """

        # Test when starting_y > expected_y
        starting_y = 452
        expected_y = 127

        difference = starting_y - expected_y

        self.spider.instant_vscroll_to(starting_y)
        self.spider.smooth_vscroll_up_by(difference)

        actual_final_y = self.spider.get_page_y_offset()

        self.assertEqual(actual_final_y, expected_y)

        # Test when starting_y < expected_y
        starting_y = 357
        expected_y = 0

        difference = 500

        self.spider.instant_vscroll_to(starting_y)
        self.spider.smooth_vscroll_up_by(difference)

        actual_final_y = self.spider.get_page_y_offset()

        self.assertEqual(actual_final_y, expected_y)

        self._assert_valueError_raised(self.spider.smooth_vscroll_up_by)

        self.checked_tests.append("test-vscroll-up-by")


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
