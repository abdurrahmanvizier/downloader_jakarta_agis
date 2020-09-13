# Downloader Jakarta Agis 
Download Tools Just For Jakarta Agis "https://riwayat-file-covid-19-dki-jakarta-jakartagis.hub.arcgis.com/", Change Link if Old Link Change


## Command Usage
```
usage: downloaddata_covid.py [-h] [-u URL] [-pd PATH_DOWNLOAD] [-pl PATH_LOG] [-dd-s DOWNLOAD_SPESIFIC_DATE] [-v]
                             [-dd {full,current,delta}]

Downloader Tools for Jakarta Agis Website

optional arguments:
  -h, --help            Show this help message and exit.
  -u URL, --url URL     The URL Jakarta Agis
  -pd PATH_DOWNLOAD, --path-download PATH_DOWNLOAD
                        Location to Store File Downloaded, Default Current Path Script
  -pl PATH_LOG, --path-log PATH_LOG
                        Location to Store File Log, Default Current Path Script
  -dd-s DOWNLOAD_SPESIFIC_DATE, --download-spesific-date DOWNLOAD_SPESIFIC_DATE
                        Spesific Date for Download Data, Required if download-date is delta. Format = 'yyyymmdd'
  -v, --version         Show program's version number and exit.

required arguments:
  -dd {full,current,delta}, --download-date {full,current,delta}
                        Type Download
```
