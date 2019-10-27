  
import arcade
from .botao import Botao

class Botao_ajuda(Botao):
    def __init__(self,center_x,center_y):
        super().__init__("img/botao/ajuda.png",center_x=center_x,center_y=center_y,escala=0.2,acao_botao=2)
