from telegram import Update,KeyboardButton,ReplyKeyboardMarkup
from telegram.ext import ApplicationBuilder,MessageHandler,CommandHandler,filters,ContextTypes


TOKEN = "8947236769:AAHnUXUSoO5o5vw-yf0VLvkae0USkK16hBM"

step,name,surename,midname = range(4)


async def start(update:Update,context:ContextTypes.DEFAULT_TYPE):
    global step
    step = "just_menu"

    # Making a keyboard
    keyboard = ReplyKeyboardMarkup([
        [KeyboardButton(text="Registration")],
        [KeyboardButton(text="Information")]
    ],resize_keyboard=True)

    # Printing here
    await update.message.reply_text("Choose on of the options",reply_markup=keyboard)


async def main(update:Update,context:ContextTypes.DEFAULT_TYPE):
    global step,name,surename,midname
    text = update.message.text
    if step == "just_menu":
        if text == "Registration":
            await update.message.reply_text("Enter your name:")
            step = "get_name"


    elif step == "get_name":
            name = update.message.text
            await update.message.reply_text("Enter your sure name:")
            step = "get_sure_name"


    elif step == "get_sure_name":
            surename = update.message.text
            await update.message.reply_text("Enter your middle name:")
            step = "get_middle_name"


    elif step == "get_middle_name":
            midname = update.message.text
            await update.message.reply_text(f"Your information collected:\n    Name:{name}\n    Sure name:{surename}\n    Middle name:{midname}")
            step = "over"

    elif text == "Information":
        await update.message.reply_text("This bot is just a bot")

    else:
        await update.message.reply_text("Choose on of the buttons")


if __name__ == "__main__":
    app = ApplicationBuilder().token(TOKEN).build()
    app.add_handler(CommandHandler("start",start))
    app.add_handler(MessageHandler(filters.TEXT & ~filters.COMMAND,main))
    print("It's working now...")
    app.run_polling()
    print("It's done now!")