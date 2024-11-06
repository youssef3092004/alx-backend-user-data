#!/usr/bin/env python3
"""
This module contains a method called filter_datum that returns the
log message obfuscated
"""

import re
from typing import List


def filter_datum(fields: List[str], redaction: str,
                 message: str, separator: str) -> str:
    """
        Replaces occurrences of certain field values in a message with a redaction string.

        Args:
            fields (List[str]): A list of field names whose values should be redacted.
            redaction (str): The string to replace the field values with.
            message (str): The original message containing the fields to be redacted.
            separator (str): The character that separates the fields in the message.

        Returns:
            str: The message with the specified field values redacted.
    """
    pattern = '|'.join(f'{field}=[^;]*' for field in fields)
    return re.sub(pattern, lambda match: f"{
                  match.group().split('=')[0]}={redaction}", message)
