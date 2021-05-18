from .exception_handler import InputFormatError
from src.service.abbreviations import WEEK, WEEKEND


def get_employee_name(employee_text):
    try:
        name,_ = employee_text.split('=')
    except ValueError:
        raise InputFormatError("Error obtaining employee's name (missing '=')")
        
    return name

def get_employee_working_schedule(employee_text):
    try:
        working_schedule = employee_text.split('=')[1]
    except IndexError:
        raise InputFormatError("Error obtaining employee's working schedule (missing '=')")
    
    return working_schedule

def get_working_shifts(working_schedule):
    shifts = working_schedule.split(',')
    if '' in shifts:
        raise InputFormatError('There is an empty shift (",,")')
    return shifts

def get_working_shift_day_abbreviation(working_schedule):
    day_abbreviation = working_schedule[:2]
    if day_abbreviation not in WEEK:
        if day_abbreviation not in WEEKEND:
            raise InputFormatError('The day indicated for the shift is incorrect (MO,TU,WE,TH,FR,SA,SU)') 
    return day_abbreviation


def get_working_shift_times(working_schedule):
    times = working_schedule[2:]
    try:
        start_time, end_time = times.split('-')
        __check_format_time(start_time)
        end_time = end_time.strip('\n')
        __check_format_time(end_time)
    except ValueError:
        raise InputFormatError("Error obtaining employee's working times (missing '-')")
    return start_time,end_time    

def __check_format_time(time_str):
    try:
        hours,minutes = time_str.split(':')
        if len(hours) > 2 or int(hours)>23 or int(hours)<0:
            raise InputFormatError("Format error for given hours")    
        if len(minutes) > 2 or int(minutes)>59 or int(minutes)<0:
            raise InputFormatError("Format error for given minutes")
    except ValueError:
        raise InputFormatError("Error. Time needs hours and minutes (missing ':')")