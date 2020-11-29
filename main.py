from remi.gui import *
from remi import start, App
from logic import search_by_words


class Window(App):
    def __init__(self, *args):
        super(Window, self).__init__(*args)

    def main(self):
        self.type = 0
        container_top = Container(width='100%', height=800, margin='0px', style={'display': 'block', 'overflow': 'auto', 'text-align': 'center'})
        container_top.css_background_color = "rgb(0,188,212)"

        container_bottom = Container(width='100%', height='50px', layout_orientation=Container.LAYOUT_HORIZONTAL, margin='0px', style={'display': 'block'})
        container_bottom.css_background_color = "rgb(180,188,212)"

        container0 = Container(width=480, margin='0px auto', style={'display': 'block', 'overflow': 'hidden'})

        self.btn = Button('查找', width=90, height=40, margin='5px')
        self.btn.onclick.do(self.on_button_pressed)

        self.input_0 = Input('', width=360, height=35, margin='5px')
        self.input_0.css_font_size = "200%"
        container_bottom.append([self.input_0, self.btn])

        self.dropDown = DropDown.new_from_list(('选择', '名解', '问答', '病例分析'), width=460, height=30, margin='10px')
        self.dropDown.onchange.do(self.drop_down_changed)
        self.dropDown.select_by_value('选择')

        self.txt_show = TextInput('', width=460, height=730, margin='10px')
        self.txt_show.attr_maxlength = "0"
        self.txt_show.css_font_size = '130%'
        container_top.append([self.dropDown, self.txt_show])

        container0.append([container_bottom, container_top])

        return container0


    def on_button_pressed(self, emitter):
        t = self.input_0.get_value()
        result = search_by_words(self.type, t.split(' '))
        self.txt_show.set_text(result)


    def drop_down_changed(self, wigdet, value):
        q_list = ['选择', '名解', '问答', '病例分析']
        self.type = q_list.index(value)

    
# start(Window, debug=True)
start(Window, debug=False, address='0.0.0.0', port=8082)