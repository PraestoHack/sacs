import arcade

class Selecao(arcade.Sprite):
    def __init__(self,img,center_x,center_y,scale=1):
        super.__init__(img,scale,center_x=center_x,center_y=center_y)
    
    def draw(self):
        self.draw()

    def update(self, delta_time):
        pass

    def on_key_press(self, key, key_modifiers):
        pass

    def on_key_release(self, key, key_modifiers):
        pass

    def on_mouse_motion(self, x, y, delta_x, delta_y):
        pass

    def on_mouse_press(self, x, y, button, key_modifiers):
        pass

    def on_mouse_release(self, x, y, button, key_modifiers):
        pass