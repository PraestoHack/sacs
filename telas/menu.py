import arcade
from botoes.botao_jogar import Botao_jogar
from botoes.botao_ajuda import Botao_ajuda
from botoes.botao_sair import Botao_sair
from box_selecoes.selecao_menu import Selecao_menu

LARGURA_SEL= 475
ALTURA_SEL = 165

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
        
        #fundo = arcade.Sprite("img/telas/menu.png",center_x=self.center_x,center_y=self.center_y,scale=1)
        #fundo.draw()

        #retangulo
        arcade.draw_rectangle_filled(self.center_x,self.center_y,self.largura_tela, self.altura_tela - 100,(19,106,159,240))

        arcade.draw_rectangle_filled(self.center_x,self.altura_tela-50,self.largura_tela,2,(31,35,58))
        arcade.draw_rectangle_filled(self.center_x,0+50,self.largura_tela,2,(31,35,58))
        self.selecao.draw()
        #logo
        #logo = arcade.Sprite("img/textos/logo.png",center_x=self.center_x,center_y=self.center_y + 150,scale=1)
        #logo.draw()

        #botoes
        for botao in self.lista_botoes:
            botao.draw()

    def on_key_release(self, key, key_modifiers):
        self.selecao.on_key_release(key,key_modifiers)
