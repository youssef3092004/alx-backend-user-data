#!/usr/bin/env python3
"""
This module contains a method called filter_datum that returns the
log message obfuscated
"""

import re
from typing import List
import logging

def filter_datum(fields: List[str], redaction: str,
                 message: str, separator: str) -> str:
    """ Returns a log message obfuscated """
    for f in fields:
        message = re.sub(f'{f}=.*?{separator}',
                         f'{f}={redaction}{separator}', message)
    return message
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
        record.msg = filter_datum(self.fields, self.REDACTION, record.getMessage(), self.SEPARATOR)
        return super().format(record)
