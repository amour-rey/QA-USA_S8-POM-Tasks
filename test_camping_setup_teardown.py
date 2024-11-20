from selenium import webdriver
import time
from urban_routes_main_page_2 import UrbanRoutesPage


# Create a class for both tests
class TestUrbanRoutes:

    # Initialize the Chrome driver once for the class
    @classmethod
    def setup_class(cls):
        cls.driver = webdriver.Chrome()

    def test_add_driver_license_custom_camping_option(self):
        self.driver.maximize_window()
        self.driver.get('https://cnt-90292678-7422-48a9-9c11-9f573b3e0c4f.containerhub.tripleten-services.com')
        time.sleep(1)
        urban_routes_page = UrbanRoutesPage(self.driver)
        # Choose camping car step to enter "From", "To" and to click "custom_option", "drive_icon", "book button", and "camping"
        urban_routes_page....
        time.sleep(1)
        # Adding driver license step to click "add driver's license"; to enter "first_name", "last_name", "date_of_birth", "number"; and
        # to click "title" and "add button"
        urban_routes_page....
        time.sleep(1)

        # Verify is "Thank you!" in the verification text
        ... = urban_routes_page....
        expected_value = "Thank you!"
        assert ... in actual_value, f"Expected '{expected_value}', but got '{actual_value}'"

    # Close the browser after all tests are done
    @classmethod
    def teardown_class(cls):
        cls.driver.quit()
