from json import load
from os import listdir
from shutil import copyfile

from Player import Player

DEFAULT_ASSETS_PATH = "./assets"
DEFAULT_LIVE_FOLDER = "Live"


class FileManager:
    def __init__(self):
        with open("configuration.json", "rb") as config_file:
            self.CONFIG = load(config_file)
        self.player_heroes = []
        self.maps = []
        for i in range(1,6):
            left = Player()
            left.num = i
            left.team = "L"

            right = Player()
            right.num = i
            right.team = "R"

            self.player_heroes.append(left)
            self.player_heroes.append(right)

    def assets_path(self):
        if "assets_path" in self.CONFIG:
            return self.CONFIG["assets_path"]
        return DEFAULT_ASSETS_PATH

    def live_folder(self):
        if "live_folder_name" in self.CONFIG:
            return self.CONFIG["live_folder_name"]
        return DEFAULT_LIVE_FOLDER

    def populate_assets(self):
        assets_path = self.assets_path()
        heroes = [h.replace(".png","") for h in listdir("{}/Heroes".format(assets_path))]
        roles = [h.replace(".png","") for h in listdir("{}/Roles".format(assets_path))]
        maps = [h.replace(".png","") for h in listdir("{}/Maps".format(assets_path)) if "Banned" not in h]
        return heroes, roles, maps

    def get_player_names(self):
        assets_path = self.assets_path()
        live_folder = self.live_folder()
        player_names = []
        for i in range(1,6):
            with open("{}/{}/L{}Name.txt".format(assets_path, live_folder, i), "r+") as player_name:
                player_names.append(player_name.read())
        for i in range(1,6):
            with open("{}/{}/R{}Name.txt".format(assets_path, live_folder, i), "r+") as player_name:
                player_names.append(player_name.read())
        return player_names

    def get_team_names(self):
        assets_path = self.assets_path()
        live_folder = self.live_folder()
        with open("{}/{}/TeamLeft.txt".format(assets_path, live_folder), "r+") as team_name:
            left_team_name = team_name.read()
        with open("{}/{}/TeamRight.txt".format(assets_path, live_folder), "r+") as team_name:
            right_team_name = team_name.read()
        return [left_team_name, right_team_name]

    def get_team_scores(self):
        assets_path = self.assets_path()
        live_folder = self.live_folder()
        with open("{}/{}/ScoreLeft.txt".format(assets_path, live_folder), "r+") as team_score:
            left_team_score = team_score.read()
        with open("{}/{}/ScoreRight.txt".format(assets_path, live_folder), "r+") as team_score:
            right_team_score = team_score.read()
        return [left_team_score, right_team_score]

    def update_assets(self):
        assets_path = self.assets_path()
        live_folder = self.live_folder()
        for player in self.player_heroes:
            if len(player.hero_name) > 0:
                copyfile(
                    "{}/Heroes/{}.png".format(assets_path, player.hero_name),
                    "{}/{}/{}{}Hero.png".format(assets_path, live_folder, player.team, player.num)
                )
            if len(player.role) > 0:
                copyfile(
                    "{}/Roles/{}.png".format(assets_path, player.role),
                    "{}/{}/{}{}role.png".format(assets_path, live_folder, player.team, player.num)
                )
            if len(player.name) > 0:
                with open(
                        "{}/{}/{}{}Name.txt".format(assets_path, live_folder, player.team, player.num),
                        "w+"
                ) as name_file:
                    name_file.write(player.name)
        for i in range(0,5):
            if len(self.maps[i]) > 0:
                copyfile(
                    "{}/Maps/Banned {}.png".format(assets_path, self.maps[i]),
                    "{}/{}/ban{}.png".format(assets_path, live_folder, i+1)
                )
        for i in range(5,12):
            if len(self.maps[i]) > 0:
                copyfile(
                    "{}/Maps/{}.png".format(assets_path, self.maps[i]),
                    "{}/{}/game{}.png".format(assets_path, live_folder, i-4)
                )
        if len(self.team_names) > 0:
            with open("{}/{}/TeamLeft.txt".format(assets_path, live_folder), "w+") as team_name:
                team_name.write(self.team_names[0])
            with open("{}/{}/TeamRight.txt".format(assets_path, live_folder), "w+") as team_name:
                team_name.write(self.team_names[1])

        if len(self.team_scores) > 0:
            with open("{}/{}/ScoreLeft.txt".format(assets_path, live_folder), "w+") as team_score:
                team_score.write(self.team_scores[0])
            with open("{}/{}/ScoreRight.txt".format(assets_path, live_folder), "w+") as team_score:
                team_score.write(self.team_scores[1])
