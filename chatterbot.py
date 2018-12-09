from chatterbot.trainers import ListTrainer
from chatterbot import ChatBot

bot = ChatBot('ChatBot 101')

chat = ['Hi', 'Hello', 'Fine', 'Great', 'Do you like programming?', 'Yes, I love Python']

bot.set_trainer(ListTrainer)
bot.train(chat)

while 1 == 1:
    ask = input('User: ')
    answer = bot.get_response(ask)
    if float(resposta.confidence) > 0.5:
        print('Bot: ', answer)
    else:
        print("Bot: I don' t hava answer for this question yet")
