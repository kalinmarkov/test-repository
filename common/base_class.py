from selenium.webdriver import ActionChains
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


class BaseClass:
    def __init__(self, driver, timeout=10):
        self.driver = driver
        self.timeout = timeout
        self.wait = WebDriverWait(self.driver, self.timeout)

    def set_timeout(self, timeout):
        self.wait._timeout = timeout

    def find_element(self, *selector):
        return self.driver.find_element(*selector)

    def visibility_of_element(self, selector):
        return self.wait.until(EC.visibility_of_element_located(selector))

    def visibility_of_elements(self, selector):
        return self.wait.until(EC.visibility_of_any_elements_located(selector))

    def clear_input_field(self, selector):
        self.visibility_of_element(selector).clear()

    def press_enter_keyboard_button(self):
        action = ActionChains(self.driver).send_keys(Keys.ENTER)
        action.perform()

    def click_on_element(self, element_name, selector):
        try:
            self.wait.until(EC.element_to_be_clickable(selector)).click()
            print(">> {} clicked.".format(element_name))
        except:
            print("## {} not clicked! ".format(element_name) + str(selector))
            raise
