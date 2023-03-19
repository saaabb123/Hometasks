class DateTimeError(Exception):
    def __init__(self,component,value,text):
        self.component = component
        self.value = value
        self.text = text
    
   
    def __str__(self):
        return f"Invalid value: {self.value} for {self.component}. It should be {self.text}"