import unittest
from csv_transformation.transformation import TransformData

class TestSurvey(unittest.TestCase):
    def test_main(self):
        file_path = 'tests/mock_data/input/'
        samp = TransformData(file_path)
        samp.main()
        df = samp.read_csv(file_path, 'output.csv')
        self.assertEquals(df.height, 16)
