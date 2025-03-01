from .Action import Action
from .MouseMoveAction import MouseMoveAction

class MouseAction(Action):
    def __init__(self):        
        self.actions = {
            "move": MouseMoveAction()
            # "moveRel": MouseAction
        }
    
    def call(self, actionData):
        actionType = actionData["type"]
        actionArgs = actionData["args"]
        
        self.actions[actionType].call(*actionArgs)
        