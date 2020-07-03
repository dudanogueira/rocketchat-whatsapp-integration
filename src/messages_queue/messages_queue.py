import os
import json
from src.constants import CHAT_API_QUEUE_FOLDER, ROCKET_QUEUE_FOLDER
class ChatApiMessageQueue:
    @staticmethod
    def store(message):
        message_id = message["id"].replace("@", "-").replace(".", "-")
        message = [message]
        message_content = json.dumps(message)
        file_path = CHAT_API_QUEUE_FOLDER + message_id
        message_file = open(file_path, "w")
        message_file.write(message_content)
        message_file.close()

    @staticmethod
    def delete(message):
        message_id = message["id"].replace("@", "-").replace(".", "-")
        file_path = CHAT_API_QUEUE_FOLDER + message_id
        if(os.path.isfile(file_path)):
            try:
                os.remove(file_path)
            except:
                print("Couldn't delete file:", file_path)

            

class RocketChatMessageQueue:
    @staticmethod
    def store(message, uuid):
        message_content = json.dumps(message)
        file_path = ROCKET_QUEUE_FOLDER + uuid
        message_file = open(file_path, "w")
        message_file.write(message_content)
        message_file.close()

    @staticmethod
    def delete(uuid):
        file_path = ROCKET_QUEUE_FOLDER + uuid
        if(os.path.isfile(file_path)):
            try:
                os.remove(file_path)
            except:
                print("Couldn't delete file:", file_path)
