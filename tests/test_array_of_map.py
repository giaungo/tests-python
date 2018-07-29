import unittest

from app.data_store_and_load import store, load


class TestDataStoreAndLoad(unittest.TestCase):

    def test_data_store(self):
        arr_of_dict = [{"key1": "value1", "key2": "value2"}, {"keyA": "valueA"}]
        expected = "key1=value1;key2=value2\nkeyA=valueA"
        actual = store(arr_of_dict)
        self.assertEqual(actual, expected)

    def test_data_load(self):
        str_from_arr_of_dict = "key1=value1;key2=value2\nkeyA=valueA"
        expected = [{"key1": "value1", "key2": "value2"}, {"keyA": "valueA"}]
        actual = load(str_from_arr_of_dict)
        self.assertEqual(actual, expected)
