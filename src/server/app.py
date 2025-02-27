from flask import Flask, jsonify
from flask_socketio import SocketIO
from .actions import simple_actions, mouse_move_action
from flask_cors import CORS

app = Flask(__name__)
CORS(app)
socketio = SocketIO(app, cors_allowed_origins="*")

@socketio.on("mouse_move")
def handle_mouse_move(data):
    dx, dy = data["dx"], data["dy"]
    mouse_move_action.call(dx, dy)  

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

def start():
    socketio.run(app, host='0.0.0.0', port=9000)