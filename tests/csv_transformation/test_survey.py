import unittest
from csv_transformation.transformation import TransformData


class TestSurvey(unittest.TestCase):
    def test_main(self):
        file_path = '/tests/mock_data/'
        samp = TransformData(file_path)
        samp.main()

        # df = samp.read_csv()
        # self.assertEquals(df.count(), 10)
