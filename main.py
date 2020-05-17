import vk_api #импортируем vk.api
from vk_api.longpoll import VkLongPoll, VkEventType
from datetime import datetime
import random
import time

#получаем токен
token = 'b800a2500b3cfcc5d60599e57a418e433a3b21f0eb92fdbe2ebc02c5df164aaa031f16e197117814a194a'
vk_session = vk_api.VkApi ( token = token )

session_api = vk_session.get_api()
longpoll = VkLongPoll( vk_session )

while True:
    for event in longpoll.listen():
        if event.type == VkEventType.MESSAGE_NEW:
            print('Сообщение пришло в: ' + str(datetime.strftime(datetime.now(), "%H:%M:%S")))
            print(f'Текст сообщения {str(event.text)}')
            print(event.user_id)
            request = event.text.lower()
            if event.from_user and not (event.from_me):
                if request == 'привет':
                    import test.py


