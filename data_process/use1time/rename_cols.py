# 열 인덱스 이름 영어로 변경
import pandas as pd

file_path = r"C:\edf\data\weather\159.csv"

df = pd.read_csv(file_path, encoding='cp949')  # 또는 'euc-kr'

column_mapping = {
    "지점": "station",
    "일시": "date",
    "평균기온(°C)": "mean_temperature",
    "최저기온(°C)": "min_temperature",
    "최저기온 시각(hhmi)": "min_temperature_time",
    "최고기온(°C)": "max_temperature",
    "최고기온 시각(hhmi)": "max_temperature_time",
    "강수 계속시간(hr)": "precipitation_duration",
    "10분 최다 강수량(mm)": "max_10min_precipitation",
    "10분 최다강수량 시각(hhmi)": "max_10min_precipitation_time",
    "1시간 최다강수량(mm)": "max_1hr_precipitation",
    "1시간 최다 강수량 시각(hhmi)": "max_1hr_precipitation_time",
    "일강수량(mm)": "daily_precipitation",
    "최대 순간 풍속(m/s)": "max_gust_wind_speed",
    "최대 순간 풍속 풍향(16방위)": "max_gust_wind_direction_16pt",
    "최대 순간풍속 시각(hhmi)": "max_gust_wind_time",
    "최대 풍속(m/s)": "max_wind_speed",
    "최대 풍속 풍향(16방위)": "max_wind_direction_16pt",
    "최대 풍속 시각(hhmi)": "max_wind_time",
    "평균 풍속(m/s)": "mean_wind_speed",
    "풍정합(100m)": "wind_run_100m",
    "평균 이슬점온도(°C)": "mean_dew_point_temperature",
    "최소 상대습도(%)": "min_relative_humidity",
    "최소 상대습도 시각(hhmi)": "min_relative_humidity_time",
    "평균 상대습도(%)": "mean_relative_humidity",
    "평균 증기압(hPa)": "mean_vapor_pressure",
    "평균 현지기압(hPa)": "mean_station_pressure",
    "최고 해면기압(hPa)": "max_sea_level_pressure",
    "최고 해면기압 시각(hhmi)": "max_sea_level_pressure_time",
    "최저 해면기압(hPa)": "min_sea_level_pressure",
    "최저 해면기압 시각(hhmi)": "min_sea_level_pressure_time",
    "평균 해면기압(hPa)": "mean_sea_level_pressure",
    "가조시간(hr)": "day_length_hr",
    "합계 일조 시간(hr)": "total_sunshine_duration_hr",
    "1시간 최다일사 시각(hhmi)": "max_1hr_solar_radiation_time",
    "1시간 최다일사량(MJ/m2)": "max_1hr_solar_radiation",
    "합계 일사(MJ/m2)": "total_solar_radiation",
    "일 최심신적설(cm)": "daily_max_fresh_snowfall",
    "일 최심신적설 시각(hhmi)": "daily_max_fresh_snowfall_time",
    "일 최심적설(cm)": "daily_max_snow_depth",
    "일 최심적설 시각(hhmi)": "daily_max_snow_depth_time",
    "합계 3시간 신적설(cm)": "total_3hr_fresh_snowfall",
    "평균 전운량(1/10)": "mean_total_cloud_amount",
    "평균 중하층운량(1/10)": "mean_middle_low_cloud_amount",
    "평균 지면온도(°C)": "mean_ground_surface_temperature",
    "최저 초상온도(°C)": "min_grass_temperature",
    "평균 5cm 지중온도(°C)": "mean_5cm_soil_temperature",
    "평균 10cm 지중온도(°C)": "mean_10cm_soil_temperature",
    "평균 20cm 지중온도(°C)": "mean_20cm_soil_temperature",
    "평균 30cm 지중온도(°C)": "mean_30cm_soil_temperature",
    "0.5m 지중온도(°C)": "soil_temperature_0_5m",
    "1.0m 지중온도(°C)": "soil_temperature_1_0m",
    "1.5m 지중온도(°C)": "soil_temperature_1_5m",
    "3.0m 지중온도(°C)": "soil_temperature_3_0m",
    "5.0m 지중온도(°C)": "soil_temperature_5_0m",
    "합계 대형증발량(mm)": "total_large_pan_evaporation",
    "합계 소형증발량(mm)": "total_small_pan_evaporation",
    "9-9강수(mm)": "precipitation_9_to_9",
    "안개 계속시간(hr)": "fog_duration",
    "합계 일조시간(hr)": "total_sunshine_duration_hr_2",
    "합계 일사량(MJ/m2)": "total_solar_radiation_2"
}

df.rename(columns=column_mapping, inplace=True)

df.to_csv(file_path, index=False, encoding='utf-8-sig')

