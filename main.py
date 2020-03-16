import vk_api
from vk_api.bot_longpoll import VkBotLongPoll, VkBotEventType
from vk_api.utils import get_random_id
from pars import print_score



def vkbot():
    vk_session=vk_api.VkApi(token='fcb715bac83de58c82745490f78b4bc7264bf23035dbff8d35c1531193f8acc43113122ad9866cb78e6a6') #Сообщество https://vk.com/club192951175
    longpoll=VkBotLongPoll(vk_session,'192951175')
    vk = vk_session.get_api()
    for event in longpoll.listen():

        if event.type == VkBotEventType.MESSAGE_NEW:
            print('Новое сообщение:')
            print('Для меня от: ', end='')
            print(event.obj.message["peer_id"])
            print('Текст:', event.obj.message["text"])
            print()
            if event.obj.message["text"]=="!счёт" or event.obj.message["text"]=="!счет":
                text=print_score("http://ig.pro100basket.ru/game/?id=80466&tab=0&compId=42127&region=40120&db=asb")
                vk.messages.send(
                    user_id=event.obj.message["peer_id"],
                    random_id=get_random_id(),
                    message=text
                )


vkbot()

