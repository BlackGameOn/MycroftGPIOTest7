from mycroft import MycroftSkill, intent_handler


class CpuTemperature(MycroftSkill):
    def __init__(self):
        MycroftSkill.__init__(self)
        

    @intent_handler('temperature.cpu.intent')
    def handle_temperature_cpu(self, message):
        python //home//pi//kerems//LED_AC.py
        self.speak("Led is On") 

def create_skill():
    return CpuTemperature()




