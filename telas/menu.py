import arcade
from botoes.botao_jogar import Botao_jogar
from botoes.botao_ajuda import Botao_ajuda
from botoes.botao_sair import Botao_sair
from box_selecoes.selecao_menu import Selecao_menu
from config import *

#fundo = arcade.Sprite("img/telas/menu.png",center_x=self.center_x,center_y=self.center_y,scale=1)
#fundo.draw()
#logo
#logo = arcade.Sprite("img/textos/logo.png",center_x=self.center_x,center_y=self.center_y + 150,scale=1)
#logo.draw()

class Menu():

    def __init__(self,largura_tela,altura_tela):
        self.largura_tela = largura_tela
        self.altura_tela = altura_tela
        self.center_x = largura_tela/2
        self.center_y = altura_tela/2
        self.selecao = Selecao_menu(self.center_x,self.center_y+130)

        #criar botoes e jogar numa lista de botoes
        jogar = Botao_jogar(self.center_x-100,self.center_y+130)
        ajuda = Botao_ajuda(self.center_x+100,self.center_y+130)
        ajuda2 = Botao_ajuda(self.center_x+100,self.center_y-100)
        sair = Botao_sair(self.center_x-100,self.center_y-100)
        self.lista_botoes = [jogar,ajuda,ajuda2,sair]
        
    def draw(self):
        #fundo
        arcade.draw_rectangle_filled(self.center_x,self.center_y,self.largura_tela, self.altura_tela,(20, 73, 107))
        

        #retangulo
        arcade.draw_rectangle_filled(self.center_x,self.center_y,self.largura_tela, self.altura_tela - 100,(19,106,159,240))

        arcade.draw_rectangle_filled(self.center_x,self.altura_tela-50,self.largura_tela,2,(31,35,58))
        arcade.draw_rectangle_filled(self.center_x,0+50,self.largura_tela,2,(31,35,58))
        arcade.draw_text(DESCRICAO_MENU,10,560,arcade.color.WHITE,14,font_name='arial')
        arcade.draw_text(TEXTO_JOGAR,self.center_x-117,self.center_y+60,arcade.color.WHITE,14)
        arcade.draw_text(TEXTO_AJUDA,self.center_x+77,self.center_y+60,arcade.color.WHITE,14)
        arcade.draw_text(TEXTO_AJUDA,self.center_x+77,self.center_y-170,arcade.color.WHITE,14)
        arcade.draw_text(TEXTO_SAIR,self.center_x-115,self.center_y-170,arcade.color.WHITE,14)
        self.selecao.draw()
        
        #botoes
        for botao in self.lista_botoes:
            botao.draw()

    def on_key_release(self, key, key_modifiers):
        acao = self.selecao.on_key_release(key,key_modifiers)
        return acao 

    def on_mouse_scroll(self, x: int, y: int, scroll_x: int, scroll_y: int):
        self.selecao.on_mouse_scroll(x,y,scroll_x,scroll_y)

    def on_mouse_release(self, x, y, button, modifiers):
        acao = self.selecao.on_mouse_release(x,y,button,modifiers)
        return acao