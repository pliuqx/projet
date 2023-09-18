import ffmpeg
import requests
import re
import json
import os
from lxml import etree

def download(url):
    headers = {
        "User-Agent": "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/605.1.15 (KHTML, like Gecko) Version/15.0 Safari/605.1.15",
        "Referer": url
    }
    html_text = requests.get(url=url, headers=headers).text
    tree = etree.HTML(html_text)
    title = tree.xpath('//*[@id="viewbox_report"]/h1/span/text()')[0]

    file_path = "./Bilibili/" + title + "/"
    if not os.path.exists(file_path):
        os.mkdir(file_path)

    ex = '.*?window.__playinfo__=(.*?)</script>'
    obj_str = re.findall(ex, html_text, re.S)[0]
    json_text = json.loads(obj_str)

    video_url = json_text['data']['dash']['video'][0]['baseUrl']
    audio_url = json_text['data']['dash']['audio'][0]['baseUrl']

    video = requests.get(url = video_url,headers = headers).content
    video_name = title + ".mp4"
    video_file = file_path +  video_name
    with open(video_file,"wb") as fp:
        fp.write(video)
    print(video_name+"视频爬取完成！")

    audio = requests.get(url = audio_url,headers = headers).content
    audio_name = title + ".mp3"
    audio_file = file_path +  audio_name
    with open(audio_file,"wb") as fp:
        fp.write(audio)
    print(audio_name+"音频爬取完成！")

    result_path = finished_path +  video_name
    instruction = "/Users/lee/Desktop/MyStudy/PyProjects/Reptile/ffmpeg -i "+video_file+" -i "+audio_file+" -codec copy "+result_path
    os.system(instruction)
    print("视频音频合并完成！！！")


if __name__ == "__main__":

    if not os.path.exists("./Bilibili"):
        os.mkdir("./Bilibili")

    finished_path = "./Bilibili/" + "Finished" + "/"
    if not os.path.exists(finished_path):
        os.mkdir(finished_path)

    url = "https://www.bilibili.com/video/BV1L64y1m7Hj"
    download(url)












