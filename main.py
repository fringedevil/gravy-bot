import os
import discord
import asyncio
import logging
import random
import sys
import time

from constants import *
from datetime import date, datetime, timedelta
from discord.ext import commands
from threading import Thread

logger = logging.getLogger()
logger.setLevel(logging.INFO)

ch = logging.StreamHandler(sys.stdout)
ch.setLevel(logging.INFO)
formatter = logging.Formatter('%(asctime)s - %(name)s - %(levelname)s - %(message)s')
ch.setFormatter(formatter)
logger.addHandler(ch)

TOKEN = os.environ.get('TOKEN')
enable_task = True
battle_seconds = 211977
whereru_seconds = 20177

bot = commands.Bot(command_prefix='!', description='A Gravy bot for the people')

def hasAttentionSpan():
    return random.random() > 0.2

def getGroupMembers(group):
    list = []
    members = bot.get_all_members()
    for member in members:
        if group in (r.name for r in member.roles):
            list.append(member)
    return list

@bot.event
async def on_ready():
    print('Logged in as')
    print(bot.user.name)
    print(bot.user.id)
    print('------')

    await bot.change_presence(activity=discord.Game(name="World of Warcraft, obviously"))

@bot.command()
async def hello(ctx):
    if hasAttentionSpan():
        await ctx.send(f'Yo {ctx.message.author.name}, keep it gangsta')
    else:
        await ctx.send(f'Yo {ctx.message.author.name}, -- spiders!!')

@bot.command()
async def gravy(ctx):
    if hasAttentionSpan():
        await ctx.send('Gravy for President!')
    else:
        await ctx.send('Spiders for President!')

@bot.command()
async def gravylife(ctx):
    if hasAttentionSpan():
        await ctx.send('My friends call me \'G\' because I was a dark gangster from Kimberly Drive. I had a Raiders trench coat that put Juice\'s trench coat to shame. I was OG, ya know.')
    else:
        await ctx.send('My friends call me...wait....spiders!!')

@bot.command()
async def playgame(ctx):
    if hasAttentionSpan():
        await ctx.send('INDIFFERENCE TO GAME!')
    else:
        await ctx.send('INDIFFERENCE TO....SPIDERS!')

@bot.command()
async def favoritemovie(ctx):
    if hasAttentionSpan():
        await ctx.send('Rush (with totally naked butts)')
    else:
        await ctx.send('Rush, with totally naked...hey, spiders!')

@bot.command()
async def trenchaf(ctx):
    if hasAttentionSpan():
        await ctx.send('https://media.giphy.com/media/cA7kvk12D4rvBeb4rR/giphy.gif')
    else:
        await ctx.send('https://media.giphy.com/media/26gsr8eaTjRiIxKgM/giphy.gif')

@bot.command()
async def gravybeerface(ctx):
    if hasAttentionSpan():
        await ctx.send('https://media.giphy.com/media/PNwk9K1FVvWyw1QDcz/giphy.gif')
    else:
        await ctx.send('https://media.giphy.com/media/QO9rT8VIOD9xS/giphy.gif')

@bot.command()
async def divinity(ctx):
    skill = DIVINITY_SKILLS[random.randint(0,DIVINITY_SKILLS.__len__())]
    await ctx.send(f'Hey, do you think I should get {skill}? {DIVINITY_WIKI_URL}{skill.replace(" ","+")}')

@bot.command()
async def config(ctx):
    global enable_task, battle_seconds, whereru_seconds

    parts = ctx.message.split(' ')
    if len(parts) < 3:
        embed = discord.Embed(title="Gravy Bot Config", description="List of configurations are:", color=0xeee657)

        embed.add_field(name="!config tasks on|off", value="Enable or disable background tasks", inline=False)
        embed.add_field(name="!config battle <seconds>", value="Set the number of seconds before Gravy craves battle", inline=False)
        embed.add_field(name="!config where <seconds>", value="Set the number of seconds before Gravy loses track of you", inline=False)

        await ctx.send(embed=embed)
    else:
        setting = parts[1].lower()
        value = parts[2]

        if setting != "tasks":
            try:
                value = int(parts[2])
            except ValueError:
                await ctx.send(f'!config {parts[1]} <value> must be an number')
                return
        
        if setting == 'tasks':
            enable_task = value == 'enable' or value == 'on' or value == 'true'
        if setting == 'battle':
            battle_seconds = value
        if setting == 'where':
            whereru_seconds = value
        await ctx.send(f'{parts[1]} set to {parts[2]}')
    
