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


    def check_tests(self):
        for test_id in self.checked_tests:
            self.pass_test(test_id)

    def pass_test(self, element_id):
        """
        Check a tickmark on the mockwebpage
        """
        element = self.spider._browser.find_element_by_id(element_id)
        element.click()


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

        self.pass_test("test-get-inner-html")
        self.checked_tests.append("test-get-inner-html")


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

        self.pass_test('test-vscroll-down-to')
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

        self.pass_test("test-vscroll-up-to")
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

        self.pass_test("test-vscroll-down-by")
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

        self.pass_test("test-vscroll-up-by")
        self.checked_tests.append("test-vscroll-up-by")


    def test_vscroll_to_element(self):
        """
        instantly scroll to an element that will change once a certain y
        threshold has been passed. Check this element's innerHTML for validation.
        """
        element_y = 2300
        element_id = "hidden-element"

        expected_starting_html = "invisible"
        expected_final_html = "visible"

        starting_html = self.spider.get_element_inner_html(element_id)
        self.assertEqual(starting_html, expected_starting_html)

        self.spider.instant_vscroll_to(element_y)
        sleep(0.05) # time for item to load
        final_html = self.spider.get_element_inner_html(element_id)

        self.assertEqual(final_html, expected_final_html)

        self.pass_test("test-vscroll-to-element")
        self.checked_tests.append("test-vscroll-to-element")


    def test_instant_vscroll_to(self):
        """
        Spider should instantly arrive to the given y position.
        """

        expected_y = 1371   # Y position of instant scroll

        self.spider.instant_vscroll_to(expected_y)

        current_y = self.spider.get_page_y_offset()

        self.assertEqual(current_y, expected_y)

        self.pass_test("test-instant-vscroll-to")
        self.checked_tests.append("test-instant-vscroll-to")

    def test_instant_vscroll_by(self):
        """
        Spider should instantly scroll by given amount and land in correct position
        """

        ### Test Case 1: scrolling down
        starting_y = 145
        scroll_amount = 476
        expected_y = starting_y + scroll_amount

        self.spider.instant_vscroll_to(starting_y)
        self.spider.instant_vscroll_by(scroll_amount)

        actual_y = self.spider.get_page_y_offset()
        
        self.assertEqual(expected_y, actual_y)

        ### Test Case 2: scrolling up
        starting_y = 578
        scroll_amount = -351
        expected_y = starting_y + scroll_amount

        self.spider.instant_vscroll_to(starting_y)
        self.spider.instant_vscroll_by(scroll_amount)

        actual_y = self.spider.get_page_y_offset()

        self.assertEqual(expected_y, actual_y)

        ### Test Case 3: scrolling up to 0
        starting_y = 357
        scroll_amount = -1000
        expected_y = 0          # according to built-in js behavior

        self.spider.instant_vscroll_to(starting_y)
        self.spider.instant_vscroll_by(scroll_amount)

        actual_y = self.spider.get_page_y_offset()

        self.assertEqual(expected_y, actual_y)

        self.pass_test('test-instant-vscroll-by')
        self.checked_tests.append('test-instant-vscroll-by')


    def test_slow_type_with_id(self):

        # REFACTOR
        element_id = "slow-input-field"
        results_button_id = "slow-results-button"
        result_field_id = "slow-input-results"
        text = "This text is being typed in slowly"        

        self.spider.instant_vscroll_to(3200)
        self.spider.slow_type(sentence=text, field_id=element_id)

        self.spider.click_button(results_button_id)
        sleep(0.05)

        results = self.spider.get_element_inner_html(result_field_id)
        self.assertEqual(text, results)

        self.pass_test("test-slow-type-id")
        self.checked_tests.append("test-slow-type-id")

    def test_slow_type_with_WebElement(self):
        
        # REFACTOR
        field = self.spider._browser.find_element_by_id("slow-input-field")
        results_button_id = "slow-results-button"
        result_field_id = "slow-input-results"
        text = "This text is being typed in slowly"

        self.spider.instant_vscroll_to(3200)
        self.spider.slow_type(sentence=text, field=field)

        self.spider.click_button(results_button_id)
        sleep(0.05)

        results = self.spider.get_element_inner_html(result_field_id)
        self.assertEqual(text, results)

        self.pass_test("test-slow-type-webelement")
        self.checked_tests.append("test-slow-type-webelement")


    def unimplemented__test_click_button(self):
        pass


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
