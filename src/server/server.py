from flask import Flask, jsonify, send_from_directory, request
from flask_socketio import SocketIO
import os, sys
from actions import simple_actions, mouse_move_action

from info import generate_qr_code

app = Flask(__name__)

socketio = SocketIO(app, cors_allowed_origins="*")

@socketio.on("mouse_move")
def handle_mouse_move(data):
    dx, dy = data["dx"], data["dy"]
    print(f"Moving mouse by {dx}, {dy}")
    mouse_move_action.call(dx, dy)  # Move cursor relative to its current position

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



if __name__ == '__main__':

    port = int(os.getenv('PORT', 9000))
    generate_qr_code(port)
    socketio.run(app, host='0.0.0.0', port=port)
