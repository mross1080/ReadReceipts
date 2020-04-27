#!/usr/bin/env python3

from telethon import TelegramClient, events, sync
api_id = 'my_api_id'
api_hash = 'my_api_hash'
my_user_id = 'my_user_id'
mqtt_topic = "topic/readreceipts/" + str(my_user_id)


from telethon.sync import TelegramClient, events

current_conversations = {}

import paho.mqtt.client as mqtt

def on_connect(client, userdata, flags, rc):
    print("Connected with result code " + str(rc))
    # client.subscribe("arduino/simple")


def on_message(client, userdata, msg):
    print("Message Recieved \n {}".format(msg.payload))
    # client.disconnect()
mqtt_client = mqtt.Client()
mqtt_client.connect("54.204.183.201", 1883, 60)
mqtt_client.on_connect = on_connect
mqtt_client.on_message = on_message
mqtt_client.loop_start()


with TelegramClient('session1', api_id, api_hash) as client:
    # msgs = client.get_messages('me')
    # print(msgs)
    print("connected and waiting for messages")


    @client.on(events.NewMessage(pattern='.*'))
    async def handler(event):

        try:
            print("Currently Monitoring Messages for User {}".format(my_user_id))
            from_id = event.message.from_id
            chat_id = event.message.chat_id
            print("got message from {}".format(from_id))
            print("Chat ID : {}".format(event.message.chat_id))

            # If the Incomign ID Is not from Matt, that means it's from someone else and we need to update the state
            if (from_id != my_user_id):

                # If this is a new chat, then we need to add it to the list of current conversations
                if chat_id not in current_conversations.keys():
                    current_conversations[chat_id] = "waiting"

                current_conversations[chat_id] = "waiting"
                mqtt_client.publish(mqtt_topic, "0");

            else:
                print("SENDING MESSAGE TO COUNTDOWN")
                # This is as text coming from Matt, Tell the Client to start Counting Down
                mqtt_client.publish(mqtt_topic, "1");

                current_conversations[chat_id] = "idle"

            # # print(x)
        except Exception as e:
            print("Exception")
            print(e)

        print(event)
        print(event.message.text)

        await print("Done with message")


    client.run_until_disconnected()
