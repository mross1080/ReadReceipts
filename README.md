# Read receipts

Welcome to Read receipts, a new way to engage with your text conversations on Telegram.  There are a few steps to get started.  

First Step is to Download this repository onto your Computer.  

You need to install two libraries in order to get the application functioning.  Open the terminal then copy and paste the following commands one at a time.  

```
cd ~/Downloads/ReadReceipts-master
pip3 install telethon
pip3 install paho-mqtt

```

Cool! So you now have the necessary libraries installed.  So now what you need to do is get your application credentials from telegram.


In order to run the app, we need you to create an application and register it with Telegram and then get Two pieces of information a `api_id` and a `api_hash`.

The process is fairly simple though, follow the instructions below in order to obtain your `api_id` and `api_hash`
https://core.telegram.org/api/obtaining_api_id

Once you have these ids fill them in in the variables in the code of `waiting_for_responses_server.py`

```
from telethon import TelegramClient, events, sync
api_id = 'my_api_id'
api_hash = 'my_api_hash'

```

Now the next part is a little strange but necessary.  We need to get your User id.  You can do that by following this tutorial.  
https://bigone.zendesk.com/hc/en-us/articles/360008014894-How-to-get-the-Telegram-user-ID-

Then you can add your user id in the my_user_id field

```
from telethon import TelegramClient, events, sync
api_id = 'my_api_id'
api_hash = 'my_api_hash'
my_user_id = 'my_user_id'
```

We're almost there.  Then in the terminal, run this command to start the program
```
python3 waiting_for_responses_server.py
```

The program will start, and ask you to authenticate. You will enter your phone number and it will text you with a code which you will enter, once that is complete you will be good to go!

You can now head to

http://54.204.183.201:3000/myuserid

To activate the app!  Make sure you replace "my_user_id" with your actual telegram id!
