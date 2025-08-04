import discord
from discord import guild
from discord.ext import commands
import logging
from dotenv import load_dotenv
import os

load_dotenv()
token = os.getenv("DISCORD_TOKEN")

handler = logging.FileHandler(filename='Discord.log', encoding='utf-8', mode='w')

intents = discord.Intents.default()
intents.messages = True
intents.members = True
intents.message_content = True


bot = commands.Bot(command_prefix="!", intents=intents)
@bot.event
async def on_ready():
    print(f"Hello, IT IS I {bot.user.name}")

@bot.event
async def on_member_join(member):
    role = discord.utils.get(member.guild.roles, name="No character")
    
    if role:
        channel = bot.get_channel(1397798125044895777)
        if channel:
            await member.add_roles(role)
            await channel.send(f'{member.author.message} Welcome to City of steel glad you could make it!')
    else:
        print("Error: Role does not exist!")

@bot.command()
async def test(ctx):
    print("Fired Test")
    channel = bot.get_channel(1401735682183135374)
    print(channel)
    if channel:
        await channel.send('Welcome to City of steel glad you could make it!')

bot.run(token, log_handler=handler, log_level=logging.DEBUG)

