import requests
import json


class LolService:
    def __init__(self):
        self.TAG = "LolService"
        self.URL = "https://kr.api.riotgames.com/lol"
        self.headers = {
            'Accept-Charset': 'application/x-www-form-urlencoded; charset=UTF-8',
            'X-Riot-Token': 'RGAPI-bee17f34-008d-4fd5-afe1-e7b6ae0c093f'
        }
        self.CHAMPION_DATA_DRAGON_URL = "http://ddragon.leagueoflegends.com/cdn/10.16.1/data/en_US/champion.json"

    # Get the summary of summoner information by name
    def get_summoner_info(self, name):
        response = requests.get(self.URL + "/summoner/v4/summoners/by-name/" + name, headers=self.headers)

        return json.loads(response.text)

    # Get a match information by encrypted summoner id
    def get_match_summary_info(self, encrypted_id):
        response = requests.get(self.URL + "/match/v4/matchlists/by-account/" + encrypted_id, headers=self.headers)

        return json.loads(response.text)

    def get_match_summary_info_by_paginate(self, encrypted_id, begin_index, end_index):
        params = {"beginIndex": begin_index, "endIndex": end_index}
        response = requests.get(self.URL + "/match/v4/matchlists/by-account/" + encrypted_id,
                                headers=self.headers,
                                params=params)

        return json.loads(response.text)

    # Get a match detail information by game id
    def get_match_detail_info(self, game_id):
        response = requests.get(self.URL + "/match/v4/matches/" + str(game_id), headers=self.headers)

        return json.loads(response.text)

    def get_match_detail_info_by_summoner_name(self, name):
        summoner_info = self.get_summoner_info(name)
        match_summaries = self.get_match_summary_info(summoner_info['accountId'])['matches']
        for match in match_summaries:
            match_detail = self.get_match_detail_info(match['gameId'])
            print(match_detail)

    def __load_champion_data_dragon(self):
        champion_raw_data = requests.get(self.CHAMPION_DATA_DRAGON_URL)

        return json.loads(champion_raw_data.text)

    def get_champion_data_by_id(self, champion_key):
        raw_data = self.__load_champion_data_dragon()
        data_list = raw_data['data']
        for data in data_list:
            champion = data_list[data]
            if champion['key'] == str(champion_key):
                print(champion)




