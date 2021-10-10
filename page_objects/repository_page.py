from selenium.webdriver.common.by import By
from common.base_class import BaseClass


class RepositoryPage(BaseClass):

    def __init__(self, driver, url, timeout=10):
        BaseClass.__init__(self, driver=driver, timeout=timeout)
        self.navigate_to(url)
        self.driver.maximize_window()

    ISSUES_TAB_SEL = (By.ID, "issues-tab")

    def navigate_to(self, url):
        self.driver.get(url)

    def click_issues_tab(self):
        self.click_on_element("Issues tab", self.ISSUES_TAB_SEL)


class IssueTab(BaseClass):

    def __init__(self, driver, timeout=10):
        BaseClass.__init__(self, driver=driver, timeout=timeout)
        if self.verify_visibility_of_new_issue_button():
            print(">> Issues tab loaded")
        else:
            raise Exception("#### ERROR: Issues tab is not loaded! Check the logs.")

    NEW_ISSUE_BTN_SEL = (By.CSS_SELECTOR, 'summary[class*="btn-primary"]')
    SEARCH_FIELD_SEL = (By.ID, "js-issues-search")
    ISSUE_BOX_ROW_SEL = (By.CSS_SELECTOR, "div[id*='issue_']")

    def verify_visibility_of_new_issue_button(self):
        return self.visibility_of_element(self.NEW_ISSUE_BTN_SEL)

    def display_all_issues(self):
        self.clear_input_field(self.SEARCH_FIELD_SEL)
        self.find_element(*self.SEARCH_FIELD_SEL).click()
        self.press_enter_keyboard_button()

    def get_issues_list(self):
        return self.visibility_of_elements(self.ISSUE_BOX_ROW_SEL)
