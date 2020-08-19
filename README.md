# LOL DATA ANALYSER (EXAMPLE)
1. 데이터 셋 지정 방법
* asset/influencer.json 파일에 스트리머 정보를 추가
* index는 가장 마지막 index + 1로 한다.
* https://developer.riotgames.com/apis#summoner-v4/GET_getBySummonerName 에서 찾고싶은 스트리머의 닉네임을 입력하여 Response를 받아온다.
```
// Response 예제
{
    "id": "lr15mOwwKRJU-wq1JMTFDQWG2aJfPlCVthEgwT5dywUI14M",
    "accountId": "Jdh5YYIiy5NDYBzg4a4Sm3dGqNg6ZqFpkbMZESh0--bt3yA",
    "puuid": "ETQDFxrkhPsCZfssV5pc2cgBDCdxwsf9x8ZHq58vTjvAIlA5zgkwBUKqBrILg9vlaMp0rtmFLP8xmg",
    "name": "나라카일",
    "profileIconId": 623,
    "revisionDate": 1597828260000,
    "summonerLevel": 150
}
```
* 위 예제중 id, accountId, puuid 항목을 influencer.json의 accounts 항목으로 추가한다.