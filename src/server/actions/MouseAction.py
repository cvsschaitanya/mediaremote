from .Action import Action
from .MouseMoveAction import MouseMoveAction
from .SingleClickAction import SingleClickAction

class MouseAction(Action):
    def __init__(self):        
        self.actions = {
            "move": MouseMoveAction(),
            "single_click": SingleClickAction(),
        }
    
    def call(self, actionData):
        actionType = actionData["type"]
        actionArgs = actionData["args"]
        
        self.actions[actionType].call(*actionArgs)
        