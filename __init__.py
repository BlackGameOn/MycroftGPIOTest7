from mycroft import MycroftSkill, intent_handler


class LedControlcu(MycroftSkill):
    def __init__(self):
        MycroftSkill.__init__(self)
        

    @intent_handler('temperature.cpu.intent')
    def handle_led_ifade(self, message):
    self.speak("Led is On") 

def create_skill():
    return LedControlcu()








