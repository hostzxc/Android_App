from kivy.app import App
from kivy.uix.screenmanager import ScreenManager
from screens.main_screen import MainScreen
from screens.calendar_screen import CalendarScreen
from screens.stopwatch_screen import StopwatchScreen
from screens.timer_screen import TimerScreen  
from screens.calendar_view_screen import CalendarViewScreen
from screens.daily_screen import DailyScreen
from screens.statistics_screen import StatisticsScreen
from screens.workout_screen import WorkoutScreen
from screens.gallery_screen import GalleryScreen

class MyApp(App):
    
    def build(self):
        sm = ScreenManager()
        sm.add_widget(MainScreen(name="main"))
        sm.add_widget(CalendarScreen(name="calendar"))
        sm.add_widget(StopwatchScreen(name="stopwatch"))
        sm.add_widget(DailyScreen(name='daily'))
        sm.add_widget(CalendarViewScreen(name='calendar_view'))
        sm.add_widget(TimerScreen(name="timer"))
        sm.add_widget(StatisticsScreen(name="statistics"))
        sm.add_widget(WorkoutScreen(name='workout'))
        sm.add_widget(GalleryScreen(name='gallery'))
        
        return sm

    def on_stop(self):
        daily_screen = self.root.get_screen('daily')
        daily_screen.save_checkboxes_state()
        
if __name__ == "__main__":
    MyApp().run()
