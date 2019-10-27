  
import arcade
from .botao import Botao
from config import *

class Botao_manual(Botao):
    def __init__(self,center_x,center_y):
        super().__init__("img/botao/livro.png",center_x=center_x,center_y=center_y,escala=0.4,acao_botao=AJUDA)
