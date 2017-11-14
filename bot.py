# -*- coding: utf-8 -*-
import telebot 
from telebot import types
import os

TOKEN = ''
bot = telebot.TeleBot(TOKEN) # Make our Bot Object

def listener(messages): # Con esto, estamos definiendo una función llamada 'listener', que recibe como parámetro un dato llamado 'messages'.
    for m in messages: # Por cada dato 'm' en el dato 'messages'
    	print(m.content_type)
    	if m.content_type == 'document':
    		print(m.document.file_name)
    		file_info = bot.get_file(m.document.file_id)
    		downloaded_file = bot.download_file(file_info.file_path)
    		path ='~/'
    		if m.from_user.username == None:
    			path = path +'Desconocido'
    		else:
    			path = path + m.from_user.username

    		if not os.path.exists(path):
    			os.makedirs(path)

    		path = path + '/' + m.document.file_name

    		with open(path, 'wb') as new_file:
    			new_file.write(downloaded_file)
        if m.content_type == 'text': # Filtramos mensajes que sean tipo texto.
            cid = m.chat.id # Almacenaremos el ID de la conversación.
            print ("[" + str(cid) + "]: " + m.text) # Y haremos que imprima algo parecido a esto -> [52033876]: /start

bot.set_update_listener(listener) # Así, le decimos al bot que utilice como función escuchadora nuestra función 'listener' declarada arriba.

bot.polling(none_stop=True)