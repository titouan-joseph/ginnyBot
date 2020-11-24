import discord
from discord.ext import commands
import os
import Cogs

TOKEN = os.getenv("BOT_TOKEN")
PREFIX = "!"

bot = commands.Bot(command_prefix=PREFIX, description="Bot de l'ASTUS")


@bot.event
async def on_ready():
    await bot.change_presence(activity=discord.Game(name="Help"))

    print(f'{bot.user} has connected to Discord!')


@bot.command()
async def load(ctx, name=None):
    try:
        bot.load_extension(name)
        await ctx.send(name + "load")
    except:
        await ctx.send(name + " has has already up")
    else:
        raise discord.ext.commands.CheckFailure


@bot.command()
async def unload(ctx, name=None):
    try:
        bot.unload_extension(name)
        await ctx.send(name + " unload")
    except:
        await ctx.send(name + " has has already down")
    else:
        raise discord.ext.commands.CheckFailure


@bot.command()
async def reload(ctx, name=None):
    try:
        bot.reload_extension(name)
        await ctx.send(name + " reload")
    except:
        bot.load_extension(name)
        await ctx.send(name + " load")
    else:
        raise discord.ext.commands.CheckFailure


if __name__ == '__main__':
    # cogs
    bot.load_extension("Cogs.ginny")

    bot.run(TOKEN)
