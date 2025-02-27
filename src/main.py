from server.app import start as start_app
from server.ui import start as start_ui
import threading

if __name__ == '__main__':

    # Run the ui in a separate thread
    ui_thread = threading.Thread(target=start_ui)
    ui_thread.start()

    print("Server is running in a separate thread.")
    start_app()
    