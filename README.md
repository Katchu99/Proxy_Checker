# Proxy Checker

## Overview

Proxy Checker is a Python script designed to verify the validity of various proxies. It supports multiple proxy types, including HTTP, HTTPS, SOCKS4, and SOCKS5. The script uses multiprocessing to efficiently check each proxy and outputs the working proxies to a file.

## Features

- **Supports Multiple Proxy Types:** HTTP, HTTPS, SOCKS4, and SOCKS5.
- **Multiprocessing:** Utilizes multiple processes to speed up proxy validation.
- **Customizable Input:** Reads proxies from a `proxies.txt` file.
- **Output:** Writes valid proxies to a `working_proxies.txt` file for easy usage.

## Requirements

- Python 3.x
- Required Libraries:
  - `requests`
  - `socks`
  - `multiprocessing`

## Installation

To install the required Python libraries, run:

```bash
pip install requests pysocks
```

## Usage

1. **Prepare the Proxy List:** 
   - Create a file named `proxies.txt` in the root directory of the project.
   - The file should contain proxies in the following format:

   ```plaintext
   http 192.168.1.1 8080
   socks5 192.168.1.2 1080
   ```
   - Comments can be added by prefixing the line with `#`.

2. **Run the Script:**

   Execute the script using Python:

   ```bash
   python proxy_checker.py
   ```

3. **Check the Output:**
   - Valid proxies will be written to `working_proxies.txt`.

## Contributing

Feel free to fork this repository, make improvements, and submit pull requests. Any enhancements to the proxy checking logic or support for additional proxy types are welcome!


