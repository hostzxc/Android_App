from kivy.uix.label import Label
from kivy.uix.button import Button
from kivy.uix.floatlayout import FloatLayout
from kivy.uix.screenmanager import Screen

class GalleryScreen(Screen):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self.layout = FloatLayout()
        
        # Метка с текстом
        self.label = Label(
            text="Позже здесь будет галерея",
            font_size=14,
            color=(1, 1, 1, 1),
            size_hint=(None, None)
        )
        self.label.size = self.label.texture_size
        self.label.pos_hint = {'center_x': 0.5, 'center_y': 0.6}
        
        # Кнопка "В меню"
        self.back_button = Button(
            text="В меню",
            size_hint=(0.2, 0.2),
            pos_hint={'center_x': 0.5, 'center_y': 0.2}
        )
        self.back_button.bind(on_press=self.go_to_main_menu)

        self.layout.add_widget(self.label)
        self.layout.add_widget(self.back_button)
        self.add_widget(self.layout)

    def go_to_main_menu(self, instance):
        self.manager.current = "main"  # Убедись, что у главного экрана именно такой name

