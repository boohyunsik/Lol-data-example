from DataService import DataService
from LolService import LolService

if __name__ == '__main__':
    lolService = LolService()

    champ = lolService.get_champion_data_by_id(76)

    # user = lolService.get_summoner_info("justlikethatkr")

    # start_index = 0
    # end_index = 99
    # count = 0
    #for i in range(20):
    #   match_summaries = lolService.get_match_summary_info_by_paginate(user['accountId'], start_index, end_index)
    #    matches = match_summaries['matches']
    #    for match in matches:
    #        if match['champion'] == 76:
    #            print(match)
    #            count += 1
    #    start_index += 100
    #    end_index += 100
    #print(f"total count : {count}")




