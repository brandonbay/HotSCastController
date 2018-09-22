from tkinter import *

from FileManager import FileManager
from Player import Player

class HotsCastControllerUI:
    window = None
    fm = None
    heroes = None
    roles = None
    maps = None
    
    left_team_name = None
    home_score = None
    left1_name = None
    left1_role = None
    left1_hero = None
    left2_name = None
    left2_role = None
    left2_hero = None
    left3_name = None
    left3_role = None
    left3_hero = None
    left4_name = None
    left4_role = None
    left4_hero = None
    left5_name = None
    left5_role = None
    left5_hero = None

    right_team_name = None
    opponent_score = None
    right1_name = None
    right1_role = None
    right1_hero = None
    right2_name = None
    right2_role = None
    right2_hero = None
    right3_name = None
    right3_role = None
    right3_hero = None
    right4_name = None
    right4_role = None
    right4_hero = None
    right5_name = None
    right5_role = None
    right5_hero = None
    
    ban1_map = None
    ban2_map = None
    ban3_map = None
    ban4_map = None
    ban5_map = None

    pick1_map = None
    pick2_map = None
    pick3_map = None
    pick4_map = None
    pick5_map = None
    pick6_map = None
    pick7_map = None

    def __init__(self, window=None):
        self.window = window
        self.setup_window()
        self.setup_files()
        self.setup_header()
        self.setup_player_fields()
        self.setup_map_fields()
        self.setup_control_buttons()

    def setup_window(self):
        if self.window == None:
            self.window = Tk()
        self.window.title("Stream Asset Manager")
        self.window.geometry('1130x600')

    def setup_files(self):
        self.fm = FileManager()
        self.heroes, self.roles, self.maps = self.fm.populate_assets()

    def setup_header(self):
        header_frame = Frame(self.window, padx=10, pady=15)
        header_frame.grid(row=0)

        home_title = Label(header_frame, text="Home Team", font=("Arial Bold", 14), width=35)
        home_title.grid(column=0, row=0)
        self.home_score = StringVar()
        home_score_box = Entry(header_frame, width=2, textvariable=self.home_score)
        home_score_box.grid(column=1, row=0)

        opponent_title = Label(header_frame, text="Opponent", font=("Arial Bold", 14), width=35)
        opponent_title.grid(column=2, row=0)
        self.opponent_score = StringVar()
        opponent_score_box = Entry(header_frame, width=2, textvariable=self.opponent_score)
        opponent_score_box.grid(column=3, row=0)
        
    def setup_player_fields(self):
        player_frame = Frame(self.window, padx=10, pady=15)
        player_frame.grid(row=1)

        self.left_team_name = StringVar()
        left_team_name_box = Entry(player_frame, width=25, textvariable=self.left_team_name)
        left_team_name_box.grid(column=0, row=0, padx=20)
        left_title_name_field = Label(player_frame, text="Name")
        left_title_name_field.grid(column=1, row=0)
        left_title_role = Label(player_frame, text="Role", width=20)
        left_title_role.grid(column=2, row=0)
        left_title_hero = Label(player_frame, text="Hero", width=18)
        left_title_hero.grid(column=3, row=0)

        left1_label = Label(player_frame, text="Player 1")
        left1_label.grid(column=0, row=1)
        self.left1_name = StringVar()
        left1_name_field = Entry(player_frame, width=12, textvariable=self.left1_name)
        left1_name_field.grid(column=1, row=1)
        self.left1_role = StringVar()
        left1_role_menu = OptionMenu(player_frame, self.left1_role, *self.roles)
        left1_role_menu.grid(column=2, row=1)
        self.left1_hero = StringVar()
        left1_hero_menu = OptionMenu(player_frame, self.left1_hero, *self.heroes)
        left1_hero_menu.grid(column=3, row=1)

        left2_label = Label(player_frame, text="Player 2")
        left2_label.grid(column=0, row=2)
        self.left2_name = StringVar()
        left2_name_field = Entry(player_frame, width=12, textvariable=self.left2_name)
        left2_name_field.grid(column=1, row=2)
        self.left2_role = StringVar()
        left2_role_menu = OptionMenu(player_frame, self.left2_role, *self.roles)
        left2_role_menu.grid(column=2, row=2)
        self.left2_hero = StringVar()
        left2_hero_menu = OptionMenu(player_frame, self.left2_hero, *self.heroes)
        left2_hero_menu.grid(column=3, row=2)

        left3_label = Label(player_frame, text="Player 3")
        left3_label.grid(column=0, row=3)
        self.left3_name = StringVar()
        left3_name_field = Entry(player_frame, width=12, textvariable=self.left3_name)
        left3_name_field.grid(column=1, row=3)
        self.left3_role = StringVar()
        left3_role_menu = OptionMenu(player_frame, self.left3_role, *self.roles)
        left3_role_menu.grid(column=2, row=3)
        self.left3_hero = StringVar()
        left3_hero_menu = OptionMenu(player_frame, self.left3_hero, *self.heroes)
        left3_hero_menu.grid(column=3, row=3)

        left4_label = Label(player_frame, text="Player 4")
        left4_label.grid(column=0, row=4)
        self.left4_name = StringVar()
        left4_name_field = Entry(player_frame, width=12, textvariable=self.left4_name)
        left4_name_field.grid(column=1, row=4)
        self.left4_role = StringVar()
        left4_role_menu = OptionMenu(player_frame, self.left4_role, *self.roles)
        left4_role_menu.grid(column=2, row=4)
        self.left4_hero = StringVar()
        left4_hero_menu = OptionMenu(player_frame, self.left4_hero, *self.heroes)
        left4_hero_menu.grid(column=3, row=4)

        left5_label = Label(player_frame, text="Player 5")
        left5_label.grid(column=0, row=5)
        self.left5_name = StringVar()
        left5_name_field = Entry(player_frame, width=12, textvariable=self.left5_name)
        left5_name_field.grid(column=1, row=5)
        self.left5_role = StringVar()
        left5_role_menu = OptionMenu(player_frame, self.left5_role, *self.roles)
        left5_role_menu.grid(column=2, row=5)
        self.left5_hero = StringVar()
        left5_hero_menu = OptionMenu(player_frame, self.left5_hero, *self.heroes)
        left5_hero_menu.grid(column=3, row=5)

        self.right_team_name = StringVar()
        right_team_name_box = Entry(player_frame, width=25, textvariable=self.right_team_name)
        right_team_name_box.grid(column=4, row=0, padx=20)
        right_title_name_field = Label(player_frame, text="Name")
        right_title_name_field.grid(column=5, row=0)
        right_title_role = Label(player_frame, text="Role", width=20)
        right_title_role.grid(column=6, row=0)
        right_title_hero = Label(player_frame, text="Hero", width=18)
        right_title_hero.grid(column=7, row=0)

        right1_label = Label(player_frame, text="Player 1")
        right1_label.grid(column=4, row=1)
        self.right1_name = StringVar()
        right1_name_field = Entry(player_frame, width=12, textvariable=self.right1_name)
        right1_name_field.grid(column=5, row=1)
        self.right1_role = StringVar()
        right1_role_menu = OptionMenu(player_frame, self.right1_role, *self.roles)
        right1_role_menu.grid(column=6, row=1)
        self.right1_hero = StringVar()
        right1_hero_menu = OptionMenu(player_frame, self.right1_hero, *self.heroes)
        right1_hero_menu.grid(column=7, row=1)

        right2_label = Label(player_frame, text="Player 2")
        right2_label.grid(column=4, row=2)
        self.right2_name = StringVar()
        right2_name_field = Entry(player_frame, width=12, textvariable=self.right2_name)
        right2_name_field.grid(column=5, row=2)
        self.right2_role = StringVar()
        right2_role_menu = OptionMenu(player_frame, self.right2_role, *self.roles)
        right2_role_menu.grid(column=6, row=2)
        self.right2_hero = StringVar()
        right2_hero_menu = OptionMenu(player_frame, self.right2_hero, *self.heroes)
        right2_hero_menu.grid(column=7, row=2)

        right3_label = Label(player_frame, text="Player 3")
        right3_label.grid(column=4, row=3)
        self.right3_name = StringVar()
        right3_name_field = Entry(player_frame, width=12, textvariable=self.right3_name)
        right3_name_field.grid(column=5, row=3)
        self.right3_role = StringVar()
        right3_role_menu = OptionMenu(player_frame, self.right3_role, *self.roles)
        right3_role_menu.grid(column=6, row=3)
        self.right3_hero = StringVar()
        right3_hero_menu = OptionMenu(player_frame, self.right3_hero, *self.heroes)
        right3_hero_menu.grid(column=7, row=3)
        
        right4_label = Label(player_frame, text="Player 4")
        right4_label.grid(column=4, row=4)
        self.right4_name = StringVar()
        right4_name_field = Entry(player_frame, width=12, textvariable=self.right4_name)
        right4_name_field.grid(column=5, row=4)
        self.right4_role = StringVar()
        right4_role_menu = OptionMenu(player_frame, self.right4_role, *self.roles)
        right4_role_menu.grid(column=6, row=4)
        self.right4_hero = StringVar()
        right4_hero_menu = OptionMenu(player_frame, self.right4_hero, *self.heroes)
        right4_hero_menu.grid(column=7, row=4)

        right5_label = Label(player_frame, text="Player 5")
        right5_label.grid(column=4, row=5)
        self.right5_name = StringVar()
        right5_name_field = Entry(player_frame, width=12, textvariable=self.right5_name)
        right5_name_field.grid(column=5, row=5)
        self.right5_role = StringVar()
        right5_role_menu = OptionMenu(player_frame, self.right5_role, *self.roles)
        right5_role_menu.grid(column=6, row=5)
        self.right5_hero = StringVar()
        right5_hero_menu = OptionMenu(player_frame, self.right5_hero, *self.heroes)
        right5_hero_menu.grid(column=7, row=5)

    def setup_map_fields(self):
        map_frame = Frame(self.window, padx=10, pady=15)
        map_frame.grid(row=2)
        
        ban1 = Label(map_frame, text="Map Ban 1")
        ban1.grid(column=0, row=0, padx=30)
        self.ban1_map = StringVar()
        ban1_map_menu = OptionMenu(map_frame, self.ban1_map, *self.maps)
        ban1_map_menu.grid(column=1, row=0)
        ban2 = Label(map_frame, text="Map Ban 2")
        ban2.grid(column=0, row=1)
        self.ban2_map = StringVar()
        ban2_map_menu = OptionMenu(map_frame, self.ban2_map, *self.maps)
        ban2_map_menu.grid(column=1, row=1)
        ban3 = Label(map_frame, text="Map Ban 3")
        ban3.grid(column=0, row=2)
        self.ban3_map = StringVar()
        ban3_map_menu = OptionMenu(map_frame, self.ban3_map, *self.maps)
        ban3_map_menu.grid(column=1, row=2)
        ban4 = Label(map_frame, text="Map Ban 4")
        ban4.grid(column=0, row=3)
        self.ban4_map = StringVar()
        ban4_map_menu = OptionMenu(map_frame, self.ban4_map, *self.maps)
        ban4_map_menu.grid(column=1, row=3)
        ban5 = Label(map_frame, text="Map Ban 5")
        ban5.grid(column=0, row=4)
        self.ban5_map = StringVar()
        ban5_map_menu = OptionMenu(map_frame, self.ban5_map, *self.maps)
        ban5_map_menu.grid(column=1, row=4)
        
        pick1 = Label(map_frame, text="Map Pick 1")
        pick1.grid(column=2, row=0, padx=30)
        self.pick1_map = StringVar()
        pick1_map_menu = OptionMenu(map_frame, self.pick1_map, *self.maps)
        pick1_map_menu.grid(column=3, row=0)
        pick2 = Label(map_frame, text="Map Pick 2")
        pick2.grid(column=2, row=1)
        self.pick2_map = StringVar()
        pick2_map_menu = OptionMenu(map_frame, self.pick2_map, *self.maps)
        pick2_map_menu.grid(column=3, row=1)
        pick3 = Label(map_frame, text="Map Pick 3")
        pick3.grid(column=2, row=2)
        self.pick3_map = StringVar()
        pick3_map_menu = OptionMenu(map_frame, self.pick3_map, *self.maps)
        pick3_map_menu.grid(column=3, row=2)
        pick4 = Label(map_frame, text="Map Pick 4")
        pick4.grid(column=2, row=3)
        self.pick4_map = StringVar()
        pick4_map_menu = OptionMenu(map_frame, self.pick4_map, *self.maps)
        pick4_map_menu.grid(column=3, row=3)
        pick5 = Label(map_frame, text="Map Pick 5")
        pick5.grid(column=2, row=4)
        self.pick5_map = StringVar()
        pick5_map_menu = OptionMenu(map_frame, self.pick5_map, *self.maps)
        pick5_map_menu.grid(column=3, row=4)
        pick6 = Label(map_frame, text="Map Pick 6")
        pick6.grid(column=2, row=5)
        self.pick6_map = StringVar()
        pick6_map_menu = OptionMenu(map_frame, self.pick6_map, *self.maps)
        pick6_map_menu.grid(column=3, row=5)
        pick7 = Label(map_frame, text="Map Pick 7")
        pick7.grid(column=2, row=6)
        self.pick7_map = StringVar()
        pick7_map_menu = OptionMenu(map_frame, self.pick7_map, *self.maps)
        pick7_map_menu.grid(column=3, row=6)

    # Update assets
    def update(self):
        player_heroes = [
            Player("L", 1, self.left1_name.get(), self.left1_hero.get(), self.left1_role.get()),
            Player("L", 2, self.left2_name.get(), self.left2_hero.get(), self.left2_role.get()),
            Player("L", 3, self.left3_name.get(), self.left3_hero.get(), self.left3_role.get()),
            Player("L", 4, self.left4_name.get(), self.left4_hero.get(), self.left4_role.get()),
            Player("L", 5, self.left5_name.get(), self.left5_hero.get(), self.left5_role.get()),
            Player("R", 1, self.right1_name.get(), self.right1_hero.get(), self.right1_role.get()),
            Player("R", 2, self.right2_name.get(), self.right2_hero.get(), self.right2_role.get()),
            Player("R", 3, self.right3_name.get(), self.right3_hero.get(), self.right3_role.get()),
            Player("R", 4, self.right4_name.get(), self.right4_hero.get(), self.right4_role.get()),
            Player("R", 5, self.right5_name.get(), self.right5_hero.get(), self.right5_role.get())
        ]
        maps = [
            self.ban1_map.get(),
            self.ban2_map.get(),
            self.ban3_map.get(),
            self.ban4_map.get(),
            self.ban5_map.get(),
            self.pick1_map.get(),
            self.pick2_map.get(),
            self.pick3_map.get(),
            self.pick4_map.get(),
            self.pick5_map.get(),
            self.pick6_map.get(),
            self.pick7_map.get()
        ]
        self.fm.player_heroes = player_heroes
        self.fm.maps = maps
        self.fm.team_names = [self.left_team_name.get(), self.right_team_name.get()]
        self.fm.team_scores = [self.home_score.get(), self.opponent_score.get()]
        self.fm.update_assets()

    def load(self):
        player_names = self.fm.get_player_names()
        self.left1_name.set(player_names[0])
        self.left2_name.set(player_names[1])
        self.left3_name.set(player_names[2])
        self.left4_name.set(player_names[3])
        self.left5_name.set(player_names[4])
        self.right1_name.set(player_names[5])
        self.right2_name.set(player_names[6])
        self.right3_name.set(player_names[7])
        self.right4_name.set(player_names[8])
        self.right5_name.set(player_names[9])

        team_names = self.fm.get_team_names()
        self.left_team_name.set(team_names[0])
        self.right_team_name.set(team_names[1])

        team_scores = self.fm.get_team_scores()
        self.home_score.set(team_scores[0])
        self.opponent_score.set(team_scores[1])

    def setup_control_buttons(self):
        control_frame = Frame(self.window, padx=10, pady=15)
        control_frame.grid(row=3)

        load_button = Button(control_frame, text="Load Names", command=self.load)
        load_button.grid(column=0, row=0, padx=20)
        apply_button = Button(control_frame, text="Update", command=self.update)
        apply_button.grid(column=1, row=0, padx=20)
