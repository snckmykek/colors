__version__ = "0.0.1"

from kivy.app import App

from kivy.config import Config

Config.set('graphics', 'resizable', '1')
Config.set('graphics', 'width', '360')
Config.set('graphics', 'height', '640')

from kivy.lang.builder import Builder

from kivy.uix.boxlayout import BoxLayout
from kivy.uix.button import Button
from kivy.uix.popup import Popup
from kivy.core.window import Window

Builder.load_file('mainscreen2.kv')


# Window
class WindowSettings:
    size: tuple
    width: int
    height: int

    def __init__(self):
        self.width = Window.width
        self.height = Window.height
        self.size = (self.width, self.height)


WINDOW = WindowSettings()


class ColorPage(Button):

    def __init__(self, **kwargs):
        super(ColorPage, self).__init__(**kwargs)


class ButtonPage(Button):

    def __init__(self, **kwargs):
        super(ButtonPage, self).__init__(**kwargs)


class MainBoxLayout(BoxLayout):

    def __init__(self, **kwargs):
        super(MainBoxLayout, self).__init__(**kwargs)

        self.colors = [(.22, .9, .41, 1), (.2, .0, .5, 1), (.11, .19, .33, 1),
                       (.43, .89, .08, 1), (.26, .31, .26, 1), (.75, .99, .12, 1)]

        self.fill_colors()


    def fill_colors(self):
        # if self.ids:
        self.ids.content_box_1.clear_widgets()
        self.ids.content_box_2.clear_widgets()
        self.ids.content_box_3.clear_widgets()
        self.colors.sort()
        for color in self.colors:
            CP = ColorPage()
            CP2 = ColorPage()
            BP = ButtonPage()
            BP.background_color = color
            CP.background_color = color
            CP2.background_color = color
            BP.text = str(color)
            CP.text = str(color)
            CP2.text = str(color)
            self.ids.content_box_1.add_widget(CP)
            self.ids.content_box_2.add_widget(CP2)
            self.ids.content_box_3.add_widget(BP)


    def click_button(self):
        popup = ColorsRedactor()
        popup.parent_box = self
        popup.open()

class ColorsRedactor(Popup):

    def __init__(self, **kwargs):
        super(ColorsRedactor, self).__init__(**kwargs)

        self.parent_box = None
        self.colors_list = list()

    def on_pre_open(self):
       self.colors_list = self.parent_box.colors
       self.change_colors()


    def change_colors(self):
        self.ids.colors_box.clear_widgets()
        self.colors_list.sort()
        for color in self.colors_list:
            C = ColorRepresentation()
            C.ids.red.text = str(color[0])
            C.ids.green.text = str(color[1])
            C.ids.blue.text = str(color[2])
            C.ids.transparency.text = str(color[3])
            C.ids.red.background_color = color
            C.ids.green.background_color = color
            C.ids.blue.background_color = color
            C.ids.transparency.background_color = color
            self.ids.colors_box.add_widget(C)

    def add_color(self):
        C = ColorRepresentation()
        color = (1, 1, 1, 1)
        C.ids.red.text = str(color[0])
        C.ids.green.text = str(color[1])
        C.ids.blue.text = str(color[2])
        C.ids.transparency.text = str(color[3])
        C.ids.red.background_color = color
        C.ids.green.background_color = color
        C.ids.blue.background_color = color
        C.ids.transparency.background_color = color
        self.ids.colors_box.add_widget(C)

    def change_colors_button(self):
        self.refresh_colors_list()
        self.change_colors()

    def refresh_colors_list(self):
        new_colors_list = []
        for color_box in self.ids.colors_box.children:
            new_colors_list.append(tuple([float(color_box.ids.red.text),
                                         float(color_box.ids.green.text),
                                         float(color_box.ids.blue.text),
                                         float(color_box.ids.transparency.text)
                                          ]
                                         )
                                   )
        self.colors_list = new_colors_list

    def close(self):
        self.refresh_colors_list()
        self.parent_box.colors = self.colors_list
        self.parent_box.fill_colors()
        self.dismiss()


class ColorRepresentation(BoxLayout):

    def __init__(self, **kwargs):
        super(ColorRepresentation, self).__init__(**kwargs)

        self.height = round(WINDOW.height / 12)


class MainScreenApp(App):
    """"Every content-object (mini-application) is in a separate box of Carousel.

    """

    def build(self):
        return MainBoxLayout()


if __name__ == "__main__":
    MainScreenApp().run()
