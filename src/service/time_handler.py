from datetime import datetime
from src.service.exception_handler import TimeRangeError

def to_datetime_from_str(time_str):
    return datetime.strptime(time_str, '%H:%M')

def to_str_from_datetime(time):
    return datetime.strftime(time, '%H:%M')

def time_elapsed_in_hours(start_time,end_time):
    if start_time > end_time:
        raise TimeRangeError(f'{to_str_from_datetime(end_time)} has to be greater than {to_str_from_datetime(start_time)}')
    diff = (end_time - start_time)
    return diff.seconds/3600
