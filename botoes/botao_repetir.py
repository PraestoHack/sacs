  
import arcade
from .botao import Botao
from config import *

class Botao_repetir(Botao):
    def __init__(self,center_x,center_y):
        super().__init__("img/botao/repetir.png",center_x=center_x,center_y=center_y,escala=0.2,acao_botao=AJUDA)
