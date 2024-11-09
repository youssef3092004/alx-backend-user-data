# Personal Data

This project focuses on implementing secure personal data handling in Python. Each file contains specific implementations for data privacy and security.

## Files

### [encrypt_password.py](./encrypt_password.py)
- Implements password encryption using bcrypt
- Functions for hashing and validating passwords
- Secure password storage implementation

### [filtered_logger.py](./filtered_logger.py)
- Logging system with PII data filtering
- RedactingFormatter class for secure logging
- Functions to handle sensitive data in logs
- Pattern matching for PII detection

### [main.py](./main.py)
- Main testing file
- Examples of usage for the implemented functions
- Demonstration of data privacy features

## Requirements
- Python 3.7+
- bcrypt
- mysql-connector-python
- mysqlclient

## Usage
```python
# Example of password encryption
from encrypt_password import hash_password
password = hash_password("my_password")

# Example of filtered logging
from filtered_logger import filter_datum
fields = ["password", "email"]
filtered_data = filter_datum(fields, '***', message, separator)
```

## Environment Variables
- `PERSONAL_DATA_DB_USERNAME`: Database username
- `PERSONAL_DATA_DB_PASSWORD`: Database password
- `PERSONAL_DATA_DB_HOST`: Database host
- `PERSONAL_DATA_DB_NAME`: Database name

