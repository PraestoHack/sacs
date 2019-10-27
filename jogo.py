import arcade
from telas.menu import Menu
from telas.partida import Partida
import pyttsx3
from config import *

class MyGame(arcade.Window):

    def __init__(self, largura, altura, titulo):
        super().__init__(largura,altura,titulo)
        self.estado_atual = MENU
        self.menu = Menu(LARGURA_TELA,ALTURA_TELA)
        self.partida = Partida(LARGURA_TELA,ALTURA_TELA)
        arcade.set_background_color(arcade.color.AMAZON)

    def setup(self):
        if self.estado_atual == MENU:
            self.menu.setup()
        elif self.estado_atual == PARTIDA:
            self.partida.setup()
            
    def on_draw(self):
        arcade.start_render()
        if self.estado_atual == MENU:
            self.menu.draw()
        elif self.estado_atual == AJUDA:
            pass
        elif self.estado_atual == PARTIDA:
            self.partida.draw()
        elif self.estado_atual == SAIR:
            self.close()

    def on_update(self, delta_time):
        if self.estado_atual == PARTIDA:
            self.partida.update(delta_time)

    def on_key_press(self, key, key_modifiers):
        pass

    
                

    def on_mouse_scroll(self, x: int, y: int, scroll_x: int, scroll_y: int):
        if self.estado_atual == MENU:
            self.menu.on_mouse_scroll(x,y,scroll_x,scroll_y)
        if self.estado_atual == PARTIDA:
            self.partida.on_mouse_scroll(x,y,scroll_x,scroll_y)

    def on_mouse_release(self, x, y, button, modifiers):
        if self.estado_atual == MENU:
            acao = self.menu.on_mouse_release(x,y,button,modifiers)
            if acao is not None:
                self.estado_atual = acao
                if self.estado_atual != MENU:
                    self.menu.kill()

        if self.estado_atual == PARTIDA:
            acao = self.partida.on_mouse_release(x,y,button,modifiers)
            if acao is not None:
                self.estado_atual = acao
                if self.estado_atual != PARTIDA:
                    self.partida.setup()
                    self.partida.kill()

    def on_key_release(self, key, key_modifiers):
        if self.estado_atual == MENU:
            acao = self.menu.on_key_release(key,key_modifiers)
            if acao is not None:
                self.estado_atual = acao
                if self.estado_atual != MENU:
                    self.menu.kill()
        if self.estado_atual == PARTIDA:
            acao = self.partida.on_key_release(key,key_modifiers)
            if acao is not None:
                self.estado_atual = acao
                if self.estado_atual != PARTIDA:
                    self.partida.setup()
                    self.partida.kill()

def main():
    game = MyGame(LARGURA_TELA, ALTURA_TELA, TITULO_TELA)
    game.setup()
    arcade.run()

#HKEY_LOCAL_MACHINE\SOFTWARE\Microsoft\Speech\Voices\Tokens\TTS_MS_PT-BR_MARIA_11.0

if __name__ == "__main__":
    main()