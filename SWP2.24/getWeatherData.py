import pandas as pd
import requests
import datetime
import pickle


#설정한 지역의 기상 상태를 API를 이용하여 불러옴.
#불러온 json을 분석하여 지역의 기온, 날씨 상태, 강수 확률을 알려줌.
class Weather:

    def __init__(self):
        self.user_area = ""
        self.items = ""

    def setJson(self):
        df = pd.read_csv('area_data.csv') #API를 사용할 수 있는 지역들 중 임의의 1000개 지역
        area = list(df['area'])
        df = pd.read_csv('x_data.csv') #API를 사용할 수 있는 지역들 중 임의의 1000개 지역의 X좌표
        x_df = list(df['X'])
        df = pd.read_csv('y_data.csv') #API를 사용할 수 있는 지역들 중 임의의 1000개 지역의 Y좌표
        y_df = list(df['Y'])

        idx_df = area.index(self.user_area)
        vilage_weather_url = "http://apis.data.go.kr/1360000/VilageFcstInfoService/getVilageFcst?"

        service_key = "aGseaS0o0EdPAsk5d2Ocp83rdLts9s84zfCq8yryY16S0ldRaKfN5qLtgwfeTLaMEaDXTpRuS3Gc3kJGj5PQhQ%3D%3D"

        today = datetime.datetime.today()
        base_date = today.strftime("%Y%m%d") # "20200214" == 기준 날짜
        time_data = ["0200", "0500", "0800", "1100", "1400", "1700", "2000", "2300"]
        base_time = time_data[1]

        nx = str(x_df[idx_df])
        ny = str(y_df[idx_df])

        payload = "serviceKey=" + service_key + "&" +\
            "dataType=json" + "&" +\
            "base_date=" + base_date + "&" +\
            "base_time=" + base_time + "&" +\
            "nx=" + nx + "&" +\
            "ny=" + ny

        # 값 요청
        res = requests.get(vilage_weather_url + payload)
        self.items = res.json().get('response').get('body').get('items')

    def getTemp(self):
        for item in self.items['item']:
            value = item['fcstValue']
            if item['category'] == 'T3H':
                return int(value)

    def getWeather(self):
        for item in self.items['item']:
            value = item['fcstValue']
            if item['category'] == 'SKY':
                return int(value)

    def isRain(self):
        for item in self.items['item']:
            value = item['fcstValue']
            if item['category'] == 'POP':
                if int(value) >= 70:
                    return True
                else:
                    return False
        return False

    def setArea(self, area):
        self.user_area = area
        return

    def getArea(self):
        return self.user_area

# 날씨 데이터
# for item in items['item']:
#     value = item['fcstValue']
#     if item['category'] == 'POP':
#         print("강수확률: " + value)
#     elif item['category'] == 'SKY':
#         if value == '1':
#             print("맑음")
#         elif value == '3':
#             print("구름많음")
#         elif value == '4':
#             print("흐림")
#     elif item['category'] == 'T3H':
#         print("기온: " + value)

### 다른 사람 코드 필요 없어지면 지워 버리자 ###
# data = dict()
# data['date'] = base_date
#
# weather_data = dict()
# for item in items['item']:
#     # 기온
#     if item['category'] == 'T3H':
#         weather_data['tmp'] = item['fcstValue']
#
#     # 기상상태
#     if item['category'] == 'PTY':
#
#         weather_code = item['fcstValue']
#
#         if weather_code == '1':
#             weather_state = '비'
#         elif weather_code == '2':
#             weather_state = '비/눈'
#         elif weather_code == '3':
#             weather_state = '눈'
#         elif weather_code == '4':
#             weather_state = '소나기'
#         else:
#             weather_state = '없음'
#
#         weather_data['code'] = weather_code
#         weather_data['state'] = weather_state
#
# data['weather'] = weather_data
# data['weather']
