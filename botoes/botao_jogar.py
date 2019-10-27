  
import arcade
from .botao import Botao
from config import *

class Botao_jogar(Botao):
    def __init__(self,center_x,center_y):
        super().__init__("img/botao/jogar.png",center_x=center_x,center_y=center_y,escala=0.1,acao_botao=PARTIDA)