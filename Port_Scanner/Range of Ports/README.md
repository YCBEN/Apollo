# Port Scanner 🔍

This repository is part of the **Apollo Cybersecurity Series**.  
It is a Python-based port scanner that supports **range scanning** and **total scanning**, with arguments for timeout, verbosity, and summary reporting.  
This project marks the stage where I began using **command-line arguments (`argparse`)** to transform simple scripts into a reusable, professional tool.

---

## 📌 Features

- Input: valid IPv4/IPv6 address
- Modes:
  - `range` → scan a user-defined port range
  - `total` → scan all ports (1–65535)
- Timeout configurable via argument
- Verbose mode to show **CLOSED** and **FILTERED** ports
- Open port counter with summary at the end
- Exception handling for invalid input, timeouts, permission errors, and connection errors

## 🔎 Port Status Legend

This scanner uses Python exceptions to classify port states, inspired by how **Nmap** reports results:

| Python Exception         | Scanner Output | Meaning                                                   | Nmap Equivalent |
| ------------------------ | -------------- | --------------------------------------------------------- | --------------- |
| Successful connection    | **OPEN**       | A service is listening and accepted the connection        | open            |
| `ConnectionRefusedError` | **CLOSED**     | Target host refused the connection (no service listening) | closed          |
| `socket.timeout`         | **FILTERED**   | Probe was dropped silently (likely blocked by firewall)   | filtered        |
| `PermissionError`        | **FILTERED**   | Local OS/firewall restricted access to this port          | filtered        |
| Other `OSError`          | **ERROR**      | Unexpected system/network error                           | error           |

## 🚀 Usage

### Range Scan (quiet mode - only open ports)

```bash
python scanner.py 127.0.0.1 --mode range --start 20 --end 25
```

### Range Scan (verbose mode - show closed/filtered too)

```bash
python scanner.py 127.0.0.1 --mode range --start 20 --end 25 --verbose
```

### Total Scan (quiet mode)

```bash
python scanner.py 127.0.0.1 --mode total --timeout 0.5
```

### Total Scan (verbose mode)

```bash
python scanner.py 127.0.0.1 --mode total --timeout 0.5 --verbose

```
