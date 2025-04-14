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

bot.run("MTM1MDg5ODI1ODA4Nzc3NjMzOA.GHf6Ga.8_u8JoA7fzqts7K2U6YqXGfpKvC0P4b_v3EcyA")
