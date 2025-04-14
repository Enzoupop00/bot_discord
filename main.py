import discord
from discord.ext import commands

intents = discord.Intents.default()
intents.message_content = True  # Nécessaire si tu veux lire les messages

bot = commands.Bot(command_prefix="!",intents=intents)

@bot.event
async def on_ready():
    print(f"Bot connecté en tant que {bot.user}")

@bot.command()
async def ping(ctx):
    await ctx.send("Pong!")

bot.run("MTM1MDg5ODI1ODA4Nzc3NjMzOA.GGZfBx.TXBxjmzjP80VBWRvqgvdjS9wJJv-2wi6BKb-ak")
