import sys, os
import importlib.util
from .KeyboardAction import KeyboardAction
from .MouseMoveAction import MouseMoveAction


def add_custom_actions():
    custom_actions = {}
    module_directory = os.path.dirname(os.path.abspath(__file__))
    
    actions_directory = os.path.join(module_directory, "custom_actions")
    
    attr_name = "action"

    for filename in os.listdir(actions_directory):
        if not filename.endswith(".py"):
            continue

        module_name = filename[:-3]
        file_path = os.path.join(actions_directory, filename)

        spec = importlib.util.spec_from_file_location(module_name, file_path)
        module = importlib.util.module_from_spec(spec)
        spec.loader.exec_module(module)

        if not hasattr(module, attr_name):
            continue

        action = getattr(module, attr_name)
        custom_actions[module_name] = action

        print(f"imported custom action: {module_name}")
    
    print(f"imported {len(custom_actions)} custom actions")
    return custom_actions

simple_actions = {
    key: KeyboardAction(key)
    for key in [
        "left",
        "right",
        "up",
        "down",
    ]
}

simple_actions.update(add_custom_actions())

mouse_move_action = MouseMoveAction()