from actions.Action import Action
import pyautogui as pg

class PlayPauseAction(Action):
    def call(self):
        pg.press('space')

        return 0

action = PlayPauseAction()