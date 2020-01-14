
from chatterbot.trainers import ListTrainer  # Treinador
from chatterbot import ChatBot  # Chatbot
from random import randint
import os  # SO
from time import sleep

class Bot:

    global bot
    global bott
    bot = ChatBot('Donizete')

    def __init__(self, name):
        self.name = name

    def treinador(self):
        bot.set_trainer(ListTrainer)
        for Base in os.listdir('Base'):  # Ler os aquivos e as linhas
            chats = open('Base/' + Base, "r").readlines()
            bot.train(chats)

    def bot_respost(self, name):  # bott nome do cara,nome nome da pessoa,inden numero d identificação
        print('Para sair digite "exit"')
        print(str('Donizete:Oi'))
        while True:  # ler e responder as questões
            pessoa = input('{}:'.format(name))
            pessoa = pessoa.title()  # Deixar Primeiras letras maiusculas
            if pessoa == 'Exit':
                return 0

            resp = str(bot.get_response(pessoa))
            resp = resp.rstrip('\n')
            print('Donizete:' + str(resp))

