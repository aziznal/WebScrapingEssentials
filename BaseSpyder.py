from selenium import webdriver
import os
from time import sleep
import json
from datetime import datetime
from pprint import pprint
from bs4 import BeautifulSoup

from selenium.webdriver.firefox.options import Options


class BaseSpyder:
    def __init__(self, url, buffer_time=3, options=None, path_to_settings="spyder_settings.json", **kwargs):
        """ 
        Args:

            url (str): page to load when browser is first launched

            buffer_time (int, optional): a wait-time (in seconds) to confirm things like page loads. Defaults to 3.

            options (selenium.webdriver.firefox.options.Options, optional): Use to pass custom options to the browser. Defaults to None.

            path_to_settings (str): where to save and load the spyder's settings
        """

        self.buffer_time = buffer_time
        self.url = url
        self.options = options
        self._settings_path = path_to_settings

        self.driver = webdriver.Firefox(options=self.options)

        self.goto(self.url)

        self.page_source = BeautifulSoup(self.driver.page_source, features="lxml")

        self.settings = self.load_settings()

    def goto(self, url):
        self.driver.get(url)
        sleep(self.buffer_time)

    def refresh_page(self):
        self.driver.refresh()
        sleep(self.buffer_time)

        # refresh page source to get new changes
        self.page_source = BeautifulSoup(
            self.driver.page_source, features="lxml")

    def load_settings(self):
        """
        Loads spyder_settings.json (default name),
        returns dict 
        """

        with open(self._settings_path) as spyder_settings_json:
            return json.load(spyder_settings_json)

    def save_settings(self):
        """
        saves the current running spyder's settings as json
        """
        try:

            with open(self._settings_path, 'w') as spyder_settings_json:
                json.dump(self.settings, spyder_settings_json, indent=4)
                print(f"Saved spyder_settings to {self._settings_path}")

        except Exception as e:

            print(
                f"Warning! couldn't save spyder_settings: {e}\nAttempting to Save data somewhere else...")

            _filename = 'spyder_settings_fallback' + \
                self.get_timestamp(appending_to_file_name=True) + '.txt'
            with open(_filename, 'a') as _file:
                _file.write(str(self.settings))

                print(f"Saved current spyder settings to {_filename}")

    def get_timestamp(self, appending_to_file_name=False):
        """
        returns a formatted timestamp string (e.g "2020-09-25 Weekday 16:45:37" )
        """
        if appending_to_file_name:
            formatted_time = datetime.now().strftime("%Y-%m-%d %H-%M-%S")
        else:
            formatted_time = datetime.now().strftime("%Y-%m-%d %A %H:%M:%S")

        return formatted_time

    def die(self):
        print("Squashing the spyder...")
        self.save_settings()
        self.driver.quit()
