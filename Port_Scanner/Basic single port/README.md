# Port Scanner - Basic single-port 🔍

This is **Basic single-port** of the Port Scanner project.  
At this stage, the tool checks if a single port on a target host is open or closed using Python sockets, with proper exception handling.

## 📌 Overview

- Learn basic socket programming
- Use `try/except` blocks for error handling
- Interpret connection results (open vs closed)

## ⚡ Features

- Input: target host (IP or domain) and a single port
- Output: whether the port is **OPEN** or **CLOSED**
- Exceptions handled:
  - Timeout
  - Connection refused
  - Invalid host
  - Other unexpected errors

## 🚀 Usage

```bash
python scanner.py
```
