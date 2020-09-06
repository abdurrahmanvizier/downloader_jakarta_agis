# -*- coding: utf-8 -*-
"""
Created on Sun Sep  6 18:21:04 2020

@author: agrabdur7137
"""

from buildLog import Log
from bs4 import BeautifulSoup
from datetime import datetime

import requests
import platform
import urllib
import os


class CovidExtrac:

    def __init__(self, url = None, download_date = None, path_download = None, path_log = None):

        self.url = url
        self.headers = {'User-Agent': 'Mozilla/5.0'}
        self.format_download = 'https://drive.google.com/uc?export=download&id='
        self.download_date = download_date

        Current_Date = datetime.now().strftime("%A, %d %b %Y %H:%m:%S")

        if path_download == None:
            # self.logger.info("Use Default Path Script")
            current_path = os.path.abspath(os.getcwd())
            try:
                os.mkdir("{current_path}/Downloaded".format(current_path = current_path))
            except FileExistsError:
                # self.logger.info("Folder Sudah Tersedia")
                pass
            
            path_download = "{current_path}/Downloaded".format(current_path = current_path)

        if path_log == None:
            # self.logger.info("Use Default Path Log")
            current_path = os.path.abspath(os.getcwd())
            try:
                os.mkdir("{current_path}/Log".format(current_path = current_path))
            except FileExistsError:
                # self.logger.info("Folder Sudah Tersedia")
                pass
            
            path_log = "{current_path}/Log".format(current_path = current_path)

        self.logger = Log("Jakarta Agis", 'log_download_covid_file', path_log).createLog()
        self.logger.info(f"###---------- START NEW PROCESS DOWNLOAD at {Current_Date} ----------###")

        # Change Directory Download to path_download Value
        os.chdir(path_download)

    def download_data(self, date_file, url_download):
        if self.download_date == "all":
                
            self.logger.info("Download data {} with {}".format(date_file, url_download))

            urllib.request.urlretrieve(url_download, "Standar Kelurahan Data Corona ({x}).xlsx".format(x = date_file))
        
        elif self.download_date == "current":
            # Check Current OS System and Current Date
            if platform.system() == "Linux":
                current_date = datetime.now().strftime("%-d %B %Y")
            elif platform.system() == "Windows":
                current_date = datetime.now().strftime("%#d %B %Y")
            
            if current_date in date_file:
                self.logger.info("Download data {} with {}".format(date_file, url_download))

                urllib.request.urlretrieve(url_download, "Standar Kelurahan Data Corona ({x}).xlsx".format(x = date_file))
    
    def MyWho(self):
        # Funtion for Check Variable
        print([v for v in globals().keys() if not v.startswith('_')])

    def mainProc(self):
        # Getting URL Contents
        page_get = requests.get(self.url, headers=self.headers, verify=False)

        # Convert URL Contents to HTML Parser
        soup_url = BeautifulSoup(page_get.text, 'html.parser')

        # Find "script" and id "site-injection" (Default from Website)
        data_injection = soup_url.find('script', id = "site-injection")
        # print(data_injection.contents[0])

        # Cleansing contents and create Variable Window
        string_injection = data_injection.contents[0].replace('\n', "").replace(" ", "").replace("window.__SITE", "self.data_injection_window")
        exec(string_injection)

        # Convert varaibale window to URL Contents
        url_parse_window = urllib.parse.unquote(self.data_injection_window)

        # Convert URL Contents to HTML Parser
        soup_window = BeautifulSoup(url_parse_window, 'html.parser')

        # Getting All "P"
        get_all_p = soup_window.find_all('p')

        # Process Looping for All data "P"
        for x in get_all_p:
            # Getting Data where conteins "Pukul" (Website Dafault)
            if 'Pukul' in x.text:
                # Getting Link in Current Data "P"
                url_ori = x.a.attrs.get('href').replace('\\','')
                # Ada 2 Jenis URL yang didapatkan disini
                # ada yang mengandung view dan open (format penulisannya beda) (Kemungkinan untuk kedapannya bisa Bertambah)
                # Contoh
                # https://drive.google.com/file/d/1TQWb6WKkEfmwmuhfy_ZUJwnE5Lsq9S_l/view?usp=sharing
                # https://drive.google.com/open?id=1s00b5zxqv6sBB1tz670PI46FhOq4qlKW

                if 'view' in url_ori:
                    id_gs = url_ori.split('/')[-2]
                elif 'open' in url_ori:
                    id_gs = url_ori.split('open?id=')[-1]
                
                # Changa URL View to URL Download
                download_url = "{}{}".format(self.format_download, id_gs)

                # Download Data with Current Date, URL Download
                self.download_data(x.text, download_url)


if __name__ == "__main__":
    import argparse
    parser = argparse.ArgumentParser(description="Downloader Tools for Jakarta Agis Website")
    parser.add_argument('-u',"--url", help="The URL Jakarta Agis", default="https://riwayat-file-covid-19-dki-jakarta-jakartagis.hub.arcgis.com/")
    parser.add_argument("-dd", "--download-date", help="Status Download Date", choices=['all', 'current'], default="all")
    parser.add_argument("-pd", "--path-download", help="Location to Store File Downloaded", default=None)
    parser.add_argument("-pl", "--path-log", help="Location to Store File Log", default=None)
    
    args = parser.parse_args()

    print(args)

    url = args.url
    path_download = args.path_download
    path_log = args.path_log
    download_date = args.download_date

    CovidExtrac(url = url, download_date = download_date, path_download = path_download, path_log = path_log).mainProc()