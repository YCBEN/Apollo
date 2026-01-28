import socket
import ipaddress
import argparse

def validate_ip(ip_str):
    """Validate IPv4/IPv6 address."""
    try:
        ipaddress.ip_address(ip_str)
        return ip_str
    except ValueError:
        raise argparse.ArgumentTypeError(f"{ip_str} is not a valid IP address")

def scan_ports(target, start_port, end_port, timeout, verbose):
    print(f"\nScanning {target} from port {start_port} to {end_port}...\n")
    open_count = 0  # counter for open ports

    for port in range(start_port, end_port + 1):
        try:
            sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
            sock.settimeout(timeout)
            sock.connect((target, port))
            print(f"Port {port} is OPEN")
            open_count += 1
        except socket.timeout:
            if verbose:
                print(f"Port {port} is FILTERED (timeout)")
        except ConnectionRefusedError:
            if verbose:
                print(f"Port {port} is CLOSED")
        except PermissionError:
            if verbose:
                print(f"Port {port} is FILTERED (restricted by OS/firewall)")
        except OSError as e:
            if verbose:
                print(f"Port {port} error: {e}")
        finally:
            sock.close()

    # summary
    if open_count > 0:
        print(f"\n Scan complete: {open_count} open port(s) found.")
    else:
        print("\n Scan complete: No open ports found.")

def scan_all_ports(target, timeout, verbose):
    print(f"\nScanning all ports (1–65535) on {target}...\n")
    open_count = 0

    for port in range(1, 65536):  # skip port 0
        try:
            sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
            sock.settimeout(timeout)
            sock.connect((target, port))
            print(f"Port {port} is OPEN")
            open_count += 1
        except socket.timeout:
            if verbose:
                print(f"Port {port} is FILTERED (timeout)")
        except ConnectionRefusedError:
            if verbose:
                print(f"Port {port} is CLOSED")
        except PermissionError:
            if verbose:
                print(f"Port {port} is FILTERED (restricted by OS/firewall)")
        except OSError as e:
            if verbose:
                print(f"Port {port} error: {e}")
        finally:
            sock.close()

    if open_count > 0:
        print(f"\n Scan complete: {open_count} open port(s) found.")
    else:
        print("\n Scan complete: No open ports found.")

if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="Port Scanner 🔍 (Apollo Cybersecurity Series)")
    parser.add_argument("target", type=validate_ip, help="Target host (valid IPv4/IPv6)")
    parser.add_argument("--mode", choices=["range", "total"], default="range",
                        help="Choose scan mode: 'range' or 'total' (default: range)")
    parser.add_argument("--start", type=int, default=1, help="Start port (for range mode)")
    parser.add_argument("--end", type=int, default=1024, help="End port (for range mode)")
    parser.add_argument("--timeout", type=float, default=1.0, help="Timeout in seconds (default: 1.0)")
    parser.add_argument("--verbose", action="store_true", help="Show CLOSED and FILTERED ports")
    args = parser.parse_args()

    if args.mode == "range":
        scan_ports(args.target, args.start, args.end, args.timeout, args.verbose)
    else:
        scan_all_ports(args.target, args.timeout, args.verbose)
