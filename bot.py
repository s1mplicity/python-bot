import discord
from discord.ext import commands
TOKEN = 'BOT_TOKEN_HERE'
bot = commands.Bot(command_prefix='??')


@bot.event
async def on_ready():
    print(f'Logged in as: {bot.user.name}')
    print(f'With ID: {bot.user.id}')
    print(f'Bot is online')


@bot.command()
async def ping(ctx):
    await ctx.send('pong')


bot.run(TOKEN)