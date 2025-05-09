import pandas as pd
import os

folder = r"C:\edf\data"
save_file = r"C:\edf\data\demand.csv"
merge_by = ""

files = os.listdir(folder)
files.sort() # 시간 오름차순

df = pd.read_csv(os.path.join(folder, files[0]))

for i in range(1, len(files)):
    if not files[i].endswith(".csv"):
        continue
    df_ = pd.read_csv(os.path.join(folder, files[i]))
    df = pd.concat([df, df_], ignore_index=True)

df = df.sort_values(by="date", ascending=True)
df.to_csv(save_file, index=False)

