import telebot
print("Log all mesage from user")
print("Github:https://github.com/Begitdj/Telegram-Logger-Bot/")
tokenx = input("Enter bot token:")
bot = telebot.TeleBot(tokenx)
@bot.message_handler(content_types=["text"])
def handle_text(message):
	print("User Name:", message.from_user.first_name) #Имя
	print("User id:", message.from_user.id) # id пользователя
	print("Chat Id:", message.chat.id) # Id чата
	print("Chat Title:", message.chat.title) # Имя Чата
	print("Message Text:", message.text) #Текст
	print("Message id:", message.message_id)
@bot.message_handler(content_types=['sticker'])
def handle_sticker(msg):
	print("User Name:", msg.from_user.first_name) #Имя
	print("User id:", msg.from_user.id) # id пользователя
	print("Stickerpack url:", msg.sticker.set_name) # Конец url стикер пака
	print("Sticker id:", msg.sticker.file_id) # id стикера
	print("Chat Id:", msg.chat.id) # id чата
	print("Chat Title:", msg.chat.title) # Имя чата
	print("Message id:", msg.message_id) # id сообщения
bot.polling(none_stop=True, interval=0)
