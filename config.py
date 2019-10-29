import pyttsx3

#CONFIG TELAS
LARGURA_TELA = 800
ALTURA_TELA = 600
TITULO_TELA = "SACS - SOFTWARE DE ACESSIBILIDADE PARA CEGOS E SURDOS"

#DIMENSOES BOX DE SELEÇÃO DO MENU
LARGURA_IMG = 475
ALTURA_IMG = 165

#Y DAS COLUNAS DO MENU 
Y_PRIMEIRA_COLUNA = 430
Y_SEGUNDA_COLUNA = 200

#COORDENADAS DAS POSIÇÕES DO BOX
PARTIDA_COLUNA1_Y = 80
#PARTIDA_COLUNA2_Y = 
#PARTIDA_COLUNA3_Y =
#PARTIDA_COLUNA4_Y = 

#ON_MOUSE_SCROLL
SCROLL_BAIXO = -1
SCROLL_CIMA = 1

#MARCADOR VERIFICADOR DE COLUNA
COLUNA1 = "COLUNA1"
COLUNA2 = "COLUNA2"
COLUNA3 = "COLUNA3"
COLUNA4 = "COLUNA4"
COLUNA5 = "COLUNA5"

SAIR = -1
MENU = 0
PARTIDA = "PARTIDA"
AJUDA = 2
SOMAR = 'somar'
SUBTRAIR = 'subtrair'
VERIFICAR_RESULTADO = "VERIFICAR"

DESCRICAO_MENU = '''Você está no menu, a tela inicial do jogo. As ações que você pode fazer aqui são: iniciar uma partida, 
pedir ajuda ou sair do jogo'''
FALA_COLUNA1_MENU = '''clique com o botão esquerdo para iniciar uma partida ou com o direito para ouvir essa mensagem novamente.
A partida funciona como um jogo de perguntas e respostas baseadas no som que você ouvirá.'''
FALA_COLUNA2_MENU = '''clique com o botão esquerdo para sair do jogou no direito para ouvir essa mensagem novamente'''
FALA_COLUNA1_PARTIDA = '''Clique com o botão esquerdo para voltar para o menu ou no direito para ouvir o desafio novamente'''
FALA_COLUNA2_PARTIDA ='''Clique com o botão esquerdo para somar ou no direito para ouvir o desafio novamente'''
FALA_COLUNA3_PARTIDA ='''Clique com o botão esquerdo para subtrair ou no direito para ouvir o desafio novamente'''
FALA_COLUNA4_PARTIDA ='''Clique para com o botão esquerdo para verificar a resposta ou com o direito para ouvir o desafio novamente'''
DESCRICAO_PROBLEMA ='''Problema: Você foi para uma fazenda e econtrou uma vaca. 
Em seguida apareceu um pato e uma pata, mas a vaquinha 
entediada saiu para pastar.
Quantos animais sobraram?'''


TEXTO_JOGAR = 'Jogar'
TEXTO_AJUDA = 'Ajuda'
TEXTO_MANUAL = 'Manual'
TEXTO_SAIR = 'Sair'


RESPOSTA_PARTIDA = 2

TAMANHO_BOX_MENOS = 46.2
TAMANHO_BOX_MAIS = 56


def falar_frase(frase):
    engine = pyttsx3.init()
    id = "HKEY_LOCAL_MACHINE\SOFTWARE\Microsoft\Speech\Voices\Tokens\TTS_MS_PT-BR_MARIA_11.0"
    engine.setProperty('voice', id)
    engine.say(frase)
    engine.save_to_file(frase,"teste", "sons/")
    engine.runAndWait()
    