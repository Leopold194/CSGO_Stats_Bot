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

@client.command()
@commands.has_permissions(manage_guild=True)
async def prefix(ctx, prefix):
	with open("extra.json", "r") as ex:
		data = json.load(ex)

	for i in range(len(data["prefix"])):
		if list(data["prefix"][i].keys())[0] == str(ctx.guild.id):
			data["prefix"][i][str(ctx.guild.id)] = prefix
			break

	with open("extra.json", "w") as ex:
		json.dump(data, ex)

	await ctx.send(embed=discord.Embed(title=f"Le nouveau préfix est {prefix}"))

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
	    description=f"Prefix du bot = `{prefixe}` \n\n",
	    colour=5213)
	await ctx.send(embed=embed)


@client.command()
async def profil(ctx):
    pass

@client.event
async def on_guild_join(guild):
	with open("extra.json", "r") as ex:
		data = json.load(ex)
	data["prefix"].append({str(guild.id): "cs!"})
	with open("extra.json", "w") as ex:
		json.dump(data, ex)

keep_alive.keep_alive()

client.run("OTgzMTI2MjAyODc1MjY5MTQ0.GpjBYr.dCOVzstayZdVWw2ddSA9lVOlz8NFPbMrRasvGo")