import socket
import ipaddress

try:
    # Ask for target host (must be a valid IP)
    target = input("Enter target host (IP address): ").strip()
    while True:
        try:
            ipaddress.ip_address(target)  # validate IP
            break
        except ValueError:
            print("Invalid IP address. Please enter a valid IPv4 or IPv6.")
            target = input("Enter target host (IP address): ").strip()

    # Ask for port
    port_input = input("Enter port number: ").strip()
    while not port_input:
        print("Port cannot be empty.")
        port_input = input("Enter port number: ").strip()

    port = int(port_input)  # may raise ValueError if not numeric

    # Create socket
    sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    sock.settimeout(1)  # timeout to avoid hanging

    # Try connecting
    sock.connect((target, port))
    print(f"Port {port} is OPEN")

except ValueError as ve:
    print(f"Input error: {ve}")

except socket.timeout:
    print(f"Port {port} is CLOSED (timeout)")

except ConnectionRefusedError:
    print(f"Port {port} is CLOSED (connection refused)")

except Exception as e:
    print(f"An unexpected error occurred: {e}")

finally:
    try:
        sock.close()
    except OSError as e:
            print(f"Socket close error: {e}")
