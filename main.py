import discord
from discord.ext import commands
from discord import app_commands

from core.config import Config

intents = discord.Intents.all()
bot = commands.Bot(command_prefix="!", intents=intents)

tree = bot.tree

@bot.event
async def on_ready():
    await tree.sync()  # Синхронизируем команды с Discord API
    print(f"Logged in as {bot.user} (ID: {bot.user.id})")
    print("------")

# Слэш-команда
@tree.command(name="ping", description="Проверка бота")
async def ping(ctx: discord.Interaction):
    await ctx.response.send_message("Pong!")
    
bot.run(Config.BOT_TOKEN)