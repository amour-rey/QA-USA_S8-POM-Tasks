import time

from selenium.webdriver.common.by import By


# Defining the page class, locators and method in the class
class UrbanRoutesPage:
    # Locators as class attributes
    FROM_LOCATOR = (By.ID, ...)
    TO_LOCATOR = (By.ID, ...)
    CUSTOM_OPTION_LOCATOR = (By.XPATH, '//div[text()="Custom"]')
    DRIVE_ICON_LOCATOR = (By.XPATH, '(//img[@src="/static/media/car.8a2b1ff5.svg"])[2]')
    BOOK_BUTTON_LOCATOR = (By.XPATH, ...)
    CAMPING_LOCATOR = (By.XPATH, '//div[contains(text(),"Camping")]')
    AUDI_TEXT_LOCATOR = (By.XPATH, ...)
    ADD_DRIVER_LICENSE_LOCATOR = (By.XPATH, '(//div[contains(text(),"Add a driver")])[2]')
    FIRST_NAME_LOCATOR = (By.ID, ...)
    LAST_NAME_LOCATOR = (By.ID, ...)
    DATE_OF_BIRTH_LOCATOR = (By.ID, ...)
    NUMBER_LOCATOR = (By.ID, ...)
    ADD_BUTTON_LOCATOR = (By.XPATH, '//form/div[2]/button[1]')
    ADD_A_DRIVER_LICENCE_TITLE_LOCATOR = (By.XPATH, '//div[contains(text(),"Add a driver")]')
    VERIFICATION_TEXT_LOCATOR = (By.XPATH, ...)

    def __init__(self, driver):
        self.driver = driver  # Initialize the driver

    def enter_from_location(self, from_text):
        # Enter From
        self.driver.find_element(*self.FROM_LOCATOR).send_keys(from_text)

    def enter_to_location(self, to_text):
        # Enter To
        ...

    def click_custom_option(self):
        # Click Custom
        ...

    # Step to enter both "From" and "To" locations
    def enter_locations(self, from_text, to_text):
        ...
        ...

    def click_drive_icon(self):
        # Click Drive Icon
        ...

    def click_book_button(self):
        # Click Book Button
        ...

    def click_camping(self):
        # Click Camping
        ...

    def get_audi_text(self):
        # Return the "Audi" text
        return self.driver.find_element(*self.AUDI_TEXT_LOCATOR).text

    def click_add_driver_license(self):
        # Click Add Driver's Licence
        ...

    def enter_first_name(self, first_name):
        # Enter First Name
        self.driver.find_element(*self.FIRST_NAME_LOCATOR).send_keys(first_name)

    def enter_last_name(self, last_name):
        # Enter Last Name
        ...

    def enter_date_of_birth(self, date_of_birth):
        # Enter Date of Birth
        ...

    def enter_number(self, number):
        # Enter Number
        ...

    def click_title(self):
        # Click Add a Driver's License Title
        self.driver.find_element(*self.ADD_A_DRIVER_LICENCE_TITLE_LOCATOR).click()

    def click_add_button(self):
        # Click Add Button
        ...

    def get_verification_text(self):
        # Return the verification text
        return ...

    # Step to enter "From", "To" and to click "custom_option", "drive_icon", "book button", and "camping"
    def choose_camping_car(self, from_text, to_text):
        self.enter_from_location(...)
        self.enter_to_location(...)
        time.sleep(1)
        self....
        self....
        self....
        self....

    # Step to click "add driver's license"; to enter "first_name", "last_name", "date_of_birth", "number"; and
    # to click "title" and "add button"
    def adding_driver_license(self, first_name, last_name, date_of_birth, number):
        self.click_add_driver_license()
        self....
        self....
        self....
        self....
        self.click_title()
        self....