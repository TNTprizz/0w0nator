################################
# bot.py written by TNTprizz
# Change it cuz the code is trash
################################
# Imports
import discord
import os

intents = discord.Intents().all
# Ready to be defineddddddddd
default_prefixes = ['~']

# For changing prefix
async def determine_prefix(bot, message):
    guild = message.guild # Get the guild so that cannot change prefix in DMChannel
    if guild: # If it is not the DMChannel
        return bot.custom_prefixes.get(guild.id, default_prefixes) # Get prefix from the bot.custom_prefixes variable
    else: # If it is a DMChannel
        return default_prefixes # Return the default prefix

bot = discord.Bot(command_prefix=determine_prefix, intents=intents)

# Import the cogs when the bot is ready (N/A)
@bot.event
async def on_ready(): # Define the function
  for filename in os.listdir('./cogs'): # List all the files in ~/src/cogs
    if filename.endswith('.py'): # If file is a python file
      print("Loaded cog " + filename[:-3] + " from file: " + filename) # Output to terminal
      bot.load_extension(f'cogs.{filename[:-3]}') # Import the Cogs
  print("Bot online!") # Output to terminal if the whole thing is completed

token = open("../E.key","r+") # Open and prepare to read ~/E.key
bot.run(token.read()) # Run the bot with the content of ~/E.key
# P.S. You need to touch the ~/E.key and store your bot token in it. Don't ask me anymore!
token.close()
# Close the object to save resources