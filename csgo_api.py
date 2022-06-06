import requests
from bs4 import BeautifulSoup

class CSGOStats:
    def __init__(self,name) -> None:
        self.name = name
        self.no_error = True

        headers = {
                'connection': 'keep-alive',
                'User-Agent': 'Mozilla/5.0 (X11; Ubuntu; Linux x86_64; rv:73.0) Gecko/20100101 Firefox/73.0'}

        cookies = {
            "steamCountry":"FR|4a6494567bd2f9b6b4d15922b610cc9e",
            "steamMachineAuth76561199100442028":"365DCC0FE322A16D5A10272F5FF638FA8104776B",
            "timezoneOffset":"7200,0",
            "sessionid":"3ca004dbe6b357f4b5cea95e"
        }


        steam_url = f"https://steamcommunity.com/search/SearchCommunityAjax?text={self.name}&filter=users&sessionid=3ca004dbe6b357f4b5cea95e&steamid_user=false"
        site_resp = requests.get(steam_url,headers=headers,cookies=cookies)
        soup_object = BeautifulSoup(site_resp.text, "lxml")
        self.steam_id = soup_object.find_all("a")[0].get("href").split("/")[-1][:-2]

        stats_profil_url = f"https://tracker.gg/csgo/profile/steam/{self.steam_id}/overview"
        site_resp3 = requests.get(stats_profil_url, headers=headers)
        soup_object3 = BeautifulSoup(site_resp3.text, "lxml")

        stats_weapons_url = f"https://tracker.gg/csgo/profile/steam/{self.steam_id}/weapons"
        site_resp4 = requests.get(stats_weapons_url, headers=headers)
        soup_object4 = BeautifulSoup(site_resp4.text, "lxml")

        stats_maps_url = f"https://tracker.gg/csgo/profile/steam/{self.steam_id}/maps"
        site_resp5 = requests.get(stats_maps_url, headers=headers)
        soup_object5 = BeautifulSoup(site_resp5.text, "lxml")

        self.informations_profil = {
                            "avatar" : soup_object3.find_all("img", {"class":"ph-avatar__image"})[0].get("src"),
                            "kd" : soup_object3.find_all("span", {"class":"value"})[0].text,
                            "headshot" : soup_object3.find_all("span", {"class":"value"})[1].text,
                            "win" : soup_object3.find_all("span", {"class":"value"})[2].text,
                            "mvp" : soup_object3.find_all("span", {"class":"value"})[3].text,
                            "kill" : soup_object3.find_all("span", {"class":"value"})[4].text,
                            "deaths" : soup_object3.find_all("span", {"class":"value"})[5].text,
                            "headshot_nb" : soup_object3.find_all("span", {"class":"value"})[6].text,
                            "win_nb" : soup_object3.find_all("span", {"class":"value"})[7].text,
                            "losses_nb" : soup_object3.find_all("span", {"class":"value"})[8].text,
                            "score" : soup_object3.find_all("span", {"class":"value"})[9].text,
                            "damage" : soup_object3.find_all("span", {"class":"value"})[10].text,
                            "shotsAccuracy" : soup_object3.find_all("span", {"class":"value"})[11].text,
                            "bombsPlanted" : soup_object3.find_all("span", {"class":"value"})[12].text,
                            "bombsDefused" : soup_object3.find_all("span", {"class":"value"})[13].text,
                            "moneyEarned" : soup_object3.find_all("span", {"class":"value"})[14].text,
                            "hostageRescued" : soup_object3.find_all("span", {"class":"value"})[15].text}
        self.informations_weapons = {}
        self.informations_maps = {}

        all_i = soup_object4.find_all("tr")
        for i in all_i:
            if i.text[1:4] == "AWP":
                self.informations_weapons["awp"] = self.do_dict(i)
            elif i.text[1:5] == "M4A4":
                self.informations_weapons["m4a4"] = self.do_dict(i)
            elif i.text[1:6] == "AK-47":
                self.informations_weapons["ak47"] = self.do_dict(i)
            elif i.text[1:7] == "SG 553":
                self.informations_weapons["sg553"] = self.do_dict(i)
            elif i.text[1:4] == "AUG":
                self.informations_weapons["aug"] = self.do_dict(i)
            elif i.text[1:6] == "P2000":
                self.informations_weapons["p2000"] = self.do_dict(i)
            elif i.text[1:6] == "Galil":
                self.informations_weapons["galil"] = self.do_dict(i)
            elif i.text[1:13] == "Desert Eagle":
                self.informations_weapons["deagle"] = self.do_dict(i)
            elif i.text[1:9] == "Glock-18":
                self.informations_weapons["glock"] = self.do_dict(i)
            elif i.text[1:6] == "FAMAS":
                self.informations_weapons["famas"] = self.do_dict(i)
            elif i.text[1:4] == "MP7":
                self.informations_weapons["mp7"] = self.do_dict(i)
            elif i.text[1:4] == "P90":
                self.informations_weapons["p90"] = self.do_dict(i)
            elif i.text[1:4] == "MP9":
                self.informations_weapons["mp9"] = self.do_dict(i)
            elif i.text[1:5] == "Nova":
                self.informations_weapons["nova"] = self.do_dict(i)
            elif i.text[1:14] == "Dual Berettas":
                self.informations_weapons["berettas"] = self.do_dict(i)
            elif i.text[1:7] == "UMP-45":
                self.informations_weapons["ump"] = self.do_dict(i)
            elif i.text[1:7] == "MAC-10":
                self.informations_weapons["mac10"] = self.do_dict(i)
            elif i.text[1:7] == "XM1014":
                self.informations_weapons["xm1014"] = self.do_dict(i)
            elif i.text[1:6] == "G3SG1":
                self.informations_weapons["g3sg1"] = self.do_dict(i)
            elif i.text[1:7] == "SSG 08":
                self.informations_weapons["ssg"] = self.do_dict(i)
            elif i.text[1:8] == "SCAR-20":
                self.informations_weapons["scar"] = self.do_dict(i)
            elif i.text[1:9] == "PP-Bizon":
                self.informations_weapons["ppbizon"] = self.do_dict(i)
            elif i.text[1:5] == "M249":
                self.informations_weapons["m249"] = self.do_dict(i)
            elif i.text[1:6] == "Negev":
                self.informations_weapons["negev"] = self.do_dict(i)
            elif i.text[1:5] == "P250":
                self.informations_weapons["p250"] = self.do_dict(i)
            elif i.text[1:11] == "Five-SeveN":
                self.informations_weapons["fiveseven"] = self.do_dict(i)
            elif i.text[1:6] == "MAG-7":
                self.informations_weapons["mag7"] = self.do_dict(i)
            elif i.text[1:6] == "Tec-9":
                self.informations_weapons["tec9"] = self.do_dict(i)
            elif i.text[1:10] == "Sawed-Off":
                self.informations_weapons["sawed"] = self.do_dict(i)
            elif i.text[1:9] == "Zeus x27":
                self.informations_weapons["zeus"] = self.do_dict(i)
        
        all_i2 = soup_object5.find_all("tr")
        for i in all_i2:
            if i.text[1:5] == "Lake":
                self.informations_maps["lake"] = self.do_dict2(i)
            elif i.text[1:8] == "Dust II":
                self.informations_maps["dust2"] = self.do_dict2(i)
            elif i.text[1:8] == "Inferno":
                self.informations_maps["inferno"] = self.do_dict2(i)
            elif i.text[1:5] == "Nuke":
                self.informations_maps["nuke"] = self.do_dict2(i)
            elif i.text[1:8] == "Vertigo":
                self.informations_maps["vertigo"] = self.do_dict2(i)
            elif i.text[1:12] == "Cobblestone":
                self.informations_maps["cobblestone"] = self.do_dict2(i)
            elif i.text[1:7] == "Office":
                self.informations_maps["office"] = self.do_dict2(i)
            elif i.text[1:10] == "Safehouse":
                self.informations_maps["safehouse"] = self.do_dict2(i)
            elif i.text[1:5] == "Bank":
                self.informations_maps["bank"] = self.do_dict2(i)
            elif i.text[1:10] == "Sugarcane":
                self.informations_maps["sugarcane"] = self.do_dict2(i)
            elif i.text[1:6] == "Train":
                self.informations_maps["train"] = self.do_dict2(i)
            elif i.text[1:10] == "Monastery":
                self.informations_maps["monastery"] = self.do_dict2(i)
            elif i.text[1:8] == "Militia":
                self.informations_maps["militia"] = self.do_dict2(i)
            elif i.text[1:7] == "Shoots":
                self.informations_maps["shoots"] = self.do_dict2(i)
            elif i.text[1:9] == "St. Marc":
                self.informations_maps["st marc"] = self.do_dict2(i)
            elif i.text[1:8] == "Baggage":
                self.informations_maps["baggage"] = self.do_dict2(i)           

    def do_dict(self, i):
        dict_stats = {"kill" : i.find_all("span", {"class":"segment-used__tp-name"})[1].text,
                "fired" : i.find_all("span", {"class":"segment-used__tp-name"})[2].text,
                "hit" : i.find_all("span", {"class":"segment-used__tp-name"})[3].text,
                "accuracy" : i.find_all("span", {"class":"segment-used__tp-name"})[4].text}
        return dict_stats

    def do_dict2(self, i):
        dict_stats = {"wins" : i.find_all("span", {"class":"segment-used__tp-name"})[1].text,
                    "loses" : i.find_all("span", {"class":"segment-used__tp-name"})[2].text,
                    "ratio" : round(float(i.find_all("span", {"class":"segment-used__tp-name"})[1].text.replace(",", ".")) / float(i.find_all("span", {"class":"segment-used__tp-name"})[2].text.replace(",", ".")), 2)}
        return dict_stats

test = CSGOStats("Leo Urahara")

print(test.informations_maps)
