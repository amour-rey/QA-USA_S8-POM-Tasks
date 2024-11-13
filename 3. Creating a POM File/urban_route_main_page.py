from selenium.webdriver.common.by import By


# Defining the page class, locators and method in the class
class UrbanRoutesPage:
    # Locators as class attributes
    FROM_LOCATOR = (By.ID, 'from')
    TO_LOCATOR = (By.ID, 'to')
    CUSTOM_OPTION_LOCATOR = (By.XPATH, '//div[text()="Custom"]')
    BIKE_ICON_LOCATOR = ...
    BIKE_TEXT_LOCATOR = ...
    DURATION_TEXT_LOCATOR = ...

    def __init__(self, driver):
        self.driver = driver  # Initialize the driver

    def enter_from_location(self, from_text):
        # Type the "From" location
        self.driver.find_element(*self.FROM_LOCATOR).send_keys(from_text)

    def enter_to_location(self, to_text):
        # Type the "To" location
        self.driver.find_element(*self.TO_LOCATOR).send_keys(to_text)

    def click_custom_option(self):
        # Click the "Custom" option
        ...

    def click_bike_icon(self):
        # Click the "Bike" icon
        ...

    def get_bike_text(self):
        # Return the "Bike" text
        ...

    # The new method returning the "Duration" text
    def get_duration_text(self):
        ...

    # Step to enter both "From" and "To" locations
    def enter_locations(self, from_text, to_text):
        ...
