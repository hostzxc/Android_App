from kivy.uix.screenmanager import Screen
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.button import Button
from kivy.uix.label import Label
from kivy.clock import Clock
from datetime import datetime
from kivy.uix.gridlayout import GridLayout
import calendar

class CalendarScreen(Screen):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self.current_date = datetime.today()

        self.back_button = Button(
            text="Назад",
            size_hint=(0.2, 0.1),
            pos_hint={"right": 1, "top": 1}
        )
        self.back_button.bind(on_press=self.go_back)


        self.time_label = Label(
            text="00:00:00",
            font_size="50sp",
            size_hint=(0.8, 0.2),
            pos_hint={"center_x": 0.5, "center_y": 0.7}
        )

        self.date_button = Button(
            text=self.current_date.strftime("%d.%m.%Y"),
            font_size="25sp",
            size_hint=(0.6, 0.1),
            pos_hint={"center_x": 0.5, "center_y": 0.6}
        )
        self.date_button.bind(on_press=self.open_calendar_view)

        self.button_layout = BoxLayout(
            orientation='horizontal',
            spacing=20,
            size_hint=(0.8, 0.1),
            pos_hint={"center_x": 0.5, "center_y": 0.3}
        )

        self.stopwatch_button = Button(text="Секундомер", size_hint=(0.5, 1)) #было свойство height
        self.stopwatch_button.bind(on_press=lambda x: setattr(self.manager, "current", "stopwatch"))


        self.timer_button = Button(text="Таймер", size_hint=(0.5, 1)) #было свойство height
        self.timer_button.bind(on_press=lambda x: setattr(self.manager, "current", "timer"))

        self.button_layout.add_widget(self.stopwatch_button)
        self.button_layout.add_widget(self.timer_button)

        self.add_widget(self.back_button)
        self.add_widget(self.time_label)
        self.add_widget(self.date_button)
        self.add_widget(self.button_layout)

        Clock.schedule_interval(self.update_time, 1)

    def update_time(self, dt):
        """Обновляет текущее время"""
        now = datetime.now()
        self.time_label.text = now.strftime("%H:%M:%S")

    def open_calendar_view(self, instance):
        """Открывает экран с календарем"""
        self.manager.current = 'calendar_view'

    def go_back(self, instance):
        """Возвращает на экран 'main'"""
        self.manager.current = 'main' 
