from DataService import DataService
from LolService import LolService


lolService = LolService()
result = {}

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
    #for participant in match_detail['participants']:
    #    print(participant)

    for participant in match_detail['participants']:
        if participant['teamId'] == team_id:
            champion = lolService.get_champion_data_by_id(participant['championId'])
            if champion['id'] in result:
                result[champion['id']] += 1
            else:
                result[champion['id']] = 1
    print("###################")
    # 같은 팀 플레이한 챔피언



if __name__ == '__main__':
    user = lolService.get_summoner_info("justlikethatkr")
    print(user)

    start_index = 0
    end_index = 99
    count = 0
    for i in range(2):
        match_summaries = lolService.get_match_summary_info_by_paginate(user['accountId'], start_index, end_index)
        matches = match_summaries['matches']
        for match in matches:
            if match['champion'] == 76:
                analysis_detail(match['gameId'], user['id'])
                count += 1
        start_index += 100
        end_index += 100
    print(f"total count : {count}")
    print(result)