@bot.command()
async def info(ctx):
    if hasAttentionSpan():
        embed = discord.Embed(title="Gravy Bot", description="To get your daily gravy fix", color=0xeee657)

        # give info about you here
        embed.add_field(name="Author", value="fingedevil")

        # Shows the number of servers the bot is member of.
        embed.add_field(name="Server count", value=f"{len(bot.guilds)}")

        # Shows link to GitHub code
        embed.add_field(name="GitHub", value="https://github.com/fringedevil/gravy-bot")

        await ctx.send(embed=embed)
    else:
        embed = discord.Embed(title="Spider Bot", description="To get your daily spider fix", color=0xeee657)
        embed.add_field(name="Author", value="fingespider")
        embed.add_field(name="Spider count", value=f"{len(bot.guilds)}")
        embed.add_field(name="SpideyHub", value="https://github.com/fringedevil/gravy-bot")
        await ctx.send(embed=embed)

bot.remove_command('help')

@bot.command()
async def help(ctx):
    if hasAttentionSpan():
        embed = discord.Embed(title="Gravy Bot", description="MOAR Gravy!! List of commands are:", color=0xeee657)

        embed.add_field(name="!hello", value="Say hi to gravy-bot", inline=False)
        embed.add_field(name="!gravy", value="A vote of confidence for Gravy", inline=False)
        embed.add_field(name="!gravylife", value="The long and winding road to becoming Gravy", inline=False)
        embed.add_field(name="!playgame", value="Ask Gravy bot to play a game", inline=False)
        embed.add_field(name="!favoritemovie", value="Ask Gravy bot what his favorite movie is", inline=False)
        embed.add_field(name="!trenchaf", value="Gravy at peak performance", inline=False)
        embed.add_field(name="!gravybeerface", value="Vintage Gravy", inline=False)
        embed.add_field(name="!divinity", value="Gravy asks you about Divinity: Original Sin 2", inline=False)
        embed.add_field(name="!info", value="Details on the bot that is Gravy", inline=False)
        embed.add_field(name="!config", value="See instructions on configurating settings", inline=False)

        await ctx.send(embed=embed)
    else:
        embed = discord.Embed(title="Spidey Bot", description="MOAR Spiders!! List of spiders are:", color=0xeee657)

        embed.add_field(name="!hello", value="Say hi to spidey-bot", inline=False)
        embed.add_field(name="!gravy", value="A vote of spiders for Gravy", inline=False)
        embed.add_field(name="!gravylife", value="The long and winding road to becoming a spider", inline=False)
        embed.add_field(name="!playgame", value="Ask spidey bot to play a game", inline=False)
        embed.add_field(name="!favoritemovie", value="Ask Gravy bot what his favorite spider is", inline=False)
        embed.add_field(name="!trenchaf", value="Gravy at spiderman performance", inline=False)
        embed.add_field(name="!gravybeerface", value="Spider Gravy", inline=False)
        embed.add_field(name="!divinity", value="Gravy asks you about Divinity: Original Spider 2", inline=False)
        embed.add_field(name="!info", value="Details on the spider that is Gravy", inline=False)
        embed.add_field(name="!config", value="See instructions on configurating spiders", inline=False)

        await ctx.send(embed=embed)

async def idle_task():
    await bot.wait_until_ready()

    channel = discord.utils.get(bot.get_all_channels(), name='gravy')

    last_battle_dt = datetime.now()
    last_uplaying_dt = datetime.now()
    last_whereru_dt = datetime.now()

    while not bot.is_closed():
        now = datetime.now()

        # if config enabled and not while we're sleeping
        if not enable_task or now.hour < 8:
            continue

        # Gravy craves battle
        delta = now - last_battle_dt
        if delta.seconds > battle_seconds:
            last_battle_dt = datetime.now()
            msg = ''
            if random.random() < 0.5: # tag someone half the time
                members = getGroupMembers('divinity')
                target = members[random.randint(0,len(members))]
                msg = target.mention + ' '
            msg += GRAVY_BATTLE_QUOTES[random.randint(0,len(GRAVY_BATTLE_QUOTES))]
            await channel.send(msg)

        # where are you?
        delta = now - last_whereru_dt
        if delta.seconds > whereru_seconds:
            last_whereru_dt = datetime.now()
            members = getGroupMembers('divinity')
            members = [m for m in members if m.status == discord.Status.idle]
            target = members[random.randint(0,len(members))]
            await channel.send(f'Where are you? {target.mention}')
        
        # you playing tonight
        delta = now - last_uplaying_dt
        if delta.days > 0 and now.hour > 17:
            last_uplaying_dt = datetime.now()
            # tag a person, or use character name.
            # gravy does not use question marks
            if random.random() < 0.5:
                members = getGroupMembers('divinity')
                target = members[random.randint(0,len(members))]
                await channel.send(f'u playing tonite {target.mention}')
            else:
                target = DIVINITY_CHARS[random.randint(0,len(DIVINITY_CHARS))]
                await channel.send(f'u playing tonite {target.mention}')
        
        await asyncio.sleep(60) # task runs every 60 seconds
    print('idle_task() exit')

# Run watcher
bot.loop.create_task(idle_task())
# Run bot
bot.run(TOKEN)