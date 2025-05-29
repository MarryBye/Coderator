import discord

from discord.ext import commands
from discord import app_commands

from core.config import Config
from core.integrations.gemini import gemini_client
from core.integrations.database import get_database_session

intents = discord.Intents.all()
bot = commands.Bot(command_prefix="!", intents=intents)

tree = bot.tree

@bot.event
async def on_ready():
    await tree.sync()
    print(f"Logged in as {bot.user} (ID: {bot.user.id})")
    print("------")

@bot.event
async def on_message(message: discord.Message):
    if message.author == bot.user:
        return
    
    generated_content = gemini_client.generate_text(message.content)
    text = generated_content.parts[0].text if generated_content.parts else "Не удалось сгенерировать ответ."
    await message.reply(text)

@tree.command(name="ping", description="Проверка бота")
async def ping(ctx: discord.Interaction):
    await ctx.response.send_message("Pong!")
    
bot.run(Config.BOT_TOKEN)
