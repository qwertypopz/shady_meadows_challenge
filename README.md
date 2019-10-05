# Tommy Nguyen's QA Project Challenge
The files and code within are designed to test the functionality of 
[Sauce Labs Retreat](https://automationintesting.online/ "Sauce Labs Retreat") through Firefox.

**Special Note**

The website changed on 2019.10.04 without warning. Reservation options were initially Single, Double, Family, and Suite.
They were changed to one Twin room and three Single rooms. Additionally, the rooms had unique characteristics such as
costs and amenities but are now all the same price offer similar amenities. In summary, the options became less refined
during the testing process so the scope of the project had to be adjusted accordingly. There has been no documentation
concerning reverting the website back to the state it was in before 2019.10.04. Documentation did state that the site
resets every ten minutes, however the reservation selections have not changed.
## Features
* QA Code is currently capable of the following:
    * Navigate and validate the Welcome Splash Page
    * Reserve a room for any amount of time within the 35-day window displayed by the website's calendar
        * Given a start date, the program will navigate to the specified calendar month to make the reservation
    * Contact the business with pre-determined information
* Python files have been organized by functions of the page and a common functions file which will be expanded upon:
    * splash.py - Welcome Splash Page
    * reservation.py - Reservation for a room
    * contact.py - Contact Business
    * common_functions.py - Common Functions
* Useful blocks of code have been compiled in the common_functions.py file to be used as needed during testing.
* Verbose documentation within code to assist the developer better understand the functionality and better utilize the 
existing code.
## Assumptions
This documentation assumes that the user is familiar with Python and is using a Windows machine with an IDE configured 
for Python projects
## Requirements
### Selenium
Within the Windows Command Prompt, enter the following command:
```bash
pip install -U selenium
```
### Webdriverwrapper
Within the Windows Command Prompt, enter the following command:
```bash
pip install webdriverwrapper
```
### Firefox
Download and install the [Firefox web browser](https://www.mozilla.org/en-US/firefox/new/)
### Geckodriver
Download and unzip [geckodriver](https://github.com/mozilla/geckodriver/releases) into the same directory as the Python 
project if it does not already exist
## Common Functions
Commonly used functions have been compiled into the *common_functions.py* file with the intent of saving time and
energy when creating new functionality to the smoke test. Code with specific use-case are typically
organized in their respective file. Listed below are the commonly used functions that would be helpful when creating
a new test.
---
#####admin_login(driver, log)
* Parameters
    * driver: Allows the program to utilize the browser in the same manner a user would.
    * log: Utilizes logging functionality for testing and diagnostic purposes.
* Summary
    * Logs into the back end of the website for tasks specific to website administrators such as records, business
    queries, and reservations.
---
#####make_reservation(room, start_date, duration, driver, log)
* Parameters
    * room: Case-sensitive String value. Current site iteration only allows *Twin* or *Single*.
    * start_date: datetime variable marking the starting date of the reservation
    * duration: int variable stating the length of stay 
    * driver: Allows the program to utilize the browser in the same manner a user would.
    * log: Utilizes logging functionality for testing and diagnostic purposes
* Summary
    * The main user-side function of the website. Developers are able to emulate user behavior in making a reservation
    by passing in the required parameters. The function itself enters dummy personal information to complete the
    reservation form before submission.
 ---
#####navigate_calendar(start_date, driver, log)
* Parameters
    * start_date: datetime variable marking the starting date of the reservation
    * driver: Allows the program to utilize the browser in the same manner a user would.
    * log: Utilizes logging functionality for testing and diagnostic purposes
* Summary
    * The website opens up on the current month's calendar. If the test case requires a starting date further in the 
    future or past, then this function will navigate through the calendar until the proper calendar month is displayed.
---
#####navigate_to_main(driver, log)
* Parameters
    * driver: Allows the program to utilize the browser in the same manner a user would
    * log: Utilizes logging functionality for testing and diagnostic purposes
* Summary
    * Navigates to the main page
---
#####setup_driver(log)
*Parameters
    * log: Utilizes logging functionality for testing and diagnostic purposes
*Summary
    * This is a necessary function if the test requires any action to be done through a web browser.
---
#####setup_log()
* Summary
    * Required to incorporate logging functionality in code.
---
#####skip_splash(driver, log)
* Parameters
    * driver: Allows the program to utilize the browser in the same manner a user would
    * log: Utilizes logging functionality for testing and diagnostic purposes
* Summary
    * When first navigating to the main page, the user would typically encounter a welcome splash page, this function
    would quickly navigate through the panels and close the splash page to continue onto the main page.
---
#####verify_reservation_via_rooms(room, start_date, driver, log)
* Parameters
    * room: Case-sensitive String value. Current site iteration only allows *Twin* or *Single*.
    * start_date: datetime variable marking the starting date of the reservation
    * driver: Allows the program to utilize the browser in the same manner a user would.
    * log: Utilizes logging functionality for testing and diagnostic purposes
* Summary
    * This function navigates to the admin panel in order to validate that a reservation has been made given the type
    of reservation and starting date.