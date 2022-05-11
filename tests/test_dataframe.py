import unittest
import pandas as pd
from pandas.testing import assert_frame_equal


class TestDataframe(unittest.TestCase):
    """
       A class for unit-testing the dataframe
       Args:
       -----
           unittest.TestCase this allows the new class to inherit
           from the unittest module
       """

    def setUp(self) -> pd.DataFrame:
        test_file_name = '../data/clean_data.csv'
        try:
            data = pd.read_csv(test_file_name,
                               sep=',',
                               header=0)
        except IOError:
            print('cannot open file')
        self.df = data

    def test_dataframe_shape(self):
        """ Test that the shape of the dataframe read in equal what we expect"""
        self.assertEqual(self.df.shape, (148506, 56))


if __name__ == '__main__':
    unittest.main()
