from typing import Final

# pip install python-telegram-bot
from telegram import Update,ReplyKeyboardMarkup, KeyboardButton, WebAppInfo, InlineKeyboardButton, InlineKeyboardMarkup
from telegram.ext import Application, CommandHandler, MessageHandler, filters, ContextTypes, CallbackContext, Updater, CallbackQueryHandler



print('Welcome to Code hunt from Computer Science Department')

TOKEN: Final = '6021110506:AAFWuNu97QdOd1biau7ZgDSF1B-bSKBWOVw'
BOT_USERNAME: Final = '@jcr102000bot'


help = "Feel free to use the help command anytime for asking any doubts and clearing any queries \n \start - To start the bot \n \contact- contact one our team member"
incorrect_answer = "Oops..Incorrect. try again by clicking on the answer button again"
# Lets us use the /start command
async def start_command(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text('Welcome to Code hunt from Computer Science Department')


# Lets us use the /help command
async def help_command(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text(help)


# Lets us use the /custom command
async def custom_command(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text('This is a custom command, you can add whatever text you want here.')
    
    
    
    
async def get_leaderboard(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text('This is the Leaderboard')
    
async def get_question1(update: Update, context: ContextTypes.DEFAULT_TYPE):
   
    question = "How big is his dick?" 
    keyboard = [[InlineKeyboardButton("ANSWER", switch_inline_query_current_chat="q12345: ")]]
    reply_markup = InlineKeyboardMarkup(keyboard)
    try:
        await update.message.reply_text(question, reply_markup=reply_markup)
    except:
        print('error')
        

        
def handle_callback(update: Update, context: CallbackContext):
    query = update.callback_query
    data = query.data
    print('query data',data)
    

def handle_response(text: str) -> str:
    # Create your own response logic
    processed: str = text.lower()
    
    user_response = processed.split(':')
    answer = user_response[1]
    questionId = user_response[0]
    
    
    if questionId in processed:
        if 'small' in answer:
            return "correct answer"
        else:
            return incorrect_answer

    if 'hello' in processed:
        return 'Hey Mf nikhil!'

    if 'how are you' in processed:
        return 'I\'m good!'

    if 'i love python' in processed:
        return 'Remember to subscribe!'
    
    

    return 'I don\'t understand'


async def handle_message(update: Update, context: ContextTypes.DEFAULT_TYPE):
    # Get basic info of the incoming message
    message_type: str = update.message.chat.type
    text: str = update.message.text

    # Print a log for debugging
    print(f'User ({update.message.chat.id}) in {message_type}: "{text}"')

    # React to group messages only if users mention the bot directly
    if message_type == 'group':
        # Replace with your bot username
        if BOT_USERNAME in text:
            new_text: str = text.replace(BOT_USERNAME, '').strip()
            response: str = handle_response(new_text)
        else:
            return  # We don't want the bot respond if it's not mentioned in the group
    else:
        response: str = handle_response(text)

    # Reply normal if the message is in private
    print('Bot:', response)
    await update.message.reply_text(response)
    
    



# Log errors
async def error(update: Update, context: ContextTypes.DEFAULT_TYPE):
    print(f'Update {update} caused error {context.error}')


# Run the program
if __name__ == '__main__':
    app = Application.builder().token(TOKEN).build()

    # Commands
    app.add_handler(CommandHandler('start', start_command))
    app.add_handler(CommandHandler('help', help_command))
    app.add_handler(CommandHandler('custom', custom_command))
    app.add_handler(CommandHandler('leaderboard', get_leaderboard))
    # app.add_handler(CommandHandler('question', get_question))
    app.add_handler(CommandHandler('q', get_question1))


    # Messages
    app.add_handler(MessageHandler(filters.TEXT, handle_message))

    # Log all errors
    app.add_error_handler(error)
    
    app.add_handler(CallbackQueryHandler(handle_callback))

    print('Polling...')
    # Run the bot
    app.run_polling(poll_interval=5)
