import time

from ChampionService import ChampionService
from DataService import DataService
from LolService import LolService


lolService = LolService()
championService = ChampionService()
result = {}
game_count = 0

def analysis_detail(game_id, user_id):
    match_detail = lolService.get_match_detail_info(game_id)
    team_id = -1
    for identity in match_detail['participantIdentities']:
        if identity['player']['summonerId'] == user_id:
            participant_id = identity['participantId']
            if participant_id <= 5:
                team_id = 100
            else:
                team_id = 200
    # 승리 여부?
    teams = match_detail['teams']
    win = True
    if team_id == 100:
        team = teams[0]
        if team['win'] == 'Win':
            win = True
        else:
            win = False
    else:
        team = teams[1]
        if team['win'] == 'Win':
            win = True
        else:
            win = False

    for participant in match_detail['participants']:
        if participant['teamId'] == team_id:
            champion = championService.get_champion_data_by_id(participant['championId'])
            if champion['id'] in result:
                result[champion['id']]['count'] += 1
                if win:
                    result[champion['id']]['win'] += 1
                else:
                    result[champion['id']]['lose'] += 1
            else:
                if win:
                    result[champion['id']] = {"win": 1, "lose": 0, "count": 1}
                else:
                    result[champion['id']] = {"win": 0, "lose": 1, "count": 1}

    print(f"game {game_id}...")


if __name__ == '__main__':
    user = lolService.get_summoner_info("justlikethatkr")
    print(user)

    start_index = 0
    end_index = 99
    count = 0
    for i in range(5):
        match_summaries = lolService.get_match_summary_info_by_paginate(user['accountId'], start_index, end_index)
        matches = match_summaries['matches']
        for match in matches:
            if match['champion'] == 76:
                analysis_detail(match['gameId'], user['id'])
                count += 1
        start_index += 100
        end_index += 100
        time.sleep(5)
    print(f"total count : {count}")

    ## print result
    for data in result:
        win_rate = (result[data]['win'] / result[data]['count']) * 100.0
        print(f"With {data}, {result[data]}, {win_rate}%")

