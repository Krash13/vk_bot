import vk_api
from vk_api.bot_longpoll import VkBotLongPoll, VkBotEventType

vk_session=vk_api.VkApi(token='fcb715bac83de58c82745490f78b4bc7264bf23035dbff8d35c1531193f8acc43113122ad9866cb78e6a6') #Сообщество https://vk.com/club192951175
longpoll=VkBotLongPoll(vk_session,'192951175')

for event in longpoll.listen():

    if event.type == VkBotEventType.MESSAGE_NEW:
        print('Новое сообщение:')

        print('Для меня от: ', end='')

        print(event.obj.message["peer_id"])

        print('Текст:', event.obj.message["text"])
        print()

