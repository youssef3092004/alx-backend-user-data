#!/usr/bin/env python3
"""
This module contains a method called filter_datum that returns the
log message obfuscated
"""

import re
from typing import List
import logging

PII_FIELDS = ("name", "email", "phone", "ssn", "password")

def filter_datum(fields: List[str], redaction: str,
                 message: str, separator: str) -> str:
    """ Returns a log message obfuscated """
    for f in fields:
        message = re.sub(f'{f}=.*?{separator}',
                         f'{f}={redaction}{separator}', message)
    return message


def get_logger() -> logging.Logger:
    """
        Returns a logging object
    """
    logger = logging.getLogger("user_data") # create a logger object
    logger.setLevel(logging.INFO)   # set the log level to INFO
    logger.propagate = False    # set the propagate to False
    handler = logging.StreamHandler()  # this will out put to the console :)
    handler.setFormatter(RedactingFormatter(PII_FIELDS))    # set the formatter to the RedactingFormatter
    logger.addHandler(handler)  # add the handler to the logger
    return logger   # return the logger object

class RedactingFormatter(logging.Formatter):
    """
        Redacting Formatter class
    """

    REDACTION = "***"
    FORMAT = "[HOLBERTON] %(name)s %(levelname)s %(asctime)-15s: %(message)s"
    SEPARATOR = ";"

    def __init__(self, fields: List[str]):
        """
            Constructor
        """
        super(RedactingFormatter, self).__init__(self.FORMAT)
        self.fields = fields

    def format(self, record: logging.LogRecord) -> str:
        """
            Filters values in incoming log records using `filter_datum`
        """
        record.msg = filter_datum(
            self.fields,
            self.REDACTION,
            record.getMessage(),
            self.SEPARATOR)
        return super().format(record)
