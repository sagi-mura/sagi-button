import pandas as pd
import json
import datetime

# Read time from file
with open("last_export_time", "r") as f1:
    last_export_time_str = f1.read()
    if last_export_time_str == "":
        last_export_time_str = "2021-01-01 00:00:00"
    last_export_time = pd.to_datetime(last_export_time_str)

pd.set_option('display.notebook_repr_html', False)
# Load xlsx
dataframe = pd.read_excel(io='./Sagi Button音频收集.xlsx', header=0)

audios = []
for index, row in dataframe.iterrows():
    submit_time: pd.Timestamp = row["提交时间（自动）"]
    # Skip if submit_time is before last_export_time
    if submit_time <= last_export_time:
        continue
    audio = {}
    audio["name"] = row["音频中文名（必填）"]
    audio["path"] = row["音频文件（必填）"]
    audio["date"] = submit_time.strftime("%Y-%m-%d")
    audio["translate"] = {}
    audio["translate"]["zh-CN"] = row["音频中文名（必填）"]
    audio["translate"]["en-US"] = row["音频英文名（必填）"]
    audio["usePicture"] = {}
    audio["usePicture"]["zh-CN"] = row["音频相关图片"]
    audio["usePicture"]["en-US"] = row["音频相关图片"]
    audio["category"] = row["音频分类（必填）"]
    audio["mark"] = {}
    audio["mark"]["title"] = row["来源直播或视频标题（必填）"]
    audio["mark"]["time"] = row["视频时间"]
    audio["mark"]["url"] = row["视频链接"]
    print(audio)
    audios.append(audio)

jsonstr = json.dumps(audios, indent=2, ensure_ascii=False)
with open("outputs.json", "w", encoding="utf8") as outputs:
    outputs.write(jsonstr)

with open("last_export_time", "w") as f2:
    f2.write(datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S"))
