# Python-telegram-bot Documentation 
# https://docs.python-telegram-bot.org/en/v21.7/index.html

# Import important libraries
import asyncio
import telegram
from telegram.ext import Application, Updater, CommandHandler, MessageHandler, filters, ContextTypes


# Replace 'YOUR_BOT_TOKEN' with your actual bot token from @botfather - This is static, keep secure
TOKEN = 'BOT_TOKEN'

# This library uses the 'async' keyword, which must be accompanied by the 'await' keyword
# Commands
# Run this command  when the user types '/start'
async def on_start(update, context):
    # Simply return a reply message to the user
    await update.message.reply_text('Welcome to your Gym Video List! Key in /display to browse your listings.')

# Run this command  when the user types '/add'
# Remember that url_List is an global variable
async def add_url(update, context):
    # retain the Youtube Url from the user input using split function
    url = update.message.text.split(' ')[1]

    # Check for youtube urls - if valid, add into a list with a auto-incremental ID
    # Optional: Check if the Youtube Vid is a short or full length video - split further and extract required string
    if 'https://www.youtube.com' in url:
        await update.message.reply_text('Valid Youtube URL')
        # Unique ID should be based on len(url_List) + 1
        uni_id = len(url_List) + 1
        url_List.append([uni_id, url])
        await update.message.reply_text('URL has been added into the list')        
    else:
        # else, display error message
        await update.message.reply_text('Invalid Youtube URL')
    await display_urls(update, context)

# Run this command  when the user types '/display' 
# Display a formatted list of Youtube URLs with their associated unique Id
# ID: XX - URL: XX
async def display_urls(update, context):
    if not url_List: # Check if the list is empty 
        await update.message.reply_text('No URLs to display.') 
        print('URL list is empty.') 
        return

    for_str = ''
    for i in url_List:
        url_id, url_str = i[0], i[1]
        for_str += f'ID: {url_id} - URL: {url_str}\n'

    # Ensure that for_str is not empty before sending the message 
    if for_str: 
        await update.message.reply_text(for_str) 
    else: 
        await update.message.reply_text('No URLs to display.')
            
# Run this command  when the user types '/del XX'
# Removes the record based on the extracted id
async def del_url(update, context):
    # Add a counter to check del_id exist
    deleted = False
    del_id = int(update.message.text.split(' ')[1])
    for i in url_List:
        if i[0] == del_id :
            url_List.remove(i)
            deleted = True
            await update.message.reply_text(f'ID {del_id} has been deleted')            
    if not deleted:
        await update.message.reply_text(f'ID {del_id} not found.')
    await display_urls(update, context)
         

if __name__ == '__main__':
    print('Starting Telegram Bot right now!')
    
    # Is this suppose to create the bot??
    app = Application.builder().token(TOKEN).build()

    # Initialise an empty list to store URL
    url_List = []

    # Add Handler to run commands
    # Run the command 'on_start' when user keys in '/start'
    app.add_handler(CommandHandler('start', on_start))

    # Run the command 'add_url' when the user keys in '/add url'
    app.add_handler(CommandHandler('add', add_url))

    # Run the command 'del_url' when the user keys in '/del XX'
    app.add_handler(CommandHandler('del', del_url))

    # Run the command 'display_urls' when the user keys in '/display' 
    app.add_handler(CommandHandler('display', display_urls))

    # Indicate how often you want to check for updates in telegram
    print('Bot is polling...')
    app.run_polling(poll_interval = 3)














