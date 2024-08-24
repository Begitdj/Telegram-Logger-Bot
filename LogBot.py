import telebot
import time
import json
print("Log all mesage from user")
print("Github:https://github.com/Begitdj/Telegram-Logger-Bot/")
tokenx = input("Enter bot token:")
direcsave = input("Enter Full Directory patch to save photo stickers and other[Example:/other/botsave/]:")
print("Directory Set! Create in your directory folders with name videos and voice and stickers and photos and music and documents for correct saving without error")
print("Bot starting.")
bot = telebot.TeleBot(tokenx)
@bot.message_handler(content_types=["text"])
def handle_text(message):
	print("User Name:", message.from_user.first_name) #Имя
	print("User id:", message.from_user.id) # id пользователя
	print("Chat Id:", message.chat.id) # Id чата
	print("Chat Title:", message.chat.title) # Имя Чата
	print("Message Text:", message.text) #Текст
	print("Message id:", message.message_id)
	print("Timestamp:", message.date)
	tconv = lambda x: time.strftime("%H:%M:%S %d.%m.%Y", time.localtime(x)) #Конвертация даты в читабельный вид
	print("Time:",tconv(message.date)) # Вывод даты типо 20:58:30 05.07.2020')
@bot.message_handler(content_types=['sticker'])
def handle_sticker(message):
	print("User Name:", message.from_user.first_name) #Имя
	print("User id:", message.from_user.id) # id пользователя
	print("Stickerpack url:", message.sticker.set_name) # Конец url стикер пака
	print("Sticker id:", message.sticker.file_id) # id стикера
	print("Chat Id:", message.chat.id) # id чата
	print("Chat Title:", message.chat.title) # Имя чата
	print("Message id:", message.message_id) # id сообщения
	print("Sticker emoji:", message.sticker.emoji)
	tconv = lambda x: time.strftime("%H:%M:%S %d.%m.%Y", time.localtime(x)) #Конвертация даты в читабельный вид
	print("Time:",tconv(message.date)) # Вывод даты типо 20:58:30 05.07.2020
	file_info = bot.get_file(message.sticker.file_id)
	downloaded_file = bot.download_file(file_info.file_path)
	src = direcsave + file_info.file_path
	with open(src, "wb") as new_file:
		new_file.write(downloaded_file)
@bot.message_handler(content_types=["document"])
def handle_files(message):
	if message.document and message.document.file_id:
		print("User Name:", message.from_user.first_name) #Имя
		print("User id:", message.from_user.id) # id пользователя
		print("Chat Id:", message.chat.id) # Id чата
		print("Chat Title:", message.chat.title) # Имя Чата
		print("Message id:", message.message_id)
		print("Timestamp:", message.date)
		tconv = lambda x: time.strftime("%H:%M:%S %d.%m.%Y", time.localtime(x)) #Конвертация даты в читабельный вид
		print("Time:",tconv(message.date)) # Вывод даты типо 20:58:30 05.07.2020
		print("Documents id:", message.document.file_id)
		file_info = bot.get_file(message.document.file_id)
		downloaded_file = bot.download_file(file_info.file_path)
		src = direcsave + file_info.file_path
		with open(src, "wb") as new_file:
			new_file.write(downloaded_file)
@bot.message_handler(content_types=["photo"])
def handle_files(message):
		print("User Name:", message.from_user.first_name) #Имя
		print("User id:", message.from_user.id) # id пользователя
		print("Chat Id:", message.chat.id) # Id чата
		print("Chat Title:", message.chat.title) # Имя Чата
		print("Message id:", message.message_id)
		print("Timestamp:", message.date)
		tconv = lambda x: time.strftime("%H:%M:%S %d.%m.%Y", time.localtime(x)) #Конвертация даты в читабельный вид
		print("Time:",tconv(message.date)) # Вывод даты типо 20:58:30 05.07.2020
		print("Photo json:", *message.photo)
		file_info = bot.get_file(message.photo[len(message.photo)-1].file_id)
		downloaded_file = bot.download_file(file_info.file_path)
		src = direcsave + file_info.file_path
		with open(src, "wb") as new_file:
			new_file.write(downloaded_file)
@bot.message_handler(content_types=["video"])
def handle_files(message):
	if message.video and message.video.file_id:
		print("User Name:", message.from_user.first_name) #Имя
		print("User id:", message.from_user.id) # id пользователя
		print("Chat Id:", message.chat.id) # Id чата
		print("Chat Title:", message.chat.title) # Имя Чата
		print("Message id:", message.message_id)
		print("Timestamp:", message.date)
		tconv = lambda x: time.strftime("%H:%M:%S %d.%m.%Y", time.localtime(x)) #Конвертация даты в читабельный вид
		print("Time:",tconv(message.date)) # Вывод даты типо 20:58:30 05.07.2020
		print("Video id:", message.video.file_id)
		file_info = bot.get_file(message.video.file_id)
		downloaded_file = bot.download_file(file_info.file_path)
		src = direcsave + file_info.file_path
		with open(src, "wb") as new_file:
			new_file.write(downloaded_file)
@bot.message_handler(content_types=["audio"])
def handle_files(message):
	if message.audio and message.audio.file_id:
		print("User Name:", message.from_user.first_name) #Имя
		print("User id:", message.from_user.id) # id пользователя
		print("Chat Id:", message.chat.id) # Id чата
		print("Chat Title:", message.chat.title) # Имя Чата
		print("Message id:", message.message_id)
		print("Timestamp:", message.date)
		tconv = lambda x: time.strftime("%H:%M:%S %d.%m.%Y", time.localtime(x)) #Конвертация даты в читабельный вид
		print("Time:",tconv(message.date)) # Вывод даты типо 20:58:30 05.07.2020
		print("Audio id:", message.audio.file_id)
		file_info = bot.get_file(message.audio.file_id)
		downloaded_file = bot.download_file(file_info.file_path)
		src = direcsave + file_info.file_path
		with open(src, "wb") as new_file:
			new_file.write(downloaded_file)
@bot.message_handler(content_types=["voice"])
def handle_files(message):
	if message.voice and message.voice.file_id:
		print("User Name:", message.from_user.first_name) #Имя
		print("User id:", message.from_user.id) # id пользователя
		print("Chat Id:", message.chat.id) # Id чата
		print("Chat Title:", message.chat.title) # Имя Чата
		print("Message id:", message.message_id)
		print("Timestamp:", message.date)
		tconv = lambda x: time.strftime("%H:%M:%S %d.%m.%Y", time.localtime(x)) #Конвертация даты в читабельный вид
		print("Time:",tconv(message.date)) # Вывод даты типо 20:58:30 05.07.2020
		print("voice id:", message.voice.file_id)
		file_info = bot.get_file(message.voice.file_id)
		downloaded_file = bot.download_file(file_info.file_path)
		src = direcsave + file_info.file_path
		with open(src, "wb") as new_file:
			new_file.write(downloaded_file)
bot.polling(none_stop=True, interval=0)
