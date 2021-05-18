import os
from src.service.exception_handler import EmptyFileError

def get_file_path(file_name):
    current_dir = os.getcwd()
    complete_path = os.path.join(current_dir, file_name)
    return complete_path                                                                    


def read_file_lines(file_name):
    file_path = get_file_path(file_name)  
    lines = []
    try:
        with open(file_path) as file:
            lines = file.readlines()
        if not lines:
            raise EmptyFileError()    
    except FileNotFoundError:
        print('File not found')

    return lines