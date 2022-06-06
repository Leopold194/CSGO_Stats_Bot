import requests
import re
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
                            "pourcent_win" : soup_object3.find_all("span", {"class":"value"})[2].text,
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
                            "hostageRescued" : soup_object3.find_all("span", {"class":"value"})[15].text,
                            "timeplay" : [int(nb) for nb in re.findall(r'-?\d+\.?\d*', soup_object3.find_all("span", {"class" : "playtime"})[0].text)][0],
                            "nb_match" : [int(nb) for nb in re.findall(r'-?\d+\.?\d*', soup_object3.find_all("span", {"class" : "matches"})[0].text.replace(",", ""))][0]}
        self.informations_weapons = {}
        self.informations_maps = {}

        all_i = soup_object4.find_all("tr")
        for i in all_i[1:]:
            self.informations_weapons[i.find_all("span", {"class":"segment-used__tp-name"})[0].text] = self.do_dict(i)
        
        all_i2 = soup_object5.find_all("tr")
        for i in all_i2[1:]:
            self.informations_maps[i.find_all("span", {"class":"segment-used__tp-name"})[0].text] = self.do_dict2(i)        

    def do_dict(self, i):
        dict_stats = {"icons" : i.find_all("img")[0].get("src"),
                "kill" : i.find_all("span", {"class":"segment-used__tp-name"})[1].text,
                "fired" : i.find_all("span", {"class":"segment-used__tp-name"})[2].text,
                "hit" : i.find_all("span", {"class":"segment-used__tp-name"})[3].text,
                "accuracy" : i.find_all("span", {"class":"segment-used__tp-name"})[4].text}
        return dict_stats

    def do_dict2(self, i):
        dict_stats = {"icons" : i.find_all("img")[0].get("src"),
                    "wins" : i.find_all("span", {"class":"segment-used__tp-name"})[1].text,
                    "loses" : i.find_all("span", {"class":"segment-used__tp-name"})[2].text,
                    "ratio" : round(float(i.find_all("span", {"class":"segment-used__tp-name"})[1].text.replace(",", ".")) / float(i.find_all("span", {"class":"segment-used__tp-name"})[2].text.replace(",", ".")), 2)}
        return dict_stats
