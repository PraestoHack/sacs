  
import arcade
from .botao import Botao
from config import *

class Botao_voltar_ao_menu(Botao):
    def __init__(self,center_x,center_y):
        super().__init__("img/botao/voltar.png",center_x=center_x,center_y=center_y,escala=0.179,acao_botao=MENU)
