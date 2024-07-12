import shutil
import unittest
from polars_task.polars_task import RetailSales


class TestPolars(unittest.TestCase):
    """
    case 1 : test_main - success testcase
    case 2 : test_main -
    """
    def test_main(self):
        file_path = 'tests/mock_data/input/'
        output_path = 'tests/mock_data/output/'
        temp = RetailSales(file_path,output_path)
        temp.main()
        shutil.rmtree(output_path)