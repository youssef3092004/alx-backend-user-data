#!/user/bin/env python3
"""
This module contains a method called filter_datum that returns the
log message obfuscated
"""

import re
from typing import List


def filter_datum(fields: List[str], redaction: str,
                 message: str, separator: str) -> str:
    pattern = '|'.join(f'{field}=[^;]*' for field in fields)
    return re.sub(pattern, lambda match: f"{
                  match.group().split('=')[0]}={redaction}", message)
