from .Action import Action 
import pyautogui as pg

class KeyboardAction(Action):
    def __init__(self, key):
        self.key = key
    
    def call(self, *args, **kwargs):
        pg.press(self.key)

        return 0
