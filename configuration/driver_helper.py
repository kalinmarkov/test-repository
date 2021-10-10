import os
from selenium import webdriver


def create_driver(browser_name):
    if browser_name == "chrome":
        return webdriver.Chrome(get_driver_exe_path(browser_name))
    if browser_name == "firefox":
        return webdriver.Firefox(get_driver_exe_path(browser_name))


def get_driver_exe_path(browser_name):
    directory = os.path.dirname(__file__)
    if browser_name == "chrome":
        return os.path.join(directory, "drivers/chromedriver.exe")
    # FF driver is not added to the project
    if browser_name == "firefox":
        return os.path.join(directory, "drivers/gechodriver.exe")


def handle_exception(driver, sreenshot_name):
    driver.save_screenshot(f"Error_{sreenshot_name}")
