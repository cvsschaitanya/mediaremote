from .Action import Action 
import pyautogui as pg

class SingleClickAction(Action):
    def call(self):
        try:
            pg.click()
            return 0
        except Exception as e:
            print(f"MouseMoveAction: failed to click mouse - {e}")
            return -1
        