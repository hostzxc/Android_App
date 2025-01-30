from kivy.uix.label import Label
from kivy.uix.screenmanager import Screen
from kivy.uix.button import Button
from kivy.uix.boxlayout import BoxLayout
from kivy.clock import Clock

class StopwatchScreen(Screen):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self.time = 0
        self.running = False 

        self.back_button = Button(
            text="← Назад",
            size_hint=(None, None),
            size=(100, 50),
            pos_hint={"right": 1, "top": 1}
        )
        self.back_button.bind(on_press=self.go_back)


        self.time_label = Label(
            text="00:00:00.000",
            font_size="50sp",
            size_hint=(0.8, None),
            height=100,
            pos_hint={"center_x": 0.5, "center_y": 0.6}
        )

        self.button_layout = BoxLayout(
            orientation='horizontal',
            spacing=20,
            size_hint=(0.6, None),
            height=50,
            pos_hint={"center_x": 0.5, "center_y": 0.4}
        )


        self.start_stop_button = Button(text="Старт", size_hint=(0.5, None), height=50)
        self.start_stop_button.bind(on_press=self.start_stop)

        self.reset_button = Button(text="Сброс", size_hint=(0.5, None), height=50)
        self.reset_button.bind(on_press=self.reset)

        self.button_layout.add_widget(self.start_stop_button)
        self.button_layout.add_widget(self.reset_button)

        self.add_widget(self.back_button)
        self.add_widget(self.time_label)
        self.add_widget(self.button_layout)

        Clock.schedule_interval(self.update_time, 0.01)

    def update_time(self, dt):
        if self.running:
            self.time += int(dt * 1000)
            hours = self.time // 3600000
            minutes = (self.time % 3600000) // 60000
            seconds = (self.time % 60000) // 1000
            milliseconds = self.time % 1000
            self.time_label.text = f"{hours:02}:{minutes:02}:{seconds:02}.{milliseconds:03}"

    def start_stop(self, instance):
        self.running = not self.running
        self.start_stop_button.text = "Стоп" if self.running else "Старт"

    def reset(self, instance):
        self.running = False
        self.time = 0
        self.time_label.text = "00:00:00.000"
        self.start_stop_button.text = "Старт"

    def go_back(self, instance):
        self.manager.current = 'calendar'
