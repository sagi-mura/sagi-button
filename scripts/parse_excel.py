import pandas as pd
import json
import datetime
import math

last_export_date_file = "last_export_date"
# Read date from file
with open(last_export_date_file, "r") as f1:
    last_export_date = f1.read()
    if last_export_date == "":
        last_export_date = "2023-08-22"
    last_export_date = pd.to_datetime(last_export_date)

pd.set_option('display.notebook_repr_html', False)
# Load xlsx
dataframe = pd.read_excel(io='./Sagi Button音频收集.xlsx', header=0)

audios = []
for index, row in dataframe.iterrows():
    submit_time: pd.Timestamp = row["提交时间（自动）"]
    # Skip if submit_time is before last_export_date
    if submit_time <= last_export_date:
        continue
    audio = {}
    audio["name"] = row["音频中文名（必填）"]
    audio["path"] = row["音频文件（必填）"]
    audio["date"] = submit_time.strftime("%Y-%m-%d")
    audio["translate"] = {}
    audio["translate"]["zh-CN"] = row["音频中文名（必填）"]
    audio["translate"]["en-US"] = row["音频英文名（必填）"]
    pic = row["音频相关图片"]
    if not math.isnan(pic):
        audio["usePicture"] = {}
        audio["usePicture"]["zh-CN"] = pic
        audio["usePicture"]["en-US"] = pic
    audio["category"] = row["音频分类（必填）"]
    audio["mark"] = {}
    audio["mark"]["title"] = row["标题（必填）"]
    mark_time = row["视频时间"]
    if mark_time is str and not math.isnan(mark_time):
        audio["mark"]["time"] = mark_time
    mark_url = row["视频链接"]
    if mark_url is str and not math.isnan(mark_url):
        audio["mark"]["url"] = mark_url
    print(audio)
    audios.append(audio)

now_date = datetime.datetime.now().strftime("%Y-%m-%d")

jsonstr = json.dumps(audios, indent=2, ensure_ascii=False)
with open(f"{now_date}.json", "w", encoding="utf8") as outputs:
    outputs.write(jsonstr)

with open(last_export_date_file, "w") as f2:
    f2.write(now_date)
