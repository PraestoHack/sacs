import arcade
from .selecao import Selecao
from config import *

class Selecao_partida(Selecao):
    def __init__(self,center_x,center_y):
        super().__init__("img/selecao/selecao_partida_col_1.png",center_x=center_x,center_y=center_y,escala=1)
        self.coluna_atual = COLUNA1

    def on_key_release(self, key, key_modifiers):
        #mover a box
        if key == arcade.key.DOWN and self.coluna_atual == COLUNA1:
            self.coluna_atual = COLUNA2
        elif key == arcade.key.DOWN and self.coluna_atual == COLUNA2:
            self.coluna_atual = COLUNA3
        elif key == arcade.key.DOWN and self.coluna_atual == COLUNA3:
            self.coluna_atual = COLUNA4
        elif key == arcade.key.UP and self.coluna_atual == COLUNA4:
            self.coluna_atual = COLUNA3
        elif key == arcade.key.UP and self.coluna_atual == COLUNA3:
            self.coluna_atual = COLUNA2
        elif key == arcade.key.UP and self.coluna_atual == COLUNA2:
            self.coluna_atual = COLUNA1
        print(self.coluna_atual)
    
        #realizar uma acao
        if key == arcade.key.LEFT and self.coluna_atual == COLUNA1:
            return MENU
        
        elif key == arcade.key.LEFT and self.coluna_atual == COLUNA2:
            return SOMAR
        elif key == arcade.key.LEFT and self.coluna_atual == COLUNA3:
            return SUBTRAIR
        elif key == arcade.key.LEFT and self.coluna_atual == COLUNA4:
            return VERIFICAR_RESULTADO

        elif key == arcade.key.RIGHT and self.coluna_atual == COLUNA1:
            #COLOCAR AUDIO
            #return AJUDA
            pass
        elif key == arcade.key.RIGHT and self.coluna_atual == COLUNA2:
            #COLOCAR AUDIO
            #return AJUDA
            pass
        elif key == arcade.key.RIGHT and self.coluna_atual == COLUNA2:
            #COLOCAR AUDIO
            #return AJUDA
            pass
        elif key == arcade.key.RIGHT and self.coluna_atual == COLUNA2:
            #COLOCAR AUDIO
            #return AJUDA
            pass
         

    def on_mouse_scroll(self, x: int, y: int, scroll_x: int, scroll_y: int):
        if scroll_y <= SCROLL_BAIXO and self.coluna_atual == COLUNA1:
            self.coluna_atual = COLUNA2
        elif scroll_y <= SCROLL_BAIXO and self.coluna_atual == COLUNA2:
            self.coluna_atual = COLUNA3
        elif scroll_y <= SCROLL_BAIXO and self.coluna_atual == COLUNA3:
            self.coluna_atual = COLUNA4
        elif scroll_y >= SCROLL_CIMA and self.coluna_atual == COLUNA4:
            self.coluna_atual = COLUNA3
        elif scroll_y >= SCROLL_CIMA and self.coluna_atual == COLUNA3:
            self.coluna_atual = COLUNA2
        elif scroll_y >= SCROLL_CIMA and self.coluna_atual == COLUNA2:
            self.coluna_atual = COLUNA1
        print(self.coluna_atual)

    def on_mouse_release(self, x, y, button, modifiers):
        if button == arcade.MOUSE_BUTTON_LEFT and self.coluna_atual == COLUNA1:
            return MENU
        elif button == arcade.MOUSE_BUTTON_LEFT and self.coluna_atual == COLUNA2:
            return SOMAR
        elif button == arcade.MOUSE_BUTTON_LEFT and self.coluna_atual == COLUNA3:
            return SUBTRAIR
        elif button == arcade.MOUSE_BUTTON_RIGHT and self.coluna_atual == COLUNA1:
            #som
            pass
        elif button == arcade.MOUSE_BUTTON_RIGHT and self.coluna_atual == COLUNA2:
            #som
            pass
        elif button == arcade.MOUSE_BUTTON_RIGHT and self.coluna_atual == COLUNA3:
            #som
            pass
        elif button == arcade.MOUSE_BUTTON_LEFT and self.coluna_atual == coluna4:
            return VERIFICAR_RESULTADO
