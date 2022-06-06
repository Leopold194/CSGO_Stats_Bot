import discord

class Embed:

    def __init__(self):

        self.ErrorPrefix = discord.Embed(title = "➜ Prefix\nCette commande permet de changer le préfix du bot sur votre serveur. Indiqué le prefix voulu après la commande.")
        self.emotes = {
            "M4A4" : "<:m4a4:983350448960450620>",
            "AK-47" : "<:ak_47:983353579366674492>",
            "XM1014" : "<:xm1014:983351227914006578>",
            "AWP" : "<:awp:983350065240346635>",
            "P2000" : "<:p2000:983351339646083112>",
            "Glock-18" : "<:glock_18:983353437058121768>",
            "Desert Eagle" : "<:desert_eagle:983351623097135104>",
            "Galil AR" : "<:galil_ar:983351740692836373>",
            "FAMAS" : "<:famas:983351863212666920>",
            "P90" : "<:p90:983351957378981958>",
            "SSG 08" : "<:ssg_08:983352068888743976>",
            "SG 553" : "<:sg_553:983352177491849237>",
            "MP7" : "<:mp7:983352254868361266>",
            "Negev" : "<:negev:983352372212428832>",
            "Five-SeveN" : "<:five_seven:983353889489297408>",
            "Nova" : "<:nova:983353972242935848>",
            "UMP-45" : "<:ump_45:983354072218357810>",
            "PP-Bizon" : "<:pp_bizon:983354181991686175>",
            "M249" : "<:m249:983354336425955428>",
            "Zeus x27" : "<:zeus_x27:983354480353488906>",
            "G3SG1" : "<:g3sg1:983354611568087040>",
            "SCAR-20" : "<:scar_20:983354690488131614>",
            "MP9" : "<:mp9:983354817533595688>",
            "Tec-9" : "<:tec_9:983354893614080080>",
            "AUG" : "<:aug:983355031724097586>",
            "Dual Berettas" : "<:dual_berettas:983355133922533397>",
            "P250" : "<:p250:983355215770181653>",
            "MAC-10" : "<:mac_10:983355289166286849>",
            "Sawed-Off" : "<:sawed_off:983355367838867536>",
            "MAG-7" : "<:mag_7:983361129508118578>"}
    
    @staticmethod
    def profil_stats(name, STATS):
        embed = discord.Embed(
                            title = f"<:counter:983323899351662602> Profil de {name} <:counter:983323899351662602>", 
                            description = f"Temps de Jeu : {STATS['timeplay']}h\nMatchs Joués : {STATS['nb_match']}", 
                            color = 37)
        embed.set_thumbnail(url = STATS["avatar"])
        embed.add_field(name = "ㅤ\n__**Statistiques du joueur :**__", value="ㅤ", inline = False)
        embed.add_field(name = "⌬ K/D", value = STATS["kd"], inline = True)
        embed.add_field(name = "⌬ MVP", value = STATS["mvp"], inline = True)
        embed.add_field(name = "⌬ Headshot %", value = STATS["headshot"], inline = True)
        embed.add_field(name = "⌬ Kills", value = STATS["kill"], inline = True)
        embed.add_field(name = "⌬ Deaths", value = STATS["deaths"], inline = True)
        embed.add_field(name = "⌬ Headshots", value = STATS["headshot_nb"], inline = True)
        embed.add_field(name = "⌬ Wins", value = STATS["win_nb"], inline = True)
        embed.add_field(name = "⌬ Losses", value = STATS["losses_nb"], inline = True)
        embed.add_field(name = "⌬ Money", value = STATS["moneyEarned"], inline = True)
        embed.add_field(name = "⌬ Score", value = STATS["score"], inline = True)
        embed.add_field(name = "⌬ Damage", value = STATS["damage"], inline = True)
        embed.add_field(name = "⌬ Accuracy", value = STATS["shotsAccuracy"], inline = True)
        embed.add_field(name = "⌬ Win %", value = STATS["pourcent_win"], inline = True)
        embed.add_field(name = "⌬ Planted", value = STATS["bombsPlanted"], inline = True)
        embed.add_field(name = "⌬ Defused", value = STATS["bombsDefused"], inline = True)
        return embed

    def weapon_stats(self, name, STATS, avatar):
        embed = discord.Embed(
                            title = f"<:counter:983323899351662602> Profil de {name} <:counter:983323899351662602>", 
                            description = f"description", 
                            color = 37)
        embed.set_thumbnail(url = avatar)
        embed.add_field(name = "ㅤ\n__**Statistiques du joueur :**__", value="ㅤ", inline = False)
        
        
        for i in STATS:
            embed.add_field(name = self.emotes[i] + i, value = f"Kill : {STATS[i]['kill']}\nFired : {STATS[i]['fired']}\nHit : {STATS[i]['hit']}\nAccuracy : {STATS[i]['accuracy']}\n", inline = True)
        return embed

    def weapon_stats2(self, name, STATS, avatar):
        for i in range(25):
            del STATS[list(STATS.keys())[0]]
        embed = discord.Embed(
                            title = f"<:counter:983323899351662602> Profil de {name} <:counter:983323899351662602>", 
                            description = f"description", 
                            color = 37)
        embed.set_thumbnail(url = avatar)
        embed.add_field(name = "ㅤ\n__**Statistiques du joueur :**__", value="ㅤ", inline = False)
        
        for i in STATS:
            embed.add_field(name = self.emotes[i] + i, value = f"Kill : {STATS[i]['kill']}\nFired : {STATS[i]['fired']}\nHit : {STATS[i]['hit']}\nAccuracy : {STATS[i]['accuracy']}\n", inline = True)
        return embed