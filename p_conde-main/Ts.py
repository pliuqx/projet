# -*- coding:utf-8 -*-
# @Time : 2021/10/19 16:45
# @Author: 应无所住，何生其心
# @File : Ts.py
# @Software : PyCharm

import os
import requests



headers = {
    # "Accept": "*/*",
    # "Accept-Encoding": "gzip, deflate, br",
    # "Accept-Language": "zh-CN,zh;q=0.9",
    # "Connection": "keep-alive",
    # "Content-Length": "879",
    # "Content-Type": "application/json;charset=UTF-8",
    # "Host": "videocloud.cn-hangzhou.log.aliyuncs.com",
    # "Origin": "https://jx.jxbdzyw.com",
    # "Referer": "https://jx.jxbdzyw.com/m3u8/?url=https://vod8.wenshibaowenbei.com/20211001/DeQItwdd/index.m3u8",
    # "Sec-Fetch-Dest": "empty",
    # "Sec-Fetch-Mode": "cors",
    # "Sec-Fetch-Site": "cross-site",
    # "x-log-apiversion": "0.6.0",
    # "x-log-bodyrawsize": "879",
    "User-Agent":"Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/86.0.4240.198 Safari/537.36"
}


def get_m3u8_file(m3u8_url, file_path):
    """
    下载m3u8文件
    :param m3u8_url: m3u8文件的URL
    :param file_path: 要下载的文件路径
    :return:
    """
    resp = requests.get(m3u8_url, headers=headers)
    if resp.status_code == 200:
        content = resp.text
        with open(file_path, "w") as f:
            f.write(content)


def get_ts_name_list(file_path):
    """
    获取ts文件名称列表
    :param file_path: m3u8文件路径
    :return: ts文件名称列表
    """
    ts_name_list = []
    with open(file_path, "rb") as f:
        cont_list = f.readlines()
    for cont in cont_list:
        cont = cont.decode().strip()
        if cont.endswith(".ts"):
            ts_name_list.append(cont.split("/")[-1])
            # if not cont.startswith("#"):
            #     ts_name_list.append(cont.split("/")[-1])
    return ts_name_list


def get_ts_files(file_dir, ts_url_template, ts_name_list):
    """
    循环下载ts文件
    :param file_dir: 文件下载所在文件夹
    :param ts_url_template: ts文件请求URL模板
    :param ts_name_list: ts文件名称列表
    :return:
    """
    i = 1
    for ts_name in ts_name_list:

        ts_url = ts_url_template + ts_name
        resp = requests.get(ts_url, headers=headers)
        if resp.status_code == 200:

            with open(os.path.join(file_dir, ts_name), "wb") as f:
                f.write(resp.content)

            # print("%s--.下载成功!" % ts_name + str(i))

            print(f"{ts_name}-->下载成功{i}!")
            i += 1
        else:
            print("%s--.下载失败!" % ts_name)


def merge_ts_files(file_dir, file_name, ts_name_list):
    """
    将多个ts文件进行合并
    :param file_dir: ts文件所在文件夹
    :param file_name: 合并后的文件名称
    :param ts_name_list: ts文件名称列表
    :return:
    """
    file_out = os.path.join(file_dir, file_name)
    with open(file_out, 'wb') as f_out:
        for ts_name in ts_name_list:
            with open(os.path.join(file_dir, ts_name), "rb") as f_in:
                f_out.write(f_in.read())
    print("合并ts文件成功!")


if __name__ == '__main__':
    # 用来保存ts文件
    file_dir = './ts_file'
    if not os.path.exists(file_dir):
        os.mkdir(file_dir)
    # m3u8文件URL
    m3u8_url = "https://vod6.wenshibaowenbei.com/20211012/Cks8WPMZ/1000kb/hls/index.m3u8"
    # 提取文件名
    file_name = m3u8_url.split('/')[-1]
    file_path = os.path.join(file_dir, file_name)
    # 下载m3u8文件
    get_m3u8_file(m3u8_url, file_path)
    # 获取文件中ts文件名称列表
    ts_name_list = get_ts_name_list(file_path)
    # ts文件URL模板
    ts_url_template = "https://ts6.hhmm0.com:9999/20211012/Cks8WPMZ/1000kb/hls/"
    # 下载ts文件
    get_ts_files(file_dir, ts_url_template, ts_name_list)
    # 合并ts文件
    ts_file_name = file_name.split(".")[0] + ".ts"
    merge_ts_files(file_dir, ts_file_name, ts_name_list)