import arcade
from .selecao import Selecao
from config import *

class Selecao_partida(Selecao):
    def __init__(self,center_x,center_y):
        super().__init__("img/selecao/selecao_partida_col_1.png",center_x=center_x,center_y=center_y,escala=1)
        self.coluna_atual = COLUNA1
        self.som_selecionar = arcade.load_sound('sons/selecionar.wav')
        self.descr_prob = arcade.load_sound('sons/descr_problema.wav')
        self.som_p1 = arcade.load_sound('sons/partida1.wav')
        self.som_p2 = arcade.load_sound('sons/partida2.wav')
        self.som_p3 = arcade.load_sound('sons/partida3.wav')
        self.som_p4 = arcade.load_sound('sons/partida4.wav')
        self.vez1 = True
    
    def on_key_release(self, key, key_modifiers):
        #mover a box
        #para baixo
        if key == arcade.key.DOWN and self.coluna_atual == COLUNA1:
            self.coluna_atual = COLUNA2
            arcade.play_sound(self.som_selecionar)
            arcade.play_sound(self.som_p2)
        elif key == arcade.key.DOWN and self.coluna_atual == COLUNA2:
            self.coluna_atual = COLUNA3
            arcade.play_sound(self.som_selecionar)
            arcade.play_sound(self.som_p3)
        elif key == arcade.key.DOWN and self.coluna_atual == COLUNA3:
            self.coluna_atual = COLUNA4
            arcade.play_sound(self.som_selecionar)
            arcade.play_sound(self.som_p4)

        #para cima
        elif key == arcade.key.UP and self.coluna_atual == COLUNA4:
            self.coluna_atual = COLUNA3
            arcade.play_sound(self.som_selecionar)
            arcade.play_sound(self.som_p3)
        elif key == arcade.key.UP and self.coluna_atual == COLUNA3:
            self.coluna_atual = COLUNA2
            arcade.play_sound(self.som_selecionar)
            arcade.play_sound(self.som_p2)
        elif key == arcade.key.UP and self.coluna_atual == COLUNA2:
            self.coluna_atual = COLUNA1
            arcade.play_sound(self.som_selecionar)
            arcade.play_sound(self.som_p1)
    
        #realizar uma acao
        if key == arcade.key.LEFT and self.coluna_atual == COLUNA1:
            return MENU
        
        elif key == arcade.key.LEFT and self.coluna_atual == COLUNA2:
            return SOMAR
        elif key == arcade.key.LEFT and self.coluna_atual == COLUNA3:
            return SUBTRAIR
        elif key == arcade.key.LEFT and self.coluna_atual == COLUNA4:
            return VERIFICAR_RESULTADO

        elif key == arcade.key.RIGHT:
            arcade.play_sound(self.descr_prob)
         

    def on_mouse_scroll(self, x: int, y: int, scroll_x: int, scroll_y: int):
        #mover pra baixo
        if scroll_y <= SCROLL_BAIXO and self.coluna_atual == COLUNA1:
            self.coluna_atual = COLUNA2
            arcade.play_sound(self.som_selecionar)
            arcade.play_sound(self.som_p2)
        elif scroll_y <= SCROLL_BAIXO and self.coluna_atual == COLUNA2:
            self.coluna_atual = COLUNA3
            arcade.play_sound(self.som_selecionar)
            arcade.play_sound(self.som_p3)
        elif scroll_y <= SCROLL_BAIXO and self.coluna_atual == COLUNA3:
            self.coluna_atual = COLUNA4
            arcade.play_sound(self.som_selecionar)
            arcade.play_sound(self.som_p4)
        #mover pra cima
        elif scroll_y >= SCROLL_CIMA and self.coluna_atual == COLUNA4:
            self.coluna_atual = COLUNA3
            arcade.play_sound(self.som_selecionar)
            arcade.play_sound(self.som_p3)
        elif scroll_y >= SCROLL_CIMA and self.coluna_atual == COLUNA3:
            self.coluna_atual = COLUNA2
            arcade.play_sound(self.som_selecionar)
            arcade.play_sound(self.som_p2)
        elif scroll_y >= SCROLL_CIMA and self.coluna_atual == COLUNA2:
            self.coluna_atual = COLUNA1
            arcade.play_sound(self.som_selecionar)
            arcade.play_sound(self.som_p1)

    def on_mouse_release(self, x, y, button, modifiers):
        if self.vez1:
            button = arcade.MOUSE_BUTTON_RIGHT
            self.vez1 = False
        if button == arcade.MOUSE_BUTTON_LEFT and self.coluna_atual == COLUNA1:
            return MENU
        elif button == arcade.MOUSE_BUTTON_LEFT and self.coluna_atual == COLUNA2:
            return SOMAR
        elif button == arcade.MOUSE_BUTTON_LEFT and self.coluna_atual == COLUNA3:
            return SUBTRAIR
        elif button == arcade.MOUSE_BUTTON_RIGHT:
            arcade.play_sound(self.descr_prob)
        