import  telebot 

bot =telebot.TeleBot('5359613323:AAHtS1FZ2OcQFlY86VtShQ_13_EcIsKgyP4')

@bot.message_handler(commands=["start"])
def start(message):
    bot.send_message(message.chat.id,' введите номер картинки ')
    bot.send_message(message.chat.id,'1-lamborghini')
    bot.send_message(message.chat.id,'2-BMW')
    bot.send_message(message.chat.id,'3-mercedes') 
    bot.send_message(message.chat.id,"4-lada") 
    bot.send_message(message.chat.id,"5-mazda")    
@bot.message_handler( )             
def get_user_text(message):
 if message.text == ('1'):
    phot = open('lamborghini.jpg','rb')
    bot.send_photo(message.chat.id,phot)
    
 if message.text == ('2'):
    phot1 = open('BMW.jpg','rb')
    bot.send_photo(message.chat.id,phot1)

 if message.text == ('3'):
    phot2 = open('mercedes.jpg','rb')
    bot.send_photo(message.chat.id,phot2)

 if message.text == ('4'):
    phot3 = open('lada.jpg','rb')
    bot.send_photo(message.chat.id,phot3)

 if message.text == ('5'):
    phot4 = open('mazda.jpg','rb')
    bot.send_photo(message.chat.id,phot4)       

bot.polling(none_stop=True)