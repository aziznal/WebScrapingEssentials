from selenium import webdriver
from time import sleep
from datetime import datetime
from bs4 import BeautifulSoup

from selenium.webdriver.firefox.options import Options


default_options = Options()
default_options.headless = True


class BasicSpider:
    def __init__(self, url, sleep_time=3, options=default_options):
        """ 
        Args:
        
            url (str): page to load when browser is first launched
            sleep_time (int): a wait-time (in seconds) to allow things like page loads to finish.
            options (selenium.webdriver.firefox.options.Options): custom options for browser
        """

        self.sleep_time = sleep_time
        self._browser = webdriver.Firefox(options=options)

        self.page_soup = None


    def _load_page_soup(self):
        return BeautifulSoup(self.page_source, features="lxml")


    def wait(self, time=None):
        
        if time is None:
            time = self.sleep_time    

        sleep(self.sleep_time)


    def goto(self, url, wait=False, wait_for=None):
        """
        Navigate to given URL. Note that some pages will not load all elements
        even if driver thinks the page has been loaded. hence why there's a wait param
        """
        self._browser.get(url)

        if wait:
            self.wait(wait_for)


    def refresh_page(self, wait=False, wait_for=None):
        """
        Refresh the page and reset local variables to get new page source.
        """
        self._browser.refresh()

        if wait:
            self.wait(wait_for)

        # refresh page source to get new changes
        self.page_soup = self._load_page_soup()


    def get_timestamp(self, for_filename=False):
        """
        returns a formatted timestamp string (e.g "2020-09-25 Weekday 16:45:37" )
        """
        if for_filename:
            formatted_time = datetime.now().strftime("%Y-%m-%d %H-%M-%S")
        else:
            formatted_time = datetime.now().strftime("%Y-%m-%d %A %H:%M:%S")

        return formatted_time


    def smooth_vscroll(self, scroll_to=None, velocity=10):
        """
        Slowly scroll to a given y coordinate. if scroll_to is not given,
        then scroll down infinitely, but stop when the bottom is reached.
        """
        pass

    def instant_vscroll(self, scroll_to):
        """
        Instantly scroll to a given y coordinate. if scroll_to is not given,
        then scroll down to bottom of page.
        """

    def smooth_hscroll(self, scroll_to):
        pass

    def instant_hscroll(self, scroll_to):
        pass


    def slow_type(self, field, sentence, speed):
        """
        Slowly send text to a given input field
        """


    def select_from_combobox(self, combobox, selection):
        """
        Select an item from a combobox
        """
        pass


    def toggle_checkbox(self, checkbox):
        pass
        
    def tick_checkbox(self, checkbox):
        """
        Raises _undefined_ exception if given checkbox is already ticked
        """
        pass

    def untick_checkbox(self, checkbox):
        """
        Raises _undefined_ exception if given checkbox is already unticked
        """
        pass
