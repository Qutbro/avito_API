import requests
import time
import json
from config import user_id


# Функция для загрузки токена из файла
def load_token_from_file(filename='access_token.json'):
    try:
        with open(filename, 'r') as file:
            token_data = json.load(file)
            return token_data['access_token']
    except FileNotFoundError:
        return None


access_token = load_token_from_file()
chat_ids = []
base_url = 'https://api.avito.ru'

headers = {
    'Authorization': f'Bearer {access_token}',
    'Content-Type': 'application/json'
}


def get_messege():
    url = base_url + "/messenger/v2/accounts/{user_id}/chats".format(user_id=user_id)
    try:
        prams = {
            "unread_only": "true"
        }
        oll_chats = requests.get(url, headers=headers, params=prams)
        return json.loads(oll_chats.text)
    except Exception as e:
        print(e)


def get_tabl_chat(chat_id):
    url = base_url + "/messenger/v3/accounts/{user_id}/chats/{chat_id}/messages/".format(user_id=user_id,
                                                                                         chat_id=chat_id)
    try:
        chat_context = requests.get(url, headers=headers)
        return json.loads(chat_context.text)
    except Exception as e:
        print(e)


def read_chat(chat_id):
    url = base_url + "/messenger/v1/accounts/{user_id}/chats/{chat_id}/read".format(user_id=user_id, chat_id=chat_id)
    try:
        TF_read_chat = requests.post(url, headers=headers)
        return json.loads(TF_read_chat.text)
    except Exception as e:
        print(e)


def messege_send(mess, chat_id):
    url = base_url + "/messenger/v1/accounts/{user_id}/chats/{chat_id}/messages".format(user_id=user_id,
                                                                                        chat_id=chat_id)
    try:
        data = {
            'text': mess
        }
        send_messege_result = requests.post(url, headers=headers, data=data)
        return json.loads(send_messege_result)
    except Exception as e:
        print(e)


def generate_GPT(chat_id, unread_messages):
    print("chat_id:" + chat_id + "   text:" + unread_messages)


def main():
    print("Начало мониторинга новых сообщений...")
    while True:
        try:
            chats = get_messege()
            print(chats)
            for chat in reversed(chats['chats']):
                chat_ids.append(chat['id'])
            print(chat_ids)
            # chat_id= chats["chats"][0]["id"]
            # print(chat_id)
            for chat_id in chat_ids:
                chat_all_messege = get_tabl_chat(chat_id)
                unread_messages = " ".join(
                    [msg['content']['text'] for msg in chat_all_messege['messages'] if not msg['isRead']][::-1])
                generate_GPT(chat_id, unread_messages)
            chat_ids.clear()
            # unread_messages = " ".join([msg['content']['text'] for msg in chat_all_messege['messages'] if not msg['isRead']][::-1])
            # id = chats["chats"][0]["last_message"]["author_id"]
            # message_content = chats["chats"][0]["last_message"]["content"]["text"]
            # print(f"{id}: {message_content}")
            print("----------------------")
            # print(chats)
            # print(chat_all_messege)
            # print("chat_id:"+ chat_id +"   text:" +unread_messages)
            time.sleep(15)

        except Exception as e:
            print(f'Ошибка: {e}')
            time.sleep(15)
    pass


if __name__ == '__main__':
    main()
