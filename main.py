import pyautogui as pt
import pyperclip as pc
from pynput.mouse import Controller, Button
import time
from respone_WP import response


mouse = Controller()


class Whatsapp:
    def __init__(self, speed=5, click_speed=1):
        self.speed = speed
        self.click_speed = click_speed
        self.message = ''
        self.last_message = ''

    def open_whats_app(self):
        try:

            position = pt.locateOnScreen('logo.jpg', confidence=.7)
            pt.moveTo(position[0:2], duration=self.speed)
            pt.moveRel(0, 0, duration=self.speed)
            pt.click(interval=self.click_speed)
            time.sleep(3)
        except Exception as e:
            print('Exceptoion (nav_green_dot) ', e)

    def nav_green_dot(self):
        try:
            position = pt.locateOnScreen('unread.jpg', confidence=.7)
            pt.moveTo(position[0:2], duration=self.speed)
            pt.moveRel(160, 280, duration=self.speed)
            pt.doubleClick(interval=self.click_speed)
        except Exception as e:
            print('Exceptoion (nav_green_dot) ', e)

    def nav_input_box(self):
        try:
            position = pt.locateOnScreen('clipborad.jpg', confidence=.7)
            pt.moveTo(position[0:2], duration=self.speed)
            pt.moveRel(80, 30, duration=self.speed)
            pt.doubleClick(interval=self.click_speed)
        except Exception as e:
            print('Exceptoion (nav_input_box) ', e)
    def nav_message(self):
        try:
            position = pt.locateOnScreen('clipborad.jpg', confidence=.7)
            pt.moveTo(position[0:2], duration=self.speed)
            pt.moveRel(10, -70, duration=self.speed)
            pt.tripleClick(interval=.3)

        except Exception as e:
            print('Exceptoion (nav_input_box) ', e)
    def get_message(self):
        mouse.click(Button.left, 3)
        time.sleep(self.speed)
        mouse.click(Button.right, 1)
        time.sleep(self.speed)
        pt.moveRel(10, 10 , duration=self.speed)
       # mouse.click(Button.left, 1)
        pt.moveRel(100, -250, duration=self.speed)
        pt.doubleClick(interval=self.speed)
        time.sleep(1)

        self.message = pc.paste()
        print("User says ", self.message)
    def send_message(self):
        try:
            if self.message != self.last_message:
                bot_response = response(self.message)
                print("Your message ", bot_response)
                pt.typewrite(bot_response, interval=.0)
                pt.typewrite('\n')
                self.last_message = self.message
                if(self.message== "1"):
                    print("User acknowledged")

            else:
                print("No new msgs ")
        except Exception as e:
            print('Exceptoion (nav_input_box) ', e)



wa_bot = Whatsapp(speed=.5, click_speed=.4)
time.sleep(2)
wa_bot.open_whats_app()
wa_bot.nav_green_dot()
wa_bot.nav_input_box()
wa_bot.nav_message()
wa_bot.get_message()
wa_bot.send_message()
#wa_bot.nav_green_dot()


