from .Action import Action 
import pyautogui as pg

class MouseMoveAction(Action):
    def call(self, *args, **kwargs):
        if len(args) not in [3]:
            print("MouseMoveAction: invalid number of arguments")
            return -1
        
        return self.call(*args[:3])
    
    def call(self, x, y, dur):
        try:
            pg.moveRel(x, y, duration=dur)
            return 0
        except Exception as e:
            print(f"MouseMoveAction: failed to move mouse - {e}")
            return -1