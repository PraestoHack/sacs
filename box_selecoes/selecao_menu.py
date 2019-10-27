import arcade
from .selecao import Selecao
from config import *

class Selecao_menu(Selecao):
    def __init__(self,center_x,center_y):
        super().__init__("img/selecao/selecao_menu.png",center_x=center_x,center_y=center_y,escala=1)
        self.coluna_atual = COLUNA1

    def on_key_release(self, key, key_modifiers):
        #mover a box
        if key == arcade.key.DOWN:
            self.center_y = Y_SEGUNDA_COLUNA
            self.coluna_atual = COLUNA2
        if key == arcade.key.UP:
            self.center_y = Y_PRIMEIRA_COLUNA
            self.coluna_atual = COLUNA1
        #realizar uma acao
        if key == arcade.key.LEFT and self.coluna_atual == COLUNA1:
            return PARTIDA
        if key == arcade.key.LEFT and self.coluna_atual == COLUNA2:
            return SAIR
        if key == arcade.key.RIGHT:
            return AJUDA

    def on_mouse_scroll(self, x: int, y: int, scroll_x: int, scroll_y: int):
        if scroll_y <= SCROLL_BAIXO:
            self.center_y = Y_SEGUNDA_COLUNA
            self.coluna_atual = COLUNA2

        if scroll_y >= SCROLL_CIMA:
            self.center_y = Y_PRIMEIRA_COLUNA
            self.coluna_atual = COLUNA1

    def on_mouse_release(self, x, y, button, modifiers):
        if button == arcade.MOUSE_BUTTON_LEFT and self.coluna_atual == COLUNA1:
            return PARTIDA
        if button == arcade.MOUSE_BUTTON_LEFT and self.coluna_atual == COLUNA2:
            return SAIR
        if button == arcade.MOUSE_BUTTON_RIGHT:
            return AJUDA