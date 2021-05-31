import requests

from utils.data_util import get_yaml


def get_weather(city, date):
    auth_data = get_yaml("./utils/auth.yml")["action"]["qweather"]

    # 处理城市
    result = requests.get(auth_data["city_lookup_url"],  {"location": city, "key": auth_data["query_key"]})
    location_id = result.json()["location"][0]["id"]

    date_list = ["今天", "明天", "后天"]
    if date in date_list:
        index = date_list.index(date)
        result = requests.get(auth_data["weather_url"],  {"location": location_id, "key": auth_data["query_key"]})
        weather = result.json()["daily"][index]
        info = weather["textDay"]
        wind_dir_day = weather["windDirDay"]
        wind_scale_day = weather["windScaleDay"]
        temp_min = weather["tempMin"]
        temp_max = weather["tempMax"]
        return f"{date}{city}天气「{info}」，{wind_dir_day}{wind_scale_day}级，气温{temp_min}-{temp_max}度。"
    else:
        return "只能获取「今明后」三天的天气信息！"
