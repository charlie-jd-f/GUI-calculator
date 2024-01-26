import kivy

from kivy.app import App
from kivy.uix.widget import Widget
from kivy.core.window import Window

Window.size = (300,450)
Window.minimum_width = 300
Window.minimum_height = 450

class MyCalculator(Widget):
    
    def calc_symbol(self, symbol):
        self.calc_field.text += symbol
        
    def clear(self):
        self.calc_field.text = ""
        
    def calculate(self):
        try:
            if "x" in self.calc_field.text:
                self.calc_field.text = self.calc_field.text.replace('x','*')
            elif "÷" in self.calc_field.text:
                self.calc_field.text = self.calc_field.text.replace('÷','/')
            
            self.calc_field.text = str(round(eval(self.calc_field.text),7))
        except:
            self.calc_field.text = "Error"
        
    def turn_negative(self):
        self.calc_field.text = f"-({self.calc_field.text})"
        

class MyCalculatorApp(App):
    
    def build(self):
        return MyCalculator()
    
if __name__ == '__main__':
    MyCalculatorApp().run()