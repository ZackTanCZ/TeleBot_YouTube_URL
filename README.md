# TeleBot_Youtube_URL

## The Premise
Ever find yourself chancing upon an interesting Youtube video which peaked your interest on the Youtube App, and you would like to visit at a later timing? Rather than going through the tedious process of setting a Youtube playlist to store these videos on the Youtube app. Don't you wish there was a simple and convenient way to store and manage these video urls, with the use of simple commands such as /add (to add), /del (to remove), /display (show all urls). The icing on the cake is if these functions are made available on a popular messaging platform.

The above scenario is the premise of this bot, offering an simple and convenient way to collect Youtube URLs to view in the future. It is integerated into `Telegram` - a popular mobile app with many functions - through Telegram's official API and scripted in `Python` with the [Python-Telegram-Bot](https://python-telegram-bot.org/) Library. There are several use cases for this bot such as a Gym playlist or White noise playlist

## Bot Features - More to be added
* /start - Start the bot and displays a welcome message
* /display - Display a list of stored Youtube URL
* /add (URL) - Adds a Youtube URL into storage 
* /del (ID) - Removes a Youtue URL from storage
* /del all - Removes all Youtube URL from storage

## main_list.py
This script file contains the codebase for the Telegram bot. Currently, the URLs are stored in a non-persistent Python list, meaning they are lost whenever the bot is restarted. This initial version serves as a proof of concept for testing the bot's functionality.

## main_MongoDB.py
To enhance the bot's persistence, a NoSQL database, specifically `MongoDB`, will be integrated in this iteration. [MongoDB](https://www.mongodb.com/docs/manual/reference/method/js-collection/) is a popular, free, and highly flexible database known for its speed and performance. The [PyMongo](https://www.mongodb.com/resources/languages/mongoengine-pymongo) library will be utilized to facilitate interaction between the bot and the MongoDB database. This integration will ensure that the list of YouTube URLs is stored persistently, even after the bot is restarted. In this iteration, MongoDB is ran locally with MongoCompass by connecting to the localhost (i.e. Data only persist when MongoCompass is running)

## Future Works
To ensure continuous operation of the bot, it is necessary to deploy it to a hosting platform. This involves hosting both the Python script and the MongoDB database on separate platforms.

Platforms for Consideration:
* `MongoDB` [MongoDB Atlas](https://cloud.mongodb.com/v2/6736f07f33b7a4212f94707c#/host/replicaSet/6736f23d3dfe6a1dbe0e97dd)
* `Python Scipt` [PythonAnyWhere](https://www.pythonanywhere.com/) | [AWS Lambda](https://aws.amazon.com/lambda/?did=ft_card&trk=ft_card) | [Render]()

