import speech_recognition as sr
import pyttsx3
from config import *
from random import choice


reproducao = pyttsx3.init()
voices = reproducao.getProperty('voices')
reproducao.setProperty('voices', voices[1].id)


def sai_som(resposta):
    reproducao.say(resposta)
    reproducao.runAndWait()

def assistente():
    print("( ' - ') Just Do IT")
    sai_som("Eu me chamo Fritz, com quem eu falo?")
    while True:
        resposta_erro_aleatoria = choice(lista_erros)
        rec = sr.Recognizer()
        with sr.Microphone() as s:
            rec.adjust_for_ambient_noise(s)

            while True:
                try:
                    audio = rec.listen(s)
                    user_name = rec.recognize_google(audio, language="pt")
                    user_name = verifica_nome(user_name)
                    name_list()
                    apresentacao = "{}".format(verifica_nome_existe(user_name))
                    print(apresentacao)
                    sai_som(apresentacao)

                    brute_user_name = user_name
                    user_name = user_name.split(" ")
                    user_name = user_name[0]
                    break


                except sr.UnknownValueError:
                    print(resposta_erro_aleatoria)
                    sai_som(resposta_erro_aleatoria)
            break

    print("="* len(apresentacao))
    print("Ouvindo.....")
    while True:
        resposta_erro_aleatoria = choice(lista_erros)
        rec = sr.Recognizer()
        with sr.Microphone() as s:
            rec.adjust_for_ambient_noise(s)

            while True:
                try:
                    audio = rec.listen(s)
                    entrada = rec.recognize_google(audio, language="pt-br")
                    print("{}: {}".format(user_name, entrada))


                    #Pesquisa Google
                    if "pesquisa" in entrada:
                        resposta = pesquisa(entrada)

                    #Abrir Aplicativo
                    elif "Abrir" in entrada:
                        resposta = abrir(entrada)

                    #operações matemáticas
                    elif "Quanto é" in entrada or "quanto é" in entrada:
                        entrada = entrada.replace("Quanto é", "")
                        resposta = calcula(entrada)

                    # Pede Tempo
                    elif "temperatura" in entrada:

                        lista_tempo = temperatura()
                        temp = lista_tempo[0]
                        temp_max = lista_tempo[1]
                        temp_min = lista_tempo[2]

                        resposta = "A temperatura de hoje é {:.2f}°. Temos a máxima de {:.2f}° e uma minima de {:.2f}°".format(temp,  temp_max, temp_min)

                    # Informações da cidade
                    elif "informações" in entrada and "cidade" in entrada:

                        resposta = "Mostrando informações da cidade"

                    else:
                        resposta = conversas[entrada]

                    if resposta == "Mostrando informações da cidade":
                        #mostra informações da cidade

                        lista_infos = clima_tempo()
                        longitude = lista_infos[0]
                        latitude = lista_infos[1]
                        temp = lista_infos[2]
                        pressao_atm = lista_infos[3]
                        humidade = lista_infos[4]
                        temp_max = lista_infos[5]
                        temp_min = lista_infos[6]
                        v_speed = lista_infos[7]
                        v_direc = lista_infos[8]
                        nebulosidade = lista_infos[9]
                        id_da_cidade = lista_infos[10]

                        print("Assistente:")
                        print("Mostrando informações de {}\n\n".format(cidade))
                        sai_som("Mostrando informações de {}".format(cidade))
                        print("Longitude: {}, Latitude: {}\nId: {}\n".format(longitude, latitude, id_da_cidade))
                        print("Temperatura : {:.2f}°".format(temp))
                        print("Temperatura Máxima : {:.2f}°".format(temp_max))
                        print("Temperatura Mínima : {:.2f}°".format(temp_min))
                        print("Humidade: {}".format(humidade))
                        print("Nebulosidade: {}".format(nebulosidade))
                        print("Velocidade do vento: {}m/s\nDireção do vento: {}".format(v_speed,v_direc))

                    else:
                        print('Fritz: {}'.format(resposta))
                        sai_som('{}'.format(resposta))

                except sr.UnknownValueError:
                    print(resposta_erro_aleatoria)
                    sai_som(resposta_erro_aleatoria)

if __name__ == '__main__':
    intro()
    sai_som("iniciando")
    assistente()




