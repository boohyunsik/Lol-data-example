import json


class ChampionService:
    def __init__(self):
        self.champion_raw_data = json.load(open("asset/champion.json", encoding="UTF-8"))

    def get_all_champion_data(self):
        return self.champion_raw_data

    def get_champion_data_by_id(self, champion_key):
        raw_data = self.champion_raw_data
        data_list = raw_data['data']
        for data in data_list:
            champion = data_list[data]
            if champion['key'] == str(champion_key):
                return champion