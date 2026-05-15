"""
AutoFlow Studio - Android Version
Main Application Entry Point
"""
from kivymd.app import MDApp
from kivymd.uix.screen import MDScreen
from kivymd.uix.button import MDRaisedButton, MDFillRoundFlatButton
from kivymd.uix.label import MDLabel
from kivymd.uix.toolbar import MDTopAppBar
from kivymd.uix.boxlayout import MDBoxLayout
from kivymd.uix.gridlayout import MDGridLayout
from kivy.uix.screenmanager import ScreenManager, Screen
from kivy.core.window import Window
from kivy.metrics import dp

# Set window size for desktop testing
Window.size = (360, 640)


class HomeScreen(MDScreen):
    """Main home screen with 4 step buttons"""
    
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self.name = 'home'
        
        # Main layout
        layout = MDBoxLayout(
            orientation='vertical',
            padding=dp(20),
            spacing=dp(15)
        )
        
        # Top bar
        toolbar = MDTopAppBar(
            title="AutoFlow Studio",
            elevation=2,
            md_bg_color=(0.2, 0.4, 0.8, 1)
        )
        layout.add_widget(toolbar)
        
        # Welcome text
        welcome = MDLabel(
            text="Create Amazing Videos",
            halign="center",
            theme_text_color="Secondary",
            font_style="H6"
        )
        layout.add_widget(welcome)
        
        # Buttons grid
        buttons_layout = MDGridLayout(
            cols=1,
            spacing=dp(15),
            size_hint_y=None,
            height=dp(400)
        )
        
        # Step 1: Text to Speech
        btn1 = MDRaisedButton(
            text="Step 1: Text to Speech",
            size_hint=(1, None),
            height=dp(80),
            md_bg_color=(0.2, 0.6, 0.8, 1),
            on_release=lambda x: self.go_to_screen('tts')
        )
        buttons_layout.add_widget(btn1)
        
        # Step 2: Slideshow
        btn2 = MDRaisedButton(
            text="Step 2: Audio + Image Video",
            size_hint=(1, None),
            height=dp(80),
            md_bg_color=(0.3, 0.7, 0.5, 1),
            on_release=lambda x: self.go_to_screen('slideshow')
        )
        buttons_layout.add_widget(btn2)
        
        # Step 3: Timer
        btn3 = MDRaisedButton(
            text="Step 3: Timer Video",
            size_hint=(1, None),
            height=dp(80),
            md_bg_color=(0.9, 0.6, 0.2, 1),
            on_release=lambda x: self.go_to_screen('timer')
        )
        buttons_layout.add_widget(btn3)
        
        # Step 4: Join
        btn4 = MDRaisedButton(
            text="Step 4: Final Join",
            size_hint=(1, None),
            height=dp(80),
            md_bg_color=(0.8, 0.3, 0.5, 1),
            on_release=lambda x: self.go_to_screen('join')
        )
        buttons_layout.add_widget(btn4)
        
        layout.add_widget(buttons_layout)
        
        # Footer
        footer = MDLabel(
            text="Version 1.0.0 - Big Total Apps",
            halign="center",
            theme_text_color="Hint",
            size_hint_y=None,
            height=dp(30)
        )
        layout.add_widget(footer)
        
        self.add_widget(layout)
    
    def go_to_screen(self, screen_name):
        """Navigate to different screens"""
        self.manager.current = screen_name


class TTSScreen(MDScreen):
    """Text to Speech Screen"""
    
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self.name = 'tts'
        
        layout = MDBoxLayout(orientation='vertical', padding=dp(20), spacing=dp(15))
        
        # Top bar with back button
        toolbar = MDTopAppBar(
            title="Text to Speech",
            left_action_items=[["arrow-left", lambda x: self.go_back()]],
            md_bg_color=(0.2, 0.6, 0.8, 1)
        )
        layout.add_widget(toolbar)
        
        # Content
        content = MDLabel(
            text="Text to Speech Feature\n\nComing Soon...",
            halign="center",
            theme_text_color="Primary"
        )
        layout.add_widget(content)
        
        self.add_widget(layout)
    
    def go_back(self):
        self.manager.current = 'home'


class SlideshowScreen(MDScreen):
    """Slideshow Creation Screen"""
    
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self.name = 'slideshow'
        
        layout = MDBoxLayout(orientation='vertical', padding=dp(20), spacing=dp(15))
        
        toolbar = MDTopAppBar(
            title="Audio + Image Video",
            left_action_items=[["arrow-left", lambda x: self.go_back()]],
            md_bg_color=(0.3, 0.7, 0.5, 1)
        )
        layout.add_widget(toolbar)
        
        content = MDLabel(
            text="Slideshow Creation\n\nComing Soon...",
            halign="center",
            theme_text_color="Primary"
        )
        layout.add_widget(content)
        
        self.add_widget(layout)
    
    def go_back(self):
        self.manager.current = 'home'


class TimerScreen(MDScreen):
    """Timer Video Screen"""
    
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self.name = 'timer'
        
        layout = MDBoxLayout(orientation='vertical', padding=dp(20), spacing=dp(15))
        
        toolbar = MDTopAppBar(
            title="Timer Video",
            left_action_items=[["arrow-left", lambda x: self.go_back()]],
            md_bg_color=(0.9, 0.6, 0.2, 1)
        )
        layout.add_widget(toolbar)
        
        content = MDLabel(
            text="Timer Video Feature\n\nComing Soon...",
            halign="center",
            theme_text_color="Primary"
        )
        layout.add_widget(content)
        
        self.add_widget(layout)
    
    def go_back(self):
        self.manager.current = 'home'


class JoinScreen(MDScreen):
    """Video Join Screen"""
    
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self.name = 'join'
        
        layout = MDBoxLayout(orientation='vertical', padding=dp(20), spacing=dp(15))
        
        toolbar = MDTopAppBar(
            title="Final Join",
            left_action_items=[["arrow-left", lambda x: self.go_back()]],
            md_bg_color=(0.8, 0.3, 0.5, 1)
        )
        layout.add_widget(toolbar)
        
        content = MDLabel(
            text="Video Join Feature\n\nComing Soon...",
            halign="center",
            theme_text_color="Primary"
        )
        layout.add_widget(content)
        
        self.add_widget(layout)
    
    def go_back(self):
        self.manager.current = 'home'


class AutoFlowStudioApp(MDApp):
    """Main Application Class"""
    
    def build(self):
        self.theme_cls.primary_palette = "Blue"
        self.theme_cls.theme_style = "Light"
        
        # Screen manager
        sm = ScreenManager()
        sm.add_widget(HomeScreen())
        sm.add_widget(TTSScreen())
        sm.add_widget(SlideshowScreen())
        sm.add_widget(TimerScreen())
        sm.add_widget(JoinScreen())
        
        return sm


if __name__ == '__main__':
    AutoFlowStudioApp().run()
