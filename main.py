import discord
import json
import random
import asyncio
import time

from discord.ext import commands
from discord.utils import get
from datetime import datetime, timedelta
from discord_components import DiscordComponents, Button, ButtonStyle, InteractionType, Select, SelectOptions

from csgo_api import CSGOStats

import keep_alive

client = commands.Bot(command_prefix="cs!", help_command=None)

@client.event
async def on_ready() :
    time=datetime.now()
    print("------\nBot Connecté\nRappelBump\n"+str(client.user.id)+"\nBot lancé le "+str(time.strftime("%d-%m-%Y à %H:%M:%S")+"\n------"))

    await client.change_presence(activity=discord.Activity(type=discord.ActivityType.watching, name="cs!help"))

@commands.cooldown(1, 2, commands.BucketType.user)
@client.command()
async def help(ctx):
	emojiFromServer = client.get_emoji(874278287143223326)
	emojiFromServer2 = client.get_emoji(874279294296293387)
	with open("extra.json", "r") as ex:
		data = json.load(ex)

	for i in range(len(data["prefix"])):
		if list(data["prefix"][i].keys())[0] == str(ctx.message.guild.id):
			prefixe = data["prefix"][i][str(ctx.guild.id)]
			break

	embed = discord.Embed(
	    title="__**Liste des commandes**__",
	    description=f"Prefix du bot = `{prefixe}` \n\n:partying_face: **Memes** : \n\n `hug`, `love`, `fight`, `kiss`, `kill`, `cry`, `highfive`, `shoot`, `sleep`, `slap`, `pat`\n\n:gear: **Commandes** : \n\n `pp`, `invite`\n\n:notes: **Musique** : \n\n `play`, `pause`, `resume`, `skip`, `queue`, `leave`\n\n:game_die: **Mini-Jeux** : \n\n `QuizzAnime`, `BlindTest`, `pendu`\n\n:tools: **Modération** (Staff Only) : \n\n `kick`, `kick_except`, `ban`, `unban`, `mute`, `unmute`, `clear`, `AuGoulag`, `SorsDuGoulag`\n\n:computer: **Serveur** (Staff Only) : \n\n `set_welcome_message`, `del_welcome_message`, `poll`, `prefix`",
	    colour=5213)
	await ctx.send(embed=embed)


@client.command()
async def profil(ctx):
    pass

keep_alive.keep_alive()

client.run("OTgzMTI2MjAyODc1MjY5MTQ0.GpjBYr.dCOVzstayZdVWw2ddSA9lVOlz8NFPbMrRasvGo")