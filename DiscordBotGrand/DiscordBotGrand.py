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
intents.reactions = True
intents.members = True
intents.message_content = True

#Channels
RulesChannelID = 1401264705644793896
CRulesChannelID = 1397800833025839175

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
            await channel.send(f'{member.mention} Welcome to City of Steel! Please read <#{RulesChannelID}> for server rules and then go to <#{CRulesChannelID}> for how to make your character!')
            await member.add_roles(role)
    else:
        print("Error: Role does not exist!")

@bot.command()
async def pingforrp(ctx):
    role = discord.utils.get(ctx.guild.roles, name="Ping For Rp")
    print("Here we go again")

    if role in ctx.author.roles:
        await ctx.author.remove_roles(role)
        await ctx.author.send(f"Removed {role.name}")
    else:
        await ctx.author.add_roles(role)
        await ctx.author.send(f"Added {role.name}")


@bot.command()
async def test(ctx):
    channel = bot.get_channel(1401735682183135374)
    print(channel)
    if channel:
        await channel.send('You were never meant to find this...')


bot.run(token, log_handler=handler, log_level=logging.DEBUG)

