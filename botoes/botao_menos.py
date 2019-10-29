  
import arcade
from .botao import Botao
from config import *

class Botao_menos(Botao):
    def __init__(self,center_x,center_y):
        super().__init__("img/botao/menos.png",center_x=center_x,center_y=center_y,escala=0.027,acao_botao=SUBTRAIR)