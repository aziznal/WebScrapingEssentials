# Web Scraping Essential Tools

## Why this exists
This is here to make my life easier when I'm creating a web scraper.
It includes the basic needs for each web scraping project.

## Details about each file

* ### geckodriver.exe

    Here for convenience. ***I did not create nor do I own this file!***
    
    Downloaded from [here](https://github.com/mozilla/geckodriver/releases)

* ### [BaseSpyder.py](https://github.com/aziznal/WebScrapingEssentials/blob/master/BaseSpyder.py)

    Includes basic functions a spyder needs, like goto(url) or (eventually) scrollPage(amount)

    * **Constructor:**

        Takes 3 parameters:

        * **url:** obvious

        * **load_buffer:** a wait time implemented in some functions to make sure everything is loaded

        * **options:** a selenium.webdriver.firefox.options object. used to define various options.

        The Spyder goes to the provided url as soon as it's initialized.

    * **refresh_page:**
        
        Causes page to refresh and to re-new the page_source.

        load_buffer is used here to make sure content has loaded before consequent operations.

    * **load_settings** and **save_settings:**
    
        used to load and save spyder_settings.json

    * **get_timestamp:**

        returns a timestamp including date and time. check function docs for details.

    * **die**:

        Ends the spyder's miserable life in the most humane way possible.

* ### [EmailSender.py](https://github.com/aziznal/WebScrapingEssentials/blob/master/EmailSender.py)

    Sends an email with an attachment. the email's body can be html or just plain text. Uses ***email.mime***
    
    ***NOTE: parent dir must include email_settings.json. Alternatively pass settings as a parameter to the constructor.***

    *The Template for email_settings.json can be found [here](https://github.com/aziznal/WebScrapingEssentials/blob/master/email_settings.json)*

    * **Constructor:**
        
        Takes 1 optional parameter:
        * **settings:** a ***dictionary*** defining the settings **in the same format** as email_settings.json.

    * **__load_settings:** Loads email_settings.json if no settings were passed to the constructor
    * **set_email_body:** Defines the contents of the email.

        Takes two parameters:
        * ***html:*** the path to the email's html template
        * ***text:*** the plain text form of the email in case the html fails to load/render.

    * **set_attachment:** Adds an attachment to send with the email.

        Takes one parameter:
        * ***filepath:*** path to the to-be-attached file

    * **__prep_message:** N/A

    * **send_email**: Sends the email. (*note: use after ***set_email_body*** and ***set_attachment****)

* ### email_settings_template.json and spyder_settings_template.json

    These two files show how the structure of their counterparts (without the *_template* at the end) should look like
    
    When in development, make sure to create files without *_template* appended to their name.