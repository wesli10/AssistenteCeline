import requests as rq
import webbrowser as web
import os
from requests.api import get
from googlesearch import search


web.register('google-chrome', None)
version = "1.0.0"
cidade = 'sao+paulo'
caminho_navegador = "C:/Program Files/Google/Chrome/Application/chrome.exe %s"
caminho_jogos = "C:/Program Files (x86)/Steam/Steam.exe"

def intro():
    msg = "Fritz - version {} / by: Wesley Lins".format(version)
    print("-" * len(msg) + "\n{}\n".format(msg) + "-" * len(msg)) 

lista_erros = [
    "Não entendi nada",
    "Desculpe, não entendi",
    "Repita por gentileza"
]

conversas = {
    "Olá": "oi, tudo bem?",
    "sim e você": "Estou bem obrigada por perguntar",
    "suave": "Tudo tranquilo mestre",
    "como está": "O dia ta lindo, clima ensorarado"
    
}

comandos = {
    "desligar": "desligando",
    "reiniciar": "reiniciando"
}

def verifica_nome(user_name):
    if user_name.startswith("meu nome é"):
        user_name = user_name.replace("meu nome é", "")
    
    if user_name.startswith("eu me chamo"):
        user_name = user_name.replace("eu me chamo", "")

    if user_name.startswith("eu sou o"):
        user_name = user_name.replace("eu sou o", "")

    if user_name.startswith("eu sou a"):
        user_name = user_name.replace("eu sou a", "")

    return user_name


def verifica_nome_existe(nome):
    dados = open("dados/nomes.txt", "r")
    nome_list = dados.readlines()

    if not nome_list:
        vazio = open("dados/nomes.txt", "r")
        conteudo = vazio.readlines()
        conteudo.append("{}".format(nome))
        vazio = open("dados/nomes.txt", "w")
        vazio.writelines(conteudo)
        vazio.close

        return "Olá {}, prazer em te conhecer!".format(nome)

    for linha in nome_list:
        if linha == nome:
            return "Olá {}, qual a boa ?".format(nome)

    vazio = open("dados/nomes.txt", "r")
    conteudo = vazio.readlines()
    conteudo.append("\n{}".format(nome))
    vazio = open("dados/nomes.txt", "w")
    vazio.writelines(conteudo)
    vazio.close
    
    return "Oi {} ".format(nome)


def name_list():
    try:
        nomes = open("dados/nomes.txt", "r")
        nomes.close
    except FileNotFoundError:
        nomes = open("dados/nomes.txt", "w")
        nomes.close

def calcula(entrada):
    if "mais" in entrada or "+" in entrada:
        entrada_recebidas = entrada.split(" ")
        resultado = int(entrada_recebidas[1]) + int(entrada_recebidas[3])
    elif "menos" in entrada or "-" in entrada:
        entrada_recebidas = entrada.split(" ")
        resultado = int(entrada_recebidas[1]) - int(entrada_recebidas[3])
        
    elif "vezes" in entrada or "x" in entrada:
        entrada_recebidas = entrada.split(" ")
        resultado = round(float(entrada_recebidas[1]) * float(entrada_recebidas[3]), 2)

    elif "dividido" in entrada or "/" in entrada:

        entrada_recebidas = entrada.split(" ")
        resultado = round(float(entrada_recebidas[1]) / float(entrada_recebidas[4]), 2)
    else:
        resultado = "Operação não encontrada"

    return resultado


def clima_tempo():
    
    endereco_api = "https://api.openweathermap.org/data/2.5/weather?q=sao+paulo&appid=a2b5dc2df428fbf233b09e3e07376119&q??"
    url = endereco_api

    infos = rq.get(url).json()

    longitude = infos['coord']['lon']
    latitude = infos['coord']['lat']
    temp = infos['main']['temp'] - 273.15 # Kelvin para Celcius
    pressao_atm = infos['main']['pressure'] / 1013.25 #Libras para ATM
    humidade = infos['main']['humidity'] #Recebe em porcentagem
    temp_max = infos['main']['temp_max'] - 273.15 # Kelvin para Celcius
    temp_min = infos['main']['temp_min'] - 273.15 # Kelvin para Celcius
    v_speed = infos['wind']['speed']
    v_direc = infos['wind']['deg']
    nebulosidade = infos['clouds']['all']
    id_da_cidade = infos['id']

    return [longitude, latitude, temp,
            pressao_atm, humidade,
            temp_max, temp_min,
            v_speed, v_direc,
            nebulosidade, id_da_cidade]

def temperatura():

    temp_atual = clima_tempo()[2]
    temp_max = clima_tempo()[5]
    temp_min = clima_tempo()[6]
    return [temp_atual, temp_max, temp_min]

def abrir(fala):
    try:
        if "Google" in fala:
            web.get(caminho_navegador).open("google.com.br/")
            return "abrindo o google"
        elif "Netflix" in fala:
            web.get(caminho_navegador).open("netflix.com/")
            return "abrindo netflix"
        elif "Twitch" in fala:
            web.get(caminho_navegador).open("twitch.tv/")
            return "abrindo twitch"
        elif "Steam" in fala:
            os.startfile("C:/Program Files (x86)/Steam/Steam.exe")
            return "Abrindo steam"
        elif "lol" in fala:
            os.startfile("C:/Riot Games/League of Legends/LeagueClient.exe")
            return "Vai abrir esse jogo ruim mesmo ?"
        elif "Facebook" in fala:
            web.get(caminho_navegador).open("facebook.com.br/")
            return "abrindo facebook"
        elif "Instagram" in fala:
            web.get(caminho_navegador).open("instagram.com/")
            return "abrindo instagram"
        elif "Youtube" in fala:
            web.get(caminho_navegador).open("youtube.com/")
            return "abrindo Youtube"
        else:
            return "site não cadastrado para aberturas"
    except:
        return "houve um erro"


def pesquisa(fala):
    if fala.startswith("pesquisa"):
        fala = fala.replace("pesquisa", "")
    try:
        for result in search(fala, num_results=0, lang="pt"):
            web.open(result)
        return "Foi oque eu encontrei"
    except:
        print("Houve um erro na pesquisa")
    
        
