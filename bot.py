from telegram.ext import Updater , commandHandler
import urllib
update =Updater("token")
def start_method(bot , update):

   my_ip = urlib.urlopen("http://ip.42.pl/raw").read()

  chat_id =update.message.chat_id
  bot.sendMessage(chat_id,"your ip is",my_ip)
start = CommandHandler("start" , start_method)
update.dispatcher.add_handler(start)
update.start_polling()
