from mycroft import MycroftSkill, intent_handler


class LedControlcu(MycroftSkill):
    def __init__(self):
        MycroftSkill.__init__(self)
        

    @intent_handler('temperature.cpu.intent')
    def handle_led_ifade(self, message):
        try:
            python //home//pi//kerems//LED_AC.py
            self.speak("Led is On") 
        except:
            self.speak("Led Operation İs Failed BlackGame")

def create_skill():
    return LedControlcu()








