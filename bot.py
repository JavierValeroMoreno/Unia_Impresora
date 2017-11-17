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
            
            if (m.from_user.username == None):
                name = 'Desconocido'
            else:
                name = m.from_user.username

            if(os.uname()[0] == 'Linux'):
                path = 'Impresora' + '/' + name
                file_path = path + '/' + m.document.file_name
            else:
                path = 'Impresora' + '\\' + name
                file_path = path + '\\' + m.document.file_name

            if (not os.path.exists(path)):
                os.makedirs(path)

            with open(file_path, 'wb') as new_file:
                new_file.write(downloaded_file)

            bot.send_message(-272075206,'Se ha recibido el archivo: ' + m.document.file_name + '\nEn el directorio: ' + name)
        if m.content_type == 'text':
            cid = m.chat.id # Almacenaremos el ID de la conversación.
            print ("[" + str(cid) + "]: " + m.text) # Y haremos que imprima algo parecido a esto -> [52033876]: /start

bot.set_update_listener(listener) # Así, le decimos al bot que utilice como función escuchadora nuestra función 'listener' declarada arriba.

@bot.message_handler(commands = ['help'])
def help(m):
    name = ''
    if m.from_user.username == None:
        name = 'Desconocido'
    else:
        name = m.from_user.username
    text = '''Instrucciones de uso del bot:
    1-El archivo a enviar debe de ser un documento, no se aceptan mensajes de texto, audios,sonido, fotos ni ningun tipo de elemento de otra indole
    2-Se agradeceria que el archivo tenga un nombre significativo e inequivoco para asi facilitar la busqueda a la hora de necesitarlo
    3-Es opcional, pero recomendable, que el usuario posea un alias/username de telegram, asi el archivo podra alojarse en una carpeta personal

    El archivo se alojara en la ruta siguiente C:\\Impresora\\''' + name +'''
    Para mas dudas puede contactar con el creador del bot @NullPointException'''
    bot.send_message(m.chat.id, text)

bot.polling(none_stop=True)
