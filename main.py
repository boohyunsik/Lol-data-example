from DataService import DataService
from LolService import LolService

if __name__ == '__main__':
    lolService = LolService()
    # match = lolService.get_match_detail_info_by_summoner_name("하위빅스비")
    # print(match)
    user = lolService.get_summoner_info("하위빅스비")
    dataService = DataService()
    dataService.print_average_data(user['accountId'])



