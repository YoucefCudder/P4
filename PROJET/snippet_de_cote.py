
player_1 = Player(
    name="Ngannou",
    f_name="Francis",
    age=34,
    birthdate=None,
    gender="M",
    ranking=None,
    score=0,
)
player_2 = Player(
    name="Nurmagomedov",
    f_name="Khabib",
    age=32,
    birthdate=None,
    gender="M",
    ranking=None,
    score=0,
)
player_3 = Player(
    name="Nunes",
    f_name="Amanda",
    age=31,
    birthdate=None,
    gender="F",
    ranking=None,
    score=0,
)
player_4 = Player(
    name="Jones",
    f_name="Jon",
    age=35,
    birthdate=None,
    gender="M",
    ranking=None,
    score=0,
)
player_5 = Player(
    name="Adesanya",
    f_name="Israel",
    age=30,
    birthdate=None,
    gender="M",
    ranking=None,
    score=0,
)
player_6 = Player(
    name="Zhang",
    f_name="Weili",
    age=29,
    birthdate=None,
    gender="F",
    ranking=None,
    score=0,
)
player_7 = Player(
    name="Yan",
    f_name="Petr",
    age=28,
    birthdate=None,
    gender="M",
    ranking=None,
    score=0
)
player_8 = Player(
    name="St-Pierre",
    f_name="Georges",
    age=39,
    birthdate=None,
    gender="M",
    ranking=None,
    score=0,
)

serialized_player_1 = dict(
    name=player_1.name,
    f_name=player_1.f_name,
    age=player_1.age,
    birthdate=player_1.birthdate,
    gender=player_1.gender,
    ranking=player_1.ranking,
    score=player_1.score,
)
serialized_player_2 = dict(
    name=player_2.name,
    f_name=player_2.f_name,
    age=player_2.age,
    birthdate=player_2.birthdate,
    gender=player_2.gender,
    ranking=player_2.ranking,
    score=player_2.score,
)
serialized_player_3 = dict(
    name=player_3.name,
    f_name=player_3.f_name,
    age=player_3.age,
    birthdate=player_3.birthdate,
    gender=player_3.gender,
    ranking=player_3.ranking,
    score=player_3.score,
)
serialized_player_4 = dict(
    name=player_4.name,
    f_name=player_4.f_name,
    age=player_4.age,
    birthdate=player_4.birthdate,
    gender=player_4.gender,
    ranking=player_4.ranking,
    score=player_4.score,
)
serialized_player_5 = dict(
    name=player_5.name,
    f_name=player_5.f_name,
    age=player_5.age,
    birthdate=player_5.birthdate,
    gender=player_5.gender,
    ranking=player_5.ranking,
    score=player_5.score,
)
serialized_player_6 = dict(
    name=player_6.name,
    f_name=player_6.f_name,
    age=player_6.age,
    birthdate=player_6.birthdate,
    gender=player_6.gender,
    ranking=player_6.ranking,
    score=player_6.score,
)
serialized_player_7 = dict(
    name=player_7.name,
    f_name=player_7.f_name,
    age=player_7.age,
    birthdate=player_7.birthdate,
    gender=player_7.gender,
    ranking=player_7.ranking,
    score=player_7.score,
)
serialized_player_8 = dict(
    name=player_8.name,
    f_name=player_8.f_name,
    age=player_8.age,
    birthdate=player_8.birthdate,
    gender=player_8.gender,
    ranking=player_8.ranking,
    score=player_8.score,
)

serialized_players = (
    serialized_player_1,
    serialized_player_2,
    serialized_player_3,
    serialized_player_4,
    serialized_player_5,
    serialized_player_6,
    serialized_player_7,
    serialized_player_8,
)

db = TinyDB("db.json")
players_table = db.table("players")
players_table.truncate()  # clear the table first
players_table.insert(serialized_player_1)
players_table.insert(serialized_player_2)
players_table.insert(serialized_player_3)
players_table.insert(serialized_player_4)
players_table.insert(serialized_player_5)
players_table.insert(serialized_player_6)
players_table.insert(serialized_player_7)
players_table.insert(serialized_player_8)