import unittest
import configuration.driver_helper
from common.test_data import TestData
from page_objects.repository_page import RepositoryPage, IssueTab

td = TestData("github_ui_issues_tests_DATA.csv")
url = td.get("URL")
browser = td.get("BROWSER")


class GitHubUIIssueTests(unittest.TestCase):
    issues_list = []

    @classmethod
    def setUpClass(cls):
        cls.driver = configuration.driver_helper.create_driver(browser)
        cls.repository_page = RepositoryPage(cls.driver, url)

    def test_01_verify_presence_of_issues(self):
        print(f'========== {self._testMethodName} ==========')
        try:
            self.repository_page.click_issues_tab()
            issue_page = IssueTab(self.driver)
            issue_page.display_all_issues()
            self.__class__.issues_list = issue_page.get_issues_list()
            assert len(self.issues_list) > 0, "#### ERROR: There are no issues for that repository!"
            print("Debug")
        except:
            raise Exception("### Page content is not loaded")

    def test_02_check_issues_assignee(self):
        print(f'========== {self._testMethodName} ==========')
        try:
            assert False
        except:
            raise Exception("### Page content is not loaded")

    def test_03_check_issue_sidebar_attributes(self):
        print(f'========== {self._testMethodName} ==========')
        try:
            assert False
        except:
            raise Exception("### Page content is not loaded")

    def test_04_confirm_issue_is_exist_in_project(self):
        print(f'========== {self._testMethodName} ==========')
        try:
            assert False
        except:
            raise Exception("### Page content is not loaded")

    @classmethod
    def tearDownClass(cls):
        cls.driver.quit()


if __name__ == "__main__":
    unittest.main()
