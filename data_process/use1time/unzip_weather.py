import zipfile
import os

zip_paths = os.listdir(r"C:/edf/data/weather")

def get_output_path(filename:str):
    names = filename.split('_')
    output_name = f'{names[2]}_{names[4]}.csv'
    return os.path.join(r"C:/edf/data/weather", names[2], output_name)

for zip_file in zip_paths:
    if not zip_file.endswith(".zip"):
        continue
    zip_path = os.path.join(r"C:/edf/data/weather", zip_file)
    with zipfile.ZipFile(zip_path, 'r') as zip_ref:
        files = zip_ref.namelist()
        if len(files) != 1:
            print(f"unexpected file count: {zip_file}, \nList: {files}")
        elif not files[0].endswith(".csv"):
            print(f"unexpected file type: {zip_file}, {files[0]}")
        out_path = get_output_path(files[0])
        with zip_ref.open(files[0]) as source:
            with open(out_path, 'wb') as target:
                target.write(source.read())
