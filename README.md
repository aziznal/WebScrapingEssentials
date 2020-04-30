# Web Scraping Essential Tools

## Why this exists
This is here to make my life easier when I'm creating a web scraper.
It includes the basic needs for each web scraping project.

## Details about each file

### [BaseSpyder.py](https://github.com/aziznal/WebScrapingEssentials/blob/master/BaseSpyder.py)

Includes basic functions a spyder needs, like goto(url) or (eventually) scrollPage(amount)

* **Constructor**:

    Takes 3 parameters:

    * **url**: obvious

    * **load_buffer**: a wait time implemented in some functions to make sure everything is loaded

    * **options**: a selenium.webdriver.firefox.options object. used to define various options.

    The Spyder goes to the provided url as soon as it's initialized.

* **refresh_page**:
    
    Causes page to refresh and to re-new the page_source.

    load_buffer is used here to make sure content has loaded before consequent operations.

* **load_settings** and **save_settings**:
  
    used to load and save spyder_settings.json

* **get_timestamp**:

    returns a timestamp including date and time. check function docs for details.

* **die**:

    Ends the spyder's miserable life in the most humane way possible.