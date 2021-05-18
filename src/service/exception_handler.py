import logging

class EmptyFileError(Exception):
    
    def __init__(self):
        logging.error('The given file is empty')
        exit(1)


class InputFormatError(Exception):
    
    def __init__(self, message):
        self.message = message
        logging.error(self.message)
        exit(1)


class TimeRangeError(Exception):

    def __init__(self, message):
        self.message = message
        logging.error(self.message)
        exit(1)