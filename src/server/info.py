
import socket, qrcode
import sys

def get_ip_address():
    # Get the local IP address of the machine
    s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    s.settimeout(0)
    try:
        # This attempts to connect to an external IP (Google DNS) to find the local IP
        s.connect(('10.254.254.254', 1))
        ip_address = s.getsockname()[0]
    except Exception:
        ip_address = '127.0.0.1'  # Default to localhost if no network found
    finally:
        s.close()
    
    return ip_address

def generate_qr_code(port):
    ip_address = get_ip_address()

    url = f"http://{ip_address}:{port}/"
    
    qr = qrcode.QRCode(
        version=1,
        error_correction=qrcode.constants.ERROR_CORRECT_L,
        box_size=10,
        border=4,
    )
    qr.add_data(url)
    qr.make(fit=True)

    # Convert the QR code to terminal-friendly output
    qr_terminal = qr.get_matrix()
    print(f"Scan this QR code with your phone to access the site at {url}:")
    for row in qr_terminal:
        print("".join("\u2588\u2588" if cell else "  " for cell in row), file=sys.stderr)

