# 년, 월, 일 분리되있는 시간데이터 병합
import pandas as pd

file_path = r"C:\edf\data\2024.csv"

df = pd.read_csv(file_path)

df["date"] = pd.to_datetime(
    df["year"].astype(str) + "-" +
    df["month"].astype(str).str.zfill(2) + "-" +
    df["day"].astype(str).str.zfill(2)
) # YYYY-MM-DD

df.drop(columns=["year", "month", "day"], inplace=True)

df.to_csv(file_path, index=False)

