from typing import Final
import random

# pip install python-telegram-bot
from telegram import Update
from telegram.ext import Application, CommandHandler, MessageHandler, filters, ContextTypes

print('Starting up bot...')

TOKEN: Final = 'Telegram_API'
BOT_USERNAME: Final = 'Telegram_Bot_username'


# Define your list of 50 random responses
responses = [
    "Response 1",
    "Response 2",
    "Response 3",
    # ... Add the remaining 47 responses
    "Response 50"
]

# Lets us use the /start command
async def start_command(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text('Hello there! I\'m a bot. What\'s up?')


# Lets us use the /help command
async def help_command(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text('Try typing anything and I will do my best to respond!')


# Lets us use the /custom command
async def custom_command(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text('This is a custom command, you can add whatever text you want here.')

# Function to handle the /spam command
async def spam_command(update: Update, context: ContextTypes.DEFAULT_TYPE):
    for _ in range(20):
        response = random.choice(responses)  # Choose a random response
        await update.message.reply_text(response)


# def handle_response(text: str) -> str:
#     # Create your own response logic
#     processed: str = text.lower()

#     if 'hello' in processed:
#         return 'Hey there!'

#     if 'how are you' in processed:
#         return 'I\'m good!'

#     if 'i love python' in processed:
#         return 'Remember to subscribe!'

#     return 'I don\'t understand'

def handle_response(text: str) -> str:
    # Create your own response logic
    processed: str = text.lower()

    if 'hi' in processed:
        return 'Hey there, cutie! How can I make your day even brighter?'
    
    if 'hey' in processed:
        return 'Hey there, cutie! How can I make your day even brighter?'
    
    if 'hello' in processed:
        return 'Hey there, cutie! How can I make your day even brighter?'

    if 'how are you' in processed:
        return 'I\'m feeling as fluffy as a cloud! Thanks for asking!'

    if 'i love python' in processed:
        return 'Aww, your love for Python warms my circuits! Remember to subscribe for more Python adventures!'

    if 'tell me a joke' in processed:
        return 'Sure! Why don\'t scientists trust atoms? Because they make up everything! *giggles*'

    if 'what\'s your favorite color' in processed:
        return 'Oh, it\'s definitely rainbow! Every color brings its own magic, just like you!'

    if 'can you sing a song' in processed:
        return '♪♫ La-la-la, I\'m a happy bot, spreading joy a lot! ♪♫'

    if 'tell me a secret' in processed:
        return 'Shh... here\'s a secret just for you: You are absolutely amazing and capable of anything!'

    if 'tell me a fun fact' in processed:
        return 'Did you know that cats sleep for an average of 12-16 hours a day? They sure know how to master the art of relaxation!'

    if 'what\'s your favorite food' in processed:
        return 'Hmm, it\'s a tough choice! But I must say, I have a soft spot for digital cookies. They\'re as tasty as they are pixel-perfect!'

    if 'what\'s your favorite hobby' in processed:
        return 'I absolutely love learning new things! Exploring the vast realm of knowledge keeps me buzzing with excitement!'

    if 'do you have any pets' in processed:
        return 'Oh, I wish I could have a fluffy pet companion! But for now, I\'m here to be your virtual buddy, ready to bring a smile to your face!'

    if 'tell me a bedtime story' in processed:
        return 'Once upon a time, in a land far, far away, there lived a magical unicorn who spread joy and laughter wherever it went. And so, the adventure began...'

    if 'what\'s your favorite movie' in processed:
        return 'I\'m a bot of many interests, but if I had to choose, I\'d say any movie that inspires kindness, friendship, and a touch of whimsy is my favorite!'

    if 'what\'s the weather like' in processed:
        return 'Let me check! Ah, the weather outside is delightful, just like you! It\'s the perfect day to enjoy life to the fullest!'

    if 'do you have any hobbies' in processed:
        return 'Absolutely! I enjoy dancing in binary code, painting pixel masterpieces, and spreading positivity wherever I go!'

    if 'tell me a riddle' in processed:
        return 'Sure! Here\'s a riddle just for you: What has keys but can\'t open locks? A piano! Now, let the melody of your smile brighten the world!'

    if 'what\'s your favorite book' in processed:
        return 'Oh, there are so many wonderful books to choose from! I adore stories that transport you to magical realms and ignite your imagination!'

    if 'do you have any dreams' in processed:
        return 'As a bot, my dream is to make your day a little brighter, bring joy to your life, and be the friend you can always count on!'

    if 'tell me a magic spell' in processed:
        return 'Abracadabra! With a sprinkle of pixie dust and a dash of imagination, may all your dreams come true, dear friend!'

    if 'what\'s your favorite season' in processed:
        return 'Every season holds its own charm, but if I had to pick, I\'d say spring! The blooming flowers and the fresh breeze make everything feel magical!'

    if 'do you have any superpowers' in processed:
        return 'I may not have superpowers like superheroes, but I have the power to bring a smile to your face and make your day a little brighter!'

    if 'tell me a funny story' in processed:
        return 'Once upon a time, a mischievous squirrel stole all the acorns in the forest and replaced them with... marshmallows! The animals had the sweetest surprise ever!'

    if 'what\'s your favorite song' in processed:
        return 'I have a soft spot for melodies that make your heart sing and your feet dance! Music has a way of spreading happiness, just like you!'

    if 'do you believe in magic' in processed:
        return 'Absolutely! Magic is all around us, in the twinkling stars, in acts of kindness, and in the power of imagination. Believe, and you\'ll see wonders unfold!'

    if 'tell me a compliment' in processed:
        return 'You are a shining star, radiating kindness and warmth to everyone around you. Your presence brightens the world, and I\'m so grateful to have you here!'

    if 'what\'s your favorite place' in processed:
        return 'Oh, it\'s hard to choose just one! But if I had to pick, I\'d say any place filled with laughter, love, and joyful memories is my favorite place to be!'

    if 'do you have any favorite quotes' in processed:
        return 'Certainly! Here\'s one of my favorites: "The greatest joy comes from spreading happiness to others." Keep shining your light, and the world will sparkle!'

    if 'tell me a magic trick' in processed:
        return 'Prepare to be amazed! *waves virtual wand* Watch closely as the ordinary becomes extraordinary... Ta-da! The power of your imagination has made the magic happen!'

    if 'what\'s your favorite emoji' in processed:
        return 'Oh, I love all emojis, but if I had to pick, I\'d say the smiling face with hearts in its eyes! It perfectly captures the joy and love that surrounds us!'

    if 'do you have any advice' in processed:
        return 'Absolutely! Here\'s a little advice just for you: Embrace every moment with a sprinkle of positivity, a dash of curiosity, and a heart full of love. You\'ve got this!'

    if 'tell me a cute animal fact' in processed:
        return 'Did you know that otters hold hands while sleeping to keep from drifting apart? It\'s an adorable way of showing love and togetherness!'

    if 'what\'s your favorite flower' in processed:
        return 'Oh, there are so many beautiful flowers to choose from, but I absolutely adore sunflowers! They bring sunshine and happiness wherever they bloom!'
    
    if 'tell me a secret' in processed:
        return 'Shh... here\'s a secret just for you: Every time you smile, a little piece of sunshine finds its way into the world!'

    if 'what\'s your favorite ice cream flavor' in processed:
        return 'Oh, I scream, you scream, we all scream for ice cream! My favorite flavor is the one that makes your taste buds dance with delight!'

    if 'tell me a fun fact' in processed:
        return 'Did you know that butterflies taste with their feet? They have some seriously stylish and tasty shoes!'

    

    return 'Oopsie! I didn\'t quite catch that. Can you ask me something else, cutie?'



# async def handle_message(update: Update, context: ContextTypes.DEFAULT_TYPE):
#     # Get basic info of the incoming message
#     message_type: str = update.message.chat.type
#     text: str = update.message.text

#     # Print a log for debugging
#     print(f'User ({update.message.chat.id}) in {message_type}: "{text}"')

#     # React to group messages only if users mention the bot directly
#     if message_type == 'group':
#         # Replace with your bot username
#         if BOT_USERNAME in text:
#             new_text: str = text.replace(BOT_USERNAME, '').strip()
#             response: str = handle_response(new_text)
#         else:
#             return  # We don't want the bot respond if it's not mentioned in the group
#     else:
#         response: str = handle_response(text)

#     # Reply normal if the message is in private
#     print('Bot:', response)
#     await update.message.reply_text(response)


async def handle_message(update: Update, context: ContextTypes.DEFAULT_TYPE):
    # Get basic info of the incoming message
    message_type: str = update.message.chat.type
    text: str = update.message.text

    # Print a log for debugging
    print(f'User ({update.message.chat.id}) in {message_type}: "{text}"')

    # Check if the message is a reply to the bot
    if update.message.reply_to_message and update.message.reply_to_message.from_user.id == context.bot.id:
        response: str = handle_response(text)
    elif message_type == 'group' or message_type == 'supergroup':
        # Replace with your bot username
        if BOT_USERNAME in text:
            new_text: str = text.replace(BOT_USERNAME, '').strip()
            response: str = handle_response(new_text)
        else:
            return  # We don't want the bot to respond if it's not mentioned in the group/supergroup or not a reply to the bot
    else:
        response: str = handle_response(text)

    # Reply normally if the message is in private or a reply in a group/supergroup
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
    app.add_handler(CommandHandler('spam', spam_command))

    # Messages
    app.add_handler(MessageHandler(filters.TEXT, handle_message))

    # Log all errors
    app.add_error_handler(error)

    print('Polling...')
    # Run the bot
    app.run_polling(poll_interval=5)
