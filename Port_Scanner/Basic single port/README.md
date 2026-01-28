# Port Scanner - Basic single-port 🔍

This is **Basic single-port** of the Port Scanner project.  
At this stage, the tool checks if a single port on a target host is open or closed using Python sockets, with proper input validation and exception handling.

## 📌 Overview

- Learn basic socket programming
- Validate user input (IP address and port number)
- Use `try/except` blocks for robust error handling
- Close sockets cleanly without hiding errors

## ⚡ Features

- Input: target host (must be a valid IPv4 or IPv6 address)
- Input: port number (must be numeric and non-empty)
- Output: whether the port is **OPEN** or **CLOSED**
- Exceptions handled:
  - Empty or invalid port input (`ValueError`)
  - Invalid IP address (`ipaddress` validation)
  - Timeout
  - Connection refused
  - Other unexpected errors
- Safe socket closing with explicit checks

## 🚀 Usage

```bash
python scanner.py
```
