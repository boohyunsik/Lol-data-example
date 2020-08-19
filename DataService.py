import json


class DataService:

    def load_mock_file(self):
        json_file = open("asset/mock-data.json", encoding="UTF8") \
            .read() \
            .replace("'", "\"") \
            .replace("False", "false") \
            .replace("True", "true")
        return json.loads(json_file)

    def print_average_data(self, account_id):
        matches = self.load_mock_file()
        for match in matches:
            self.__get_average_data(match, account_id)
            print("\n")

    def __get_average_data(self, game_data, account_id):
        game_data = self.__get_game_detail_data(game_data, account_id)
        champion = game_data['championId']
        print(f"champion: {champion}")

        stats = game_data['stats']
        kills = stats['kills']
        deaths = stats['deaths']
        assists = stats['assists']
        total_damage = stats['totalDamageDealtToChampions']
        vision_score = stats['visionScore']
        print(f"kills: {kills}, deaths: {deaths}, assists: {assists}")
        print(f"total damage dealt: {total_damage}")
        print(f"vision score: {vision_score}")

        total_minion_killed = stats['totalMinionsKilled']
        print(f"total minion: {total_minion_killed}")

        total_monster_killed = stats['neutralMinionsKilled']
        print(f"total monster: {total_monster_killed}")

        if 'neutralMinionsKilledTeamJungle' in stats:
            total_team_monster = stats['neutralMinionsKilledTeamJungle']
            print(f"total team monster: {total_team_monster}")

        if 'neutralMinionsKilledEnemyJungle' in stats:
            total_enemy_monster = stats['neutralMinionsKilledEnemyJungle']
            print(f"total enemy monster: {total_enemy_monster}")

        timeline = game_data['timeline']

        lane = timeline['lane']
        print(f"lane: {lane}")

        cs = timeline['creepsPerMinDeltas']
        print(f"creep: {cs}")

        gold_per_minute = timeline['goldPerMinDeltas']
        print(f"gold: {gold_per_minute}")

        dpm = timeline['damageTakenPerMinDeltas']
        print(f"dpm: {dpm}")

    def __get_game_detail_data(self, game_data, account_id):
        participant_identities = game_data['participantIdentities']
        for participant_identity in participant_identities:
            player = participant_identity['player']
            if player['accountId'] == account_id:
                for participant in game_data['participants']:
                    if participant['participantId'] == participant_identity['participantId']:
                        return participant
