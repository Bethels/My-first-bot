from telegram.ext import Updater, CommandHandler, MessageHandler, Filters
import logging
import settings
FORMAT = '%(asctime)s - %(name)s - %(levelname)s - %(message)s'
logging.basicConfig(format=FORMAT, level=logging.INFO, filename='bot.log', )


def greet_user(update):
    text = 'User hit /start'
    update.message.reply_text(update.message)
    logging.info(text)


def talk_to_me(update, context):
    user_text = update.message.text
    text = f'Greetings, {update.message.chat.first_name}! You wrote "{update.message.text}"'
    print(update.message)
    logging.info(f'User: {update.message.chat.username}; Chat id: {update.message.chat.id}; '
                 f'Message: {update.message.text}')

    update.message.reply_text(text)


def main():
    mybot = Updater(settings.API_KEY, use_context=True)

    logging.info('Bot is starting')

    dp = mybot.dispatcher

    dp.add_handler(CommandHandler('start', greet_user))
    dp.add_handler(MessageHandler(Filters.text, talk_to_me))

    mybot.start_polling()
    mybot.idle()


main()
