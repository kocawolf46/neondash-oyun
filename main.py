from kivy.app import App
from kivy.uix.widget import Widget
from kivy.properties import NumericProperty, ObjectProperty, BooleanProperty
from kivy.clock import Clock
from kivy.lang import Builder
import random
# YENİ: Ses dosyalarını oynatmak için gerekli kütüphaneyi çağırıyoruz
from kivy.core.audio import SoundLoader 

Builder.load_string('''
<PlayerWidget>:
    size: 50, 50
    canvas:
        Rectangle:
            pos: self.pos
            size: self.size
            source: 'player.png'

<ObstacleWidget>:
    size_hint: None, None
    width: 50
    canvas:
        Rectangle:
            pos: self.pos
            size: self.size
            source: 'obstacle.png'

<GameScreen>:
    player: player_id
    obstacle: obstacle_id
    
    canvas.before:
        Rectangle:
            pos: root.bg_x1, 0
            size: self.size
            source: 'bg.png'
        Rectangle:
            pos: root.bg_x2, 0
            size: self.size
            source: 'bg.png'
    
    Label:
        text: str(root.score)
        font_size: 60
        center_x: root.width / 2
        top: root.top - 20
        color: 1, 1, 1, 1
        opacity: 1 if not root.game_over else 0

    PlayerWidget:
        id: player_id
        x: root.width / 4       
        y: root.center_y        

    ObstacleWidget:
        id: obstacle_id
        x: root.width           
        y: 0
        height: 150
        
    BoxLayout:
        orientation: 'vertical'
        center: root.center
        size_hint: None, None
        size: 300, 200
        opacity: 1 if root.game_over else 0
        disabled: not root.game_over
        
        Label:
            text: "NEON DASH" if root.score == 0 else "OYUN BITTI!"
            font_size: 50
            color: 0, 1, 1, 1 if root.score == 0 else (1, 0.2, 0.2, 1)
            
        Label:
            text: "Skor: " + str(root.score)
            font_size: 30
            opacity: 1 if root.score > 0 else 0
            
        Button:
            text: "BASLA / TEKRAR OYNA"
            font_size: 25
            background_color: 0, 0.8, 0.8, 1
            on_release: root.start_game()
''')

class PlayerWidget(Widget):
    velocity_y = NumericProperty(0)
    
    def move(self):
        gravity = -0.5
        self.velocity_y += gravity
        self.y += self.velocity_y
        
        if self.y < 0:
            self.y = 0
            self.velocity_y = 0

    def jump(self):
        self.velocity_y = 10

class ObstacleWidget(Widget):
    velocity_x = NumericProperty(-7)

class GameScreen(Widget):
    player = ObjectProperty(None)
    obstacle = ObjectProperty(None)
    score = NumericProperty(0)
    bg_x1 = NumericProperty(0)
    bg_x2 = NumericProperty(0)
    game_over = BooleanProperty(True)

    def __init__(self, **kwargs):
        super(GameScreen, self).__init__(**kwargs)
        Clock.schedule_interval(self.update, 1.0 / 60.0)
        
        # YENİ: Sesleri oyun başlarken hafızaya yüklüyoruz (Gecikmeyi önlemek için)
        self.sound_jump = SoundLoader.load('jump.wav')
        self.sound_crash = SoundLoader.load('crash.wav')

    def on_size(self, *args):
        self.bg_x1 = 0
        self.bg_x2 = self.width

    def update(self, dt):
        if self.game_over:
            return

        self.player.move()
        self.obstacle.x += self.obstacle.velocity_x
        
        self.bg_x1 -= 2
        self.bg_x2 -= 2
        
        if self.bg_x1 <= -self.width:
            self.bg_x1 = self.bg_x2 + self.width
        if self.bg_x2 <= -self.width:
            self.bg_x2 = self.bg_x1 + self.width

        if self.obstacle.right < 0:
            self.obstacle.x = self.width  
            self.score += 1               
            
            min_yukseklik = self.height * 0.1
            max_yukseklik = self.height * 0.6
            self.obstacle.height = random.uniform(min_yukseklik, max_yukseklik)
            
            if self.score % 5 == 0: 
                self.obstacle.velocity_x -= 1
        
        if self.player.collide_widget(self.obstacle):
            # YENİ: Çarpışma anında çarpma sesini çal
            if self.sound_crash:
                self.sound_crash.play()
            self.game_over = True

    def start_game(self):
        self.player.y = self.center_y
        self.player.velocity_y = 0
        self.obstacle.x = self.width
        self.obstacle.velocity_x = -7
        self.obstacle.height = 150
        self.score = 0
        self.game_over = False

    def on_touch_down(self, touch):
        if not self.game_over:
            self.player.jump()
            # YENİ: Ekrana her dokunulduğunda zıplama sesini çal
            if self.sound_jump:
                self.sound_jump.play()
        
        return super(GameScreen, self).on_touch_down(touch)

class NeonDashApp(App):
    def build(self):
        return GameScreen()

if __name__ == '__main__':
    NeonDashApp().run()