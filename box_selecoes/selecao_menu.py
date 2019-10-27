import arcade
from .selecao import Selecao

#475 165
LARGURA_IMG = 475
ALTURA_IMG = 165
Y_PRIMEIRA_COLUNA = 430
Y_SEGUNDA_COLUNA = 200

class Selecao_menu(Selecao):
    def __init__(self,center_x,center_y):
        super().__init__("img/selecao/selecao_menu.png",center_x=center_x,center_y=center_y,escala=1)
    
    def on_key_release(self, key, key_modifiers):
        if key == arcade.key.DOWN:
            self.center_y = Y_SEGUNDA_COLUNA

        
        if key == arcade.key.UP:
            self.center_y = Y_PRIMEIRA_COLUNA
