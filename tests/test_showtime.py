'''Test'''
import unittest
from unittest import mock
from datetime import date
from datetime import timedelta
from datetime import datetime

from src.show_time import get_current_time
from src.show_time import substract_five_days_from_current_date
from src.show_time import get_current_date



class TestShowTime(unittest.TestCase):
    '''Test for current date'''
    @mock.patch('show_time.datetime')
    def test_current_time(self, datetime_mock):
        expected = datetime.now().strftime('11:22:40.252670')
        datetime_mock.now().strftime.return_value = '11:22:40.252670'
        print(get_current_time())
        assert get_current_time() == expected


    def test_current_date(self):
        '''Test the current date'''
        expected_day = '2022-09-29'
        #print(type(expected_day))
        #print(type(get_current_date()))
        self.assertEqual(str(get_current_date()), expected_day)



    def test_date_five_days_before(self):
        '''Test substracts 5 days from current day'''
        with mock.patch('show_time.datetime', return_value = '2022-9-24'):
            days_to_substract = 5
            assert substract_five_days_from_current_date() == (date.today()
                                                                - timedelta(days_to_substract))


    def test_time_now(self):
        '''Test the current time'''
        days_to_substract = 5
        assert substract_five_days_from_current_date() == (date.today()
                                                             - timedelta(days_to_substract))


if __name__ == '__main__':
    unittest.main()
