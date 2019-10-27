import arcade
from telas.menu import Menu
from telas.partida import Partida
from config import *
'''
LARGURA_TELA = 800
ALTURA_TELA = 600
TITULO_TELA = "SACS - SOFTWARE DE ACESSIBILIDADE PARA CEGOS E SURDOS"

#estados do jogo
SAIR = -1
MENU = 0
PARTIDA = 1
AJUDA = 2
'''
class MyGame(arcade.Window):

    def __init__(self, largura, altura, titulo):
        super().__init__(largura,altura,titulo)
        self.estado_atual = MENU
        self.menu = Menu(LARGURA_TELA,ALTURA_TELA)
        self.partida = Partida(LARGURA_TELA,ALTURA_TELA)
        arcade.set_background_color(arcade.color.AMAZON)


    def setup(self):
        pass

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
        pass

    def on_key_press(self, key, key_modifiers):
        pass

    def on_key_release(self, key, key_modifiers):
        if self.estado_atual == MENU:
            acao = self.menu.on_key_release(key,key_modifiers)
            if acao is not None:
                self.estado_atual = acao
        if self.estado_atual == PARTIDA:
            acao = self.partida.on_key_release(key,key_modifiers)
            if acao is not None:
                acao = self.partida.on_mouse_release(x,y,button,modifiers)

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
        if self.estado_atual == PARTIDA:
            acao = self.partida.on_mouse_release(x,y,button,modifiers)
            if acao is not None:
                acao = self.partida.on_mouse_release(x,y,button,modifiers)

def main():
    game = MyGame(LARGURA_TELA, ALTURA_TELA, TITULO_TELA)
    game.setup()
    arcade.run()


if __name__ == "__main__":
    main()