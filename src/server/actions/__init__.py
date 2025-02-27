import sys, os
import importlib.util
from .KeyboardAction import KeyboardAction
from .MouseMoveAction import MouseMoveAction


simple_actions = {
    key: KeyboardAction(key)
    for key in [
        "left",
        "right",
        "up",
        "down",
        "space",
    ]
}

mouse_move_action = MouseMoveAction()