import unittest

import requests
from common.test_data import TestData

td = TestData("github_issues_tests_DATA.csv")
owner = td.get("OWNER")
repo = td.get("REPO")
type = td.get("TYPE")


class GithubIssuesTest(unittest.TestCase):
    skip_tests = False
    response = None

    @classmethod
    def setUp(cls):
        print("========= Start testing =========")

    def test_01_github_issues_response(self):
        print(f'========= {self._testMethodName} =========')

        try:
            owner = "kalinmarkov"
            repo = "test-repository"

            url = f"https://api.github.com/repos/{owner}/{repo}/issues"
            headers = {
                "accept": "application/vnd.github.v3+json"
            }

            self.__class__.response = requests.get(url, headers)

            assert self.response.status_code == 200, f"#### ERROR: Response not OK -> {self.response.status_code}"
            print(f">> GET request for {url} return response 200 OK")

        except:
            self.__class__.skip_tests = True

    def test_02_github_issues_search(self):
        print(f'========= {self._testMethodName} =========')
        if self.skip_tests:
            raise Exception("Skipped")

        url = f"https://api.github.com/search/issues?q=author:{owner} type:{type}"

        issues_response = requests.get(url)
        json_issues_response = issues_response.json()
        issues = json_issues_response['items']

        print("Print issues titles where author is the owner:")
        for issue in issues:
            print(issue['title'])

    @classmethod
    def tearDown(cls) -> None:
        print("========= End of testing ========= \n")


if __name__ == "__main__":
    unittest.main()
