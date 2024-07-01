# TLD Validation Tool

This is a Python script that validates a list of domains against a set of valid top-level domains (TLDs). It provides a summary report of the valid and invalid domains.

## Features

- Validates domains against a list of valid TLDs
- Provides a summary report with the number of valid and invalid domains
- Supports displaying valid or invalid domains separately

## Usage

1. Clone the repository:

`git clone https://github.com/your-username/tld-validation-tool.git`

2. Install the required dependencies:

`pip3 install -r requirements.txt`

3. Run the script with the necessary arguments:

`python3 tld_validation.py -df domains.txt`

## Options
```bash
options:
  -h, --help            show this help message and exit
  -df DOMAINS, --domains     domains file
  -tf VALIDTLD, --validtld   valid TLD file (default valid_tld.txt from SecLists )
  -in, --invaliddomains      invalid domains list in result
  -s, --silent               silent report
```

### Contributing
If you find any issues or have suggestions for improvements, feel free to open an issue or submit a pull request.
