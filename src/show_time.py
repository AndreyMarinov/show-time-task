'''Modul that shows the current time and date'''

from datetime import datetime
from datetime import timedelta
from datetime import date


def get_current_time():
    '''Function that represents the current time '''
    return datetime.now().strftime('%H:%M:%S.%f')



def get_current_date():
    '''Function that represents the current date in order y/m/d'''
    return date.today()



def substract_five_days_from_current_date():
    '''Function that substract five days from the current date'''
    days_to_substract = 5
    return date.today() - timedelta(days_to_substract)
