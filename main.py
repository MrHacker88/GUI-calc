from kivy.app import App
from kivy.uix.widget import Widget
from kivy.properties import ObjectProperty
from kivy.lang import Builder
from kivy.core.window import Window

#Window.maximize()
Window.size= (350, 400)
Builder.load_file('main.kv')

class MyLayout(Widget):
    def clear(self):
        self.ids.calc_input.text = '0'

    def button_press(self, button_pressed):
        prior = self.ids.calc_input.text

        if "ERROR!..." in prior:
            prior = ''
        
        if prior == "0":
            self.ids.calc_input.text = ''
            self.ids.calc_input.text = f'{button_pressed}'

        else:
            self.ids.calc_input.text = f'{prior}{button_pressed}'

    def one_hundredth(self):
        prior = self.ids.calc_input.text
        prior = float(prior)
        prior = prior / 100
        self.ids.calc_input.text = str(prior)
    
    def back(self):
        prior = self.ids.calc_input.text
        prior = prior[:-1]
        self.ids.calc_input.text = prior
        if self.ids.calc_input.text == '':
            self.ids.calc_input.text = "0"
    
    def pos_neg(self):
        prior = self.ids.calc_input.text
        if prior =="0":
            self.ids.calc_input.text = "0"
        elif "-" in prior:
            self.ids.calc_input.text = f'{prior.replace("-", "")}'      
        else:
            self.ids.calc_input.text = f'-{prior}'

    def decimal(self):
        prior = self.ids.calc_input.text
        num_list = prior.split("+" or "-" or "*" or "/")

        if "+" in prior or "-" in prior or "x" in prior or "/" in prior and "." not in num_list[-1]:
            prior = f'{prior}.'
            self.ids.calc_input.text = prior       
    
        elif "." in prior:
            pass
        else:
            prior = f'{prior}.'
            self.ids.calc_input.text = prior

    def math_sign(self, sign):
        prior = self.ids.calc_input.text
        self.ids.calc_input.text = f'{prior}{sign}'

    def equal(self):
        prior = self.ids.calc_input.text
        if "x" in prior:
            prior = prior.replace("x", "*")
            ans = eval(prior)
            answer = str(ans)
            self.ids.calc_input.text = f'{answer}'
        else:

            try:
                answer = eval(prior)
                ans = str(answer)
                self.ids.calc_input.text = f'{ans}'
            except:
                self.ids.calc_input.text = "ERROR!..."

class CalculatorApp(App):
    def build(self):
        self.icon = 'logo.jpg'
        return MyLayout()
    
if __name__ == '__main__':
    CalculatorApp().run()