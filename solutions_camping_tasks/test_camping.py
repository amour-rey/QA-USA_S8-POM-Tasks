import time
from selenium import webdriver

from urban_routes_main_page_2 import UrbanRoutesPage  # Import the POM class


def test_drive_custom_camping_option():
    driver = webdriver.Chrome()
    driver.get('https://cnt-90292678-7422-48a9-9c11-9f573b3e0c4f.containerhub.tripleten-services.com')

    urban_routes_page = UrbanRoutesPage(driver)

    # Use the "enter_locations" step to enter both locations
    urban_routes_page.enter_locations('East 2nd Street, 601', '1300 1st St')

    urban_routes_page.click_custom_option()
    time.sleep(2)
    urban_routes_page.click_drive_icon()
    time.sleep(2)
    urban_routes_page.click_book_button()
    time.sleep(2)
    urban_routes_page.click_camping()
    time.sleep(2)
    # Verify is "Audi A3 Sedan" in the text
    actual_value = urban_routes_page.get_audi_text()
    expected_value = "Audi A3 Sedan"
    assert expected_value in actual_value, f"Expected '{expected_value}', but got '{actual_value}'"

    driver.quit()


def test_add_driver_license_custom_camping_option():
    driver = webdriver.Chrome()
    # to maximize the window
    driver.maximize_window()
    driver.get('https://cnt-90292678-7422-48a9-9c11-9f573b3e0c4f.containerhub.tripleten-services.com')

    urban_routes_page = UrbanRoutesPage(driver)

    # Use the "enter_locations" step to enter both locations
    urban_routes_page.enter_locations('East 2nd Street, 601', '1300 1st St')

    urban_routes_page.click_custom_option()
    time.sleep(1)
    urban_routes_page.click_drive_icon()
    urban_routes_page.click_book_button()
    urban_routes_page.click_camping()
    time.sleep(1)
    urban_routes_page.click_add_driver_license()
    time.sleep(1)
    urban_routes_page.enter_first_name('Anna')
    urban_routes_page.enter_last_name('Smith')
    urban_routes_page.enter_date_of_birth('24.04.1889')
    urban_routes_page.enter_number('01 01 123456')
    urban_routes_page.click_title()
    time.sleep(1)
    urban_routes_page.click_add_button()
    time.sleep(1)

    # Verify is "Thank you!" in the verification text
    actual_value = urban_routes_page.get_verification_text()
    expected_value = "Thank you!"
    assert expected_value in actual_value, f"Expected '{expected_value}', but got '{actual_value}'"

    driver.quit()