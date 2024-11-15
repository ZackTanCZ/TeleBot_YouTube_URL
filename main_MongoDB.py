# Python-telegram-bot Documentation 
# https://docs.python-telegram-bot.org/en/v21.7/index.html


# 13/11/2024 - Upload url into a DB?? mongoDB?
# https://github.com/python-telegram-bot/python-telegram-bot/wiki/Making-your-bot-persistent

# Import important libraries
import asyncio
import telegram
from telegram.ext import Application, Updater, CommandHandler, MessageHandler, filters, ContextTypes
import pymongo

# setup mongoDB Database - Connect using Local host for now
client = pymongo.MongoClient("CONNECTION_STRING")
# In mongoDB, Database name is 'youtube_urls_db'
db = client["youtube_urls_db"]
# In mongoDB, Table (collection) name is 'youtube_urls'
collection = db["youtube_urls"]

# Replace 'YOUR_BOT_TOKEN' with your actual bot token from @botfather - This is static, keep secure
TOKEN = 'BOT_TOKEN'

# This library uses the 'async' keyword, which must be accompanied by the 'await' keyword
# Commands
# Run this command  when the user types '/start'
async def on_start(update, context):
    # Simply return a reply message to the user
    await update.message.reply_text('Welcome to your Gym Video List! Key in /display to browse your listings.')

# Run this command  when the user types '/display' 
# Display a list of Youtube URLs with their associated unique Id - ID: XX - URL: XX
async def display_urls(update, context):
    # It retrieves all documents (via .find()) from the collection
    urls = collection.find()
    
    # Check if collection is empty
    if (collection.count_documents({}) == 0):
        await update.message.reply_text('No Youtube URLs found.\nConsider adding one with the add command') 
    else:
    # if collection is not empty, display all documents in a formatted string
        for_str = 'Youtube URLS:\n'
        for url in urls:
            for_str += f"ID: {url['id']} - URL: {url['url']}\n"
        await update.message.reply_text(for_str) 

# Run this command  when the user types '/add XX'
# Adds the Youtube URL into the collection (youtube_urls) in MongoDB
async def add_url(update, context):
    # extracts the Youtube Url from the user input using split function
    url = update.message.text.split(' ')[1]

    # Check for youtube urls - if valid, add the document {'id': uni_id, 'url':url} into the collection with a auto-incremental ID 
    # Optional: Check if the Youtube Vid is a short or full length video - split further and extract required string
    if 'https://www.youtube.com' in url:
        await update.message.reply_text('Valid Youtube URL')
    # Unique ID should be based on number of documents (in the collection) + 1
        uni_id = int(collection.count_documents({})) + 1
        collection.insert_one({'id':uni_id, 'url':url})
        await update.message.reply_text('Youtube URL added into mongoDB')  
    else:
    # else, display error message
        await update.message.reply_text('Invalid Youtube URL')
    await display_urls(update, context)

# Run this command  when the user types '/del XX'
# Removes the document from the collection based on the extracted id
async def del_url(update, context):
    # Extract the id of the document to delete - del_id
    del_id = update.message.text.split(' ')[1]
    # '/del all' delete all documents from the collection
    if (del_id.lower() == 'all'):
        collection.delete_many({})
    else:
    # Implement Try.. except for cases like '/del abc'
        try:    
            del_id = int(del_id)
    # if del_id is not found in the collection
            if collection.count_documents({'id':del_id}) == 0:
                await update.message.reply_text(f'ID {del_id} is not found.')
            else:
    # if del_id is found, remove the document from the collection    
                collection.delete_one({'id':del_id})
                await update.message.reply_text(f'ID {del_id} has been deleted')
        except (TypeError, ValueError):
            await update.message.reply_text('Please key in valid Integer ID')

    await display_urls(update, context)    


if __name__ == '__main__':
    print('Starting Telegram Bot right now!')
    
    # Creates an entity to handle all the inner working of the bot
    app = Application.builder().token(TOKEN).build()

    # Add Handler to run commands
    # Run the command 'on_start' when user keys in '/start'
    app.add_handler(CommandHandler('start', on_start))

    # Run the command 'add_url' when the user keys in '/add url'
    app.add_handler(CommandHandler('add', add_url))

    # Run the command 'del_url' when the user keys in '/del id'
    app.add_handler(CommandHandler('del', del_url))

    # Run the command 'display_urls' when the user keys in '/display' 
    app.add_handler(CommandHandler('display', display_urls))

    # Indicate how often you want to check for updates in telegram
    print('Bot is polling...')
    app.run_polling(poll_interval = 3)


