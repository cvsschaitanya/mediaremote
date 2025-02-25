from flask import Flask, jsonify, send_from_directory, request
import os, sys
from actions import simple_actions, mouse_move_action
import socket, qrcode
from flask_cors import CORS

app = Flask(__name__)

# Enable Cross-Origin Resource Sharing (CORS) for the Flask app
CORS(app)

@app.route('/mouse/move', methods=['GET'])
def move_mouse():
    x = request.args.get('x', type=float)
    y = request.args.get('y', type=float)
    dur_ms = request.args.get('dur', type=float)
    
    if x is None or y is None or dur_ms is None:
        return jsonify({
            "status": "failure", 
            "message": "Missing required parameters: x, y, dur",
        }), 400

    try:
        # Assuming you have a function move_mouse_by(x, y) to move the mouse
        # move_mouse_by(x, y)
        print(f"Mouse moved by ({x}, {y}) in {dur_ms} milliseconds")
        mouse_move_action.call(x, y, dur_ms/1000)
        return jsonify({
            "status": "success", 
        }), 200
    except Exception as e:
        return jsonify({
            "status": "failure", 
            "message": f"An error occurred: {str(e)}",
        }), 500

@app.route('/keyboard/<action_name>', methods=['GET'])
def handle_action(action_name):
    if action_name not in simple_actions:
        return jsonify({
            "status": "failure", 
            "message": f"Action '{action_name}' not found!",
        }), 404

    try:
        res = simple_actions[action_name].call()
    except Exception as e:
        return jsonify({
            "status": "failure", 
            "message": f"An error occurred: {str(e)}",
        }), 500

    if res == 0:
        return jsonify({
            "status": "success", 
        }), 200
    else:
        return jsonify({
            "status": "failure", 
        }), 400

@app.route('/')
def index():
    # Serve the HTML file located in the 'templates' directory
    thisFile = os.path.abspath(sys.argv[0])
    serverDir = os.path.dirname(thisFile)
    return send_from_directory(
        os.path.join(
            serverDir,
            os.path.pardir,
            "public"
        ), "index.html"
    )


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

def generate_qr_code(url):
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
        print("".join("\u2588\u2588" if cell else "  " for cell in row))


if __name__ == '__main__':

    ip_address = get_ip_address()  # Find the local IP address
    port = 9000  # Flask server's port
    url = f"http://{ip_address}:{port}/"  # Construct the full URL

    generate_qr_code(url)
    app.run(host='0.0.0.0', port=port)
