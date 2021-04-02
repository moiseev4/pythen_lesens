from vk_api.longpoll import VkLongPoll, VkEventType
from vk_api.keyboard import VkKeyboard, VkKeyboardColor
import vk_api
import data
from datetime import datetime
from vk_api.utils import get_random_id
token = '135735d4d2a12308a9b0233246f5c3573ffa41f744116df49c7eacd15828ec3830a9d09ca7a10b3657b21'
vk_session = vk_api.VkApi(token=token)

session_api = vk_session.get_api()
longpoll = VkLongPoll(vk_session)

keyboard = VkKeyboard(one_time=True)
keyboard.add_button('Привет', color=VkKeyboardColor.NEGATIVE)
keyboard.add_button('Клавиатура', color=VkKeyboardColor.POSITIVE)
keyboard.add_line()
keyboard.add_location_button()
keyboard.add_line()
keyboard.add_vkpay_button(hash="action=transfer-to-group&group_id=183415444")

while True:
    for event in longpoll.listen():
        if event.type == VkEventType.MESSAGE_NEW:
            print('сообщение пришло в: ' + str(datetime.strftime(datetime.now(), "%H:%M:%S")))
            print('Текст сообщения: ' + str(event.text))
            print(event.user_id)
            response = event.text.lower()
            if event.from_user and not (event.from_me):
                if response == "привет":
                    vk_session.method('messages.send',
                                      {'user_id': event.user_id, 'message': 'Привет, как ты понимаешь - я родился!', 'random_id': 0})
                elif response == "тупой бот":
                    vk_session.method('messages.send',
                                      {'user_id': event.user_id, 'message': 'Я только учусь, не крошите на меня батон, я тоже могу быть злым!', 'random_id': 0})
                elif response == "как дела?":
                    vk_session.method('messages.send',
                                      {'user_id': event.user_id, 'message': 'Всё прекрасно, твои как дружище?', 'random_id': 0})
