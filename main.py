from turtle import color
import discord
import json
import random
import asyncio
import time

from discord.ext import commands
from discord.utils import get
from datetime import datetime, timedelta
from discord_components import DiscordComponents, Button, ButtonStyle, Select, SelectOption

from csgo_api import CSGOStats
from embed_bot import Embed

import keep_alive

async def get_prefix(bot, message):
	guild = message.guild
	with open("extra.json", "r") as ex:
		data = json.load(ex)
	for i in range(len(data["prefix"])):
		if list(data["prefix"][i].keys())[0] == str(guild.id):
			prefix = data["prefix"][i][str(guild.id)]
	if guild:
		return prefix
	else:
		return "cs!"

client = commands.Bot(command_prefix=get_prefix, help_command=None)
DiscordComponents(client)

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
	with open("extra.json", "r") as ex:
		data = json.load(ex)

	for i in range(len(data["prefix"])):
		if list(data["prefix"][i].keys())[0] == str(ctx.message.guild.id):
			prefixe = data["prefix"][i][str(ctx.guild.id)]
			break

	embed = discord.Embed(
	    title="__**Liste des commandes**__",
	    description=f"Prefix du bot = `{prefixe}` \n\n **Serveur** (Staff Only) : \n\n`prefix`",
	    colour=5213)
	await ctx.send(embed=embed)


@client.command()
async def profil(ctx, *, name):
	STATS = CSGOStats(name).informations_profil
	await ctx.send(embed = Embed.profil_stats(name, STATS))

@client.command()
async def weapons(ctx, *, name):
	global name_to_give_stats
	global embed
	STATS = CSGOStats(name)
	emojiPage2 = client.get_emoji(983369471618084916)
	name_to_give_stats= name
	embed = await ctx.send(embed = Embed().weapon_stats(name, STATS.informations_weapons, STATS.informations_profil["avatar"]), components=[[
					Button(style=ButtonStyle.grey,
							label="Page 2",
							emoji=emojiPage2)]])

@client.command()
async def stats(ctx, *, name):
	await ctx.send(
        f"Menu des Statistiques de {name}",
        components=[
            Select(
                placeholder="Quelles statistiques souhaiteriez-vous voir ?",
                options=[
                    SelectOption(label="Profil", value="Profil"),
                    SelectOption(label="Armes", value="Armes"),
					SelectOption(label="Maps", value="Maps")],
				custom_id="select1")])
		
	interaction = await client.wait_for("select_option", check=lambda inter: inter.custom_id == "select1")
	STATS = CSGOStats(name)
	if interaction.values[0] == "Profil":
		await ctx.send(embed = Embed.profil_stats(name, STATS.informations_profil))
	elif interaction.values[0] == "Armes":
		global name_to_give_stats
		global embed
		STATS = CSGOStats(name)
		emojiPage2 = client.get_emoji(983369471618084916)
		name_to_give_stats= name
		embed = await ctx.send(embed = Embed().weapon_stats(name, STATS.informations_weapons, STATS.informations_profil["avatar"]), components=[[
						Button(style=ButtonStyle.grey,
								label="Page 2",
								emoji=emojiPage2)]])
	elif interaction.values[0] == "Maps":
		await ctx.send(embed = Embed.map_stats(name, STATS))


@client.event
async def on_guild_join(guild):
	with open("extra.json", "r") as ex:
		data = json.load(ex)
	data["prefix"].append({str(guild.id): "cs!"})
	with open("extra.json", "w") as ex:
		json.dump(data, ex)

@client.event
async def on_button_click(res):
	if res.component.label == "Page 2":
		STATS = CSGOStats(name_to_give_stats)
		emojiPage1 = client.get_emoji(983367231352234034)
		await embed.edit(embed = Embed().weapon_stats2(name_to_give_stats, STATS.informations_weapons, STATS.informations_profil["avatar"]), components=[[
	                   Button(style=ButtonStyle.grey,
	                          label="Page 1",
	                          emoji=emojiPage1)]])
	elif res.component.label == "Page 1":
		STATS = CSGOStats(name_to_give_stats)
		emojiPage2 = client.get_emoji(983369471618084916)
		await embed.edit(embed = Embed().weapon_stats(name_to_give_stats, STATS.informations_weapons, STATS.informations_profil["avatar"]), components=[[
	                   Button(style=ButtonStyle.grey,
	                          label="Page 2",
	                          emoji=emojiPage2)]])

"""@client.event
async def on_command_error(ctx, error):

	if isinstance(error, commands.MissingPermissions):
		await ctx.send("<:pepesmile:828677897288024154> Vous n'avez pas les permissions pour effectuer cette commande !")
	else:
		Embeds = Embed()
		
		Embed_Errors = {
		    "prefix": Embeds.ErrorPrefix}
		await ctx.send(embed=Embed_Errors[ctx.command.qualified_name])"""
		
keep_alive.keep_alive()

client.run("OTgzMTI2MjAyODc1MjY5MTQ0.GO2L27.3aMD-7u2mWCt_wUOeQc6mKq1zxzim7WDjoWBsQ")