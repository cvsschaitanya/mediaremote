import sys, os
import importlib.util
from .KeyboardAction import KeyboardAction
from .MouseAction import MouseAction


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

mouse_action = MouseAction()