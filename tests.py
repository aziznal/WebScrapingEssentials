import unittest
from BasicSpider import BasicSpider
from time import sleep, perf_counter

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


class TestSpider(unittest.TestCase):

    @classmethod
    def setUpClass(cls):
        make_spider(cls)
        make_test_urls(cls)

    @classmethod
    def tearDownClass(cls):
        sleep(3)
        cls.spider._browser.close()
        
    def setUp(self):
        self.spider.buffer_time = 1
        self.spider.goto(base_url)

        self.spider.instant_vscroll(0)


    def test_get_element_inner_html(self):
        element_id = element_class = "page-title"
        expected_innerHTML = "Welcome to this mock html webpage"

        # Test using element id as search parameter
        actual_innerHTML = self.spider.get_element_inner_html(element_id=element_id)
        self.assertEqual(actual_innerHTML, expected_innerHTML)

        # reset actual_innerHTML
        actual_innerHTML = None

        # Test using element class name as parameter
        actual_innerHTML = self.spider.get_element_inner_html(element_class=element_class)
        self.assertEqual(actual_innerHTML, expected_innerHTML)


    def test_smooth_vscroll_down(self):
        """
        Scroll from y = 0 down to 905. must stop at exactly given y.
        """

        expected_y_offset = 906     # Pixels
        given_time = 10   # Seconds

        self.spider.smooth_vscroll_down(scroll_to=expected_y_offset, approx_time=given_time)

        current_y = self.spider.get_page_y_offset()

        self.assertEqual(expected_y_offset, current_y)
    
    def test_smooth_vscroll_up(self):
        """
        Spider will scroll from y = 500 upwards
        """
        self.spider.instant_vscroll(500)

        expected_y_offset = 1     # Pixels
        given_time = 10   # Seconds

        self.spider.smooth_vscroll_up(scroll_to=expected_y_offset, approx_time=given_time)

        current_y = self.spider.get_page_y_offset()

        self.assertEqual(expected_y_offset, current_y)


    def test_smooth_vscroll_to_element(self):
        """
        Smooth scroll to an element that will only load once a certain y
        threshold has been passed. Check this element's innerHTML for validation.
        """
        element_y = 2100
        element_id = "hidden-element"

        expected_starting_html = "invisible"
        expected_final_html = "visible"

        starting_html = self.spider.get_element_inner_html(element_id)
        self.assertEqual(starting_html, expected_starting_html)

        self.spider.instant_vscroll(element_y)
        sleep(0.05) # time for item to load
        final_html = self.spider.get_element_inner_html(element_id)

        self.assertEqual(final_html, expected_final_html)


    def test_instant_vscroll(self):
        """
        Spider should instantly arrive to the given y position.
        """

        expected_y = 1371   # Y position of instant scroll

        self.spider.instant_vscroll(expected_y)

        current_y = self.spider.get_page_y_offset()

        self.assertEqual(current_y, expected_y)

    def teest_instant_vscroll_to_element(self):
        self.assertEqual(1, 0)

    
    def teest_slow_type(self):
        self.assertEqual(1, 0)


    def teest_select_from_combobox(self):
        self.assertEqual(1, 0)


    def teest_toggle_checkbox(self):
        self.assertEqual(1, 0)

    def teest_tick_checkbox(self):
        self.assertEqual(1, 0)

    def teest_untick_checkbox(self):
        self.assertEqual(1, 0)


if __name__ == "__main__":
    unittest.main()
