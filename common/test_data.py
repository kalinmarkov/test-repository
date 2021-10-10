import os
import csv


class TestData:

    def __init__(self, test_data_csv_path):
        self.test_data_file = os.path.realpath(test_data_csv_path)
        self.test_data_dict = {}
        self.test_data_row_list = []
        with open(self.test_data_file) as csvfile:
            reader = csv.DictReader(csvfile)
            for row in reader:
                if row['EXECUTE'] == '1':
                    self.test_data_dict = row
                    break
                else:
                    print("### Error: No test data for execution!")

    def get(self, column_name):
        return self.test_data_dict[column_name]

    def get_data_list(self):
        return self.test_data_row_list
