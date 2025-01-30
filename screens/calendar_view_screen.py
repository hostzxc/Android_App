from kivy.uix.screenmanager import Screen
from kivy.uix.button import Button
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.gridlayout import GridLayout
from kivy.uix.label import Label
from datetime import datetime, timedelta
import calendar

class CalendarViewScreen(Screen):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self.current_date = datetime.today() 
        self.update_calendar()

        #Кнопка "Назад"
        self.back_button = Button(
            text="Назад",
            size_hint=(0.2, 0.1),
            pos_hint={"right": 1, "top": 1},
            font_size="14sp"  #Установка размера шрифта для кнопки
        )
        self.back_button.bind(on_press=self.go_back)

        self.add_widget(self.back_button)

    def update_calendar(self):
        #Удаляем старый календарь, если он существует
        if hasattr(self, 'calendar_layout'):
            self.remove_widget(self.calendar_layout)

        #Создаем новый календарь
        self.calendar_layout = BoxLayout(orientation="vertical", size_hint=(1, 1))

        #Панель управления месяцем
        month_control = BoxLayout(size_hint=(1, 0.2))
        prev_button = Button(text="Prev", size_hint=(0.3, 0.2), font_size="14sp")  # Установка размера шрифта
        next_button = Button(text="Next", size_hint=(0.3, 0.2), font_size="14sp")  # Установка размера шрифта
        month_label = Label(
            text=self.current_date.strftime("%B %Y"),
            size_hint=(0.6, 1),
            font_size="16sp"  # Установка размера шрифта
        )
        prev_button.bind(on_press=self.prev_month)
        next_button.bind(on_press=self.next_month)
        month_control.add_widget(prev_button)
        month_control.add_widget(month_label)
        month_control.add_widget(next_button)

        #Сетка календаря
        calendar_grid = GridLayout(cols=7, size_hint=(1, None), height=250)
        #Заголовки дней недели
        days = ["Пн", "Вт", "Ср", "Чт", "Пт", "Сб", "Вс"]
        for day in days:
            calendar_grid.add_widget(Label(text=day, bold=True, font_size="14sp"))  # Установка размера шрифта

        # Заполнение календаря
        year, month = self.current_date.year, self.current_date.month
        month_days = calendar.monthcalendar(year, month)

        for week in month_days:
            for day in week:
                if day == 0:
                    calendar_grid.add_widget(Label(text="")) 
                else:
                    day_text = str(day)
                    lbl = Label(text=day_text, size_hint=(1, None), height=40, font_size="14sp")  # Установка размера шрифта

                    # Подсветка текущего дня
                    if day == datetime.today().day and month == datetime.today().month and year == datetime.today().year:
                        lbl.color = (1, 0, 0, 1)  # Красный цвет для текущего дня

                    calendar_grid.add_widget(lbl)

        # Добавляем панель управления и сетку календаря в основной layout
        self.calendar_layout.add_widget(month_control)
        self.calendar_layout.add_widget(calendar_grid)

        # Добавляем календарь на экран
        self.add_widget(self.calendar_layout)

    def prev_month(self, instance):
        # Переход к предыдущему месяцу
        self.current_date = self.current_date.replace(day=1) - timedelta(days=1)
        self.current_date = self.current_date.replace(day=1) 
        self.update_calendar()

    def next_month(self, instance):
        # Переход к следующему месяцу
        next_month = self.current_date.replace(day=28) + timedelta(days=4) 
        self.current_date = next_month.replace(day=1)
        self.update_calendar()

    def go_back(self, instance):
        # Возврат на предыдущий экран
        self.manager.current = 'calendar'