import arcade
from botoes.botao_voltar import Botao_voltar_ao_menu
from botoes.botao_repetir import Botao_repetir
from botoes.botao_mais import Botao_mais
from botoes.botao_menos import Botao_menos
from config import *
from box_selecoes.selecao_partida import Selecao_partida

class Partida():
    def __init__(self,largura_tela,altura_tela):
        self.largura_tela = largura_tela
        self.altura_tela = altura_tela
        self.center_x = largura_tela/2
        self.center_y = altura_tela/2
        self.selecao = Selecao_partida(self.center_x,self.altura_tela - 50)
        self.vaca = arcade.Sprite("img/vaca.jpg",center_x=self.center_x,center_y=self.center_y + 60,scale=0.4)
        self.patos = arcade.Sprite("img/patos.jpg",center_x=self.center_x,center_y=self.center_y + 60,scale=0.4)
        voltar = Botao_voltar_ao_menu(80,self.altura_tela-50)
        repetir = Botao_repetir(self.largura_tela-80,self.altura_tela-50)
        self.somar = Botao_mais(self.center_x,220)
        self.sub = Botao_menos(self.center_x,175)
        self.lista_botoes = [voltar,repetir,self.somar,self.sub]
        self.numero = 0
        self.timer = 0
        self.vez1 = True
        self.tempo_trocar = 5
        self.trocar = False
        self.som_erro = arcade.load_sound('sons/erro.wav')
        self.som_acerto = arcade.load_sound('sons/acerto.wav') 

    def setup(self):
        self.timer = 0
        self.numero = 0
        self.trocar = False
        self.vez1 = True
        #arcade.play_sound(self.selecao.descr_prob)
    
    def draw(self):
        
        #fundo
        
        arcade.draw_rectangle_filled(self.center_x,self.center_y,self.largura_tela, self.altura_tela,(20, 73, 107))
        arcade.draw_rectangle_filled(self.center_x,self.center_y,self.largura_tela, self.altura_tela - 200,(19,106,159,240))
        arcade.draw_rectangle_filled(self.center_x,self.center_y-170,140,40,(20, 73, 107,240))
        arcade.draw_text(DESCRICAO_PROBLEMA,self.center_x,560,arcade.color.WHITE,14,anchor_x="center",anchor_y="center")
        arcade.draw_text(str(self.numero),self.center_x,self.center_y-170,arcade.color.WHITE,14,anchor_x="center",anchor_y="center")
        if not self.trocar:
            self.vaca.draw()
        else:
            self.patos.draw()
        #botoes
        if self.selecao.coluna_atual == COLUNA1:
            self.selecao.draw()
        elif self.selecao.coluna_atual == COLUNA2:
            arcade.draw_rectangle_outline(self.somar.center_x,self.somar.center_y,47,47,(199,33,47),2)
        elif self.selecao.coluna_atual == COLUNA3:
            arcade.draw_rectangle_outline(self.sub.center_x,self.sub.center_y,43,43,(199,33,47),2)
        elif self.selecao.coluna_atual == COLUNA4:
            arcade.draw_rectangle_outline(self.center_x,self.center_y-170,145,45,(199,33,47),2)

        for botao in self.lista_botoes:
            botao.draw()
        
    def on_key_release(self, key, key_modifiers):
        acao = self.selecao.on_key_release(key,key_modifiers)
        if acao == SOMAR:
            self.numero += 1 
        elif acao == SUBTRAIR:
            if self.numero -1 > -1:
                self.numero -= 1
        elif acao == VERIFICAR_RESULTADO:
            if self.numero == RESPOSTA_PARTIDA:
                arcade.play_sound(self.som_acerto)
                #COLOCAR SOM E TALS
                return MENU
            else:
                arcade.play_sound(self.som_erro)
        else:
            return acao 

    def on_mouse_scroll(self, x: int, y: int, scroll_x: int, scroll_y: int):
        self.selecao.on_mouse_scroll(x,y,scroll_x,scroll_y)

    def on_mouse_release(self, x, y, button, modifiers):
        acao = self.selecao.on_mouse_release(x,y,button,modifiers)
        if acao == SOMAR:
            self.numero += 1
        elif acao == SUBTRAIR:
            if self.numero -1 > -1:
                self.numero -= 1
        elif acao == VERIFICAR_RESULTADO:
            if self.numero == RESPOSTA_PARTIDA:
                arcade.play_sound(self.som_acerto)
                #COLOCAR SOM E TALS
                print("RESPOSTA CORRETA")
                return MENU
            else:
                arcade.play_sound(self.som_erro)
        else:
            return acao

    def update(self,delta_time):
        self.timer += delta_time
        if self.timer >= self.tempo_trocar:
            self.trocar = True
            self.timer = 0