import requests
from pprint import pprint
import datetime
headers = {
    "x-nxopen-api-key": "test_be0e4ffa4d06038831a158bb078bbcf6195b86c9e4d81e29525b0aa7e94b1112cd41f510e25ecac2eeb5dced9e968079"
    
  }

now = (datetime.datetime.now()-datetime.timedelta(days=1)).strftime('20%y-%m-%d')
print(now)
dict_charater = {}
characterName = input('캐릭터명을 입력하세요 : ')
urlString = f"https://open.api.nexon.com/maplestory/v1/id?character_name={characterName}"
response = requests.get(urlString, headers = headers).json()
dict_charater[characterName] = response['ocid']
pprint(dict_charater[characterName])
dict_method = {
    '기본' : 'basic',
    '종합' : 'stat',
    '하이퍼스텟' : 'hyper-stat',
    '성향' : 'propensity',
    '어빌리티' : 'ability'
}
method = input('얻을 정보를 입력하세요 (기본/종합/하이퍼스텟/성향/어빌리티) : ')

urlresult = f"https://open.api.nexon.com/maplestory/v1/character/{dict_method[method]}?ocid={dict_charater[characterName]}&date={now}"
results = requests.get(urlresult, headers = headers).json()
pprint(results)