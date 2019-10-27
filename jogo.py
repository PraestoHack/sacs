import arcade
from telas.menu import Menu

LARGURA_TELA = 800
ALTURA_TELA = 600
TITULO_TELA = "SACS - SOFTWARE DE ACESSIBILIDADE PARA CEGOS E SURDOS"

#estados do jogo
SAIR = -1
MENU = 0
PARTIDA = 1
AJUDA = 2

class MyGame(arcade.Window):

    def __init__(self, largura, altura, titulo):
        super().__init__(largura,altura,titulo)
        self.estado_atual = MENU
        self.menu = Menu(LARGURA_TELA,ALTURA_TELA)
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
            pass
        elif self.estado_atual == SAIR:
            self.close()

    def on_update(self, delta_time):
        pass

    def on_key_press(self, key, key_modifiers):
        pass

    def on_key_release(self, key, key_modifiers):
        self.menu.on_key_release(key,key_modifiers)


def main():
    game = MyGame(LARGURA_TELA, ALTURA_TELA, TITULO_TELA)
    game.setup()
    arcade.run()


if __name__ == "__main__":
    main()