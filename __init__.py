from mycroft import MycroftSkill, intent_handler


class LedControlcu(MycroftSkill):
    def __init__(self):
        MycroftSkill.__init__(self)
        

    @intent_handler('ledled.intent')
    def handle_led_ifade(self, message):
        try:
            python //home//pi//kerems//LED_AC.py

def create_skill():
    return LedControlcu()








