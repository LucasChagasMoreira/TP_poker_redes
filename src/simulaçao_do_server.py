import socket
import time
import threading
from constantes import *

#objeto socket
#AF_INET especifica o tipo de endereço que o objeto ira receber
#SOCK_STREAM indica que o tipo de conexao do socket é sequencial
server = socket.socket(socket.AF_INET,socket.SOCK_STREAM)

#Conecta o objeto socket "server" ao endereço
server.bind(ADDR)

conexoes = {}

#nome_jogadores = []

def handle_client(connect,endereco,enderecos):

    enviar_mensagem(connect,"Digite seu nome jogador")
    nome = receber_mensagem(connect)
    receber_mensagem(connect)

    enderecos.append((endereco,nome))

def enviar_para_jogador(dados,mensagem):
    global conexoes
    if dados[0] in conexoes:
        cliente_socket = conexoes[dados[0]]
        try:
            enviar_mensagem(cliente_socket,MENSAGEM_QUALQUER)
            enviar_mensagem(cliente_socket,mensagem)
        except:
            # Lidar com a exceção se a conexão estiver fechada ou ocorrer um erro de envio
            print(f"Erro ao enviar mensagem para {dados[0]}")



def conectar_jogadores():
    global conexoes
    start_time = time.time()
    enderecos = []
    lista_threads = []
    qtd_threads = 0
    while qtd_threads < 2:
        threads_ativas = threading.active_count()-1
        #aceita conecçao com algum cliente
        connect,endereco = server.accept()
        conexoes[endereco] = connect

        #inicia um thread para cuidar do cliente atravez da funçao handle_cliente
        thread = threading.Thread(target=handle_client,args=(connect,endereco,enderecos))
        thread.start()
        lista_threads.append(thread)
        qtd_threads += 1
        print(f'[conecções ativas] {qtd_threads}')
        

    if qtd_threads >= 2:
        print("Número máximo de threads atingido.")
    else:
        print("Tempo limite atingido, encerrando a função.")

    # Esperar que todas as threads terminem
    for thread in lista_threads:
            thread.join()
    
    return enderecos
    
def envia_para_todos(mensagem,grupo_de_jogadores):
    global conexoes

    for endereco in grupo_de_jogadores:
        if endereco[0] in conexoes:
            cliente_socket = conexoes[endereco[0]]
            try:
                enviar_mensagem(cliente_socket,MENSAGEM_QUALQUER)
                enviar_mensagem(cliente_socket,mensagem)
            except:
                # Lidar com a exceção se a conexão estiver fechada ou ocorrer um erro de envio
                print(f"Erro ao enviar mensagem para {endereco}")
        else:
            print(f"Cliente {endereco} não encontrado.")

def envia_para_todos_menos_um(mensagem,grupo_de_jogadores,excluido):
    global conexoes

    for endereco in grupo_de_jogadores:
        if endereco[0] in conexoes and endereco != excluido:
            cliente_socket = conexoes[endereco[0]]
            try:
                enviar_mensagem(cliente_socket,MENSAGEM_QUALQUER)
                enviar_mensagem(cliente_socket,mensagem)
            except:
                # Lidar com a exceção se a conexão estiver fechada ou ocorrer um erro de envio
                print(f"Erro ao enviar mensagem para {endereco}")
        else:
            print(f"Mensagem nao foi enviada para o {endereco}.")

def funcao_de_encerramento(endereco):
    global conexoes

    if endereco[0] in conexoes:
        cliente_socket = conexoes[endereco[0]]
        try:
            enviar_mensagem(cliente_socket,"end")
        except:
            # Lidar com a exceção se a conexão estiver fechada ou ocorrer um erro de envio
            print(f"Erro ao enviar mensagem para {endereco}")
    else:
        print(f"Cliente {endereco} não encontrado.")
    
def requisita_jogada(dados):
    
    global conexoes

    if dados[0] in conexoes:
        cliente_socket = conexoes[dados[0]]
        try:
            enviar_mensagem(cliente_socket,JOGADA)
            return receber_mensagem(cliente_socket)
        
        except:
            # Lidar com a exceção se a conexão estiver fechada ou ocorrer um erro de envio
            print(f"Erro ao enviar mensagem para {dados[0]}")
    else:
        print(f"Cliente {dados[0]} não encontrado.")
    

