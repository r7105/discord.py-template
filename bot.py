import discord.py
import discord.ext
import json
import dotenv
# open this repo in your prefered editor (VSCode, Intellij Idea, ect.) via cloning with url (requires GitHub Desktop) or whatever method you prefer and enter in the terminal `pip install -r requirements.txt`
# open the discord developer portal and go to bot and click reset token and proceed to copy the token and enter it in a new .env file as anything (example: `Token: INPUT-TOKEN`)
# Load environment variables from the .env file (replace `ENTER-.ENV-IDENTIFIER` with the identifier you set (as seen in the example Token)
load_dotenv()
TOKEN = os.getenv('ENTER-.ENV-IDENTIFIER')

# Create an instance of the bot
bot = commands.Bot(command_prefix='!')

# Event that runs when the bot is ready
@bot.event
async def on_ready():
    print(f'Bot is ready. Logged in as {bot.user.name} ({bot.user.id})')

# Command that responds with "Hello!" when a user types "!hello"
@bot.command(name='hello')
async def hello(interaction): # always enter `async def `commandname`(interaction):` after creating a @bot.command or anything else, this allows the bot to run the  
    await interaction.send('Hello!') # by entering `await` before making a message (aka interaction.send) this allows you to connect efficiently for after making the async

# Command that allows users to get the latency of the bot, sending a request to discord and getting the time in milliseconds it takes to get a responce via heartbeat
@bot.command(name='ping')
async def ping(interaction):
  latency = bot.latency  # Latency in seconds
  await interaction.send(f'Pong! {latency * 1000:.2f}ms')  # Convert to milliseconds and sends it

# Run the bot
if __name__ == '__main__':
    bot.run(TOKEN)
