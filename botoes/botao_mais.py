  
import arcade
from .botao import Botao
from config import *

class Botao_mais(Botao):
    def __init__(self,center_x,center_y):
        super().__init__("img/botao/mais.png",center_x=center_x,center_y=center_y,escala=0.1,acao_botao=SOMAR)