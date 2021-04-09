#!/usr/bin/env python3
# 
#       SMP Downloader
#
#

import argparse
import re

from helper import *
from SAP_DLM import *
from SAP_SMP import *

parser = argparse.ArgumentParser(description="Downloader")
parser.add_argument("--config", required=True, type=str, dest="config", help="The configuration file")
parser.add_argument("--dir", required=False, type=str, dest="dir", help="Location to place the download file")
parser.add_argument("--basket", required=False, action="store_true", dest="basket", help="To include item in the basket, default False")
parser.add_argument("--dryrun", required=False, action="store_true", dest="dryrun", help="Dryrun set to True will not actually download the bits")

args = parser.parse_args()
Config.load(args.config)
include_basket = args.basket
dryrun         = args.dryrun
download_dir   = args.dir


DLM.init(download_dir, dryrun)
basket = DownloadBasket()

if include_basket:
    DLM.refresh_basket(basket)
    assert(len(basket.items) > 0), \
        "Download basket is empty."
    basket.filter_latest()

SMP.init()


results = [{'Fastkey': '0010000000211202021', 'Description': 'Attribute Change Package 02 for SAP_UI 755', 'Filesize': 4, 'Infotype': 'SAR'},
{'Fastkey': '0010000014247222017', 'Description': 'Attribute Change Package 11 for UIMDG001 200', 'Filesize': 4, 'Infotype': 'SAR'},
{'Fastkey': '0010000000561182019', 'Description': 'Attribute Change Package 11 for UITRV001 300', 'Filesize': 4, 'Infotype': 'SAR'},
{'Fastkey': '0010000000059642016', 'Description': 'Attribute Change Package 16 for EA-HR 608', 'Filesize': 7, 'Infotype': 'SAR'},
{'Fastkey': '0010000000029982015', 'Description': 'Attribute Change Package 18 for GBX01HR 600', 'Filesize': 4, 'Infotype': 'SAR'},
{'Fastkey': '0010000000060132013', 'Description': 'Attribute Change Package 19 for SRA004 600', 'Filesize': 5, 'Infotype': 'SAR'},
{'Fastkey': '0010000000033172015', 'Description': 'Attribute Change Package 21 for GBX01HR5 605', 'Filesize': 4, 'Infotype': 'SAR'},
{'Fastkey': '0010000020208092017', 'Description': 'Attribute Change Package 27 for UIHR002 100', 'Filesize': 4, 'Infotype': 'SAR'},
{'Fastkey': '0010000000249512014', 'Description': 'Attribute Change Package 33 for SAP_HR 608', 'Filesize': 26, 'Infotype': 'SAR'},
{'Fastkey': '0010000000297212015', 'Description': 'Attribute Change Package 34 for ST-PI 740', 'Filesize': 4, 'Infotype': 'SAR'},
{'Fastkey': '0020000001634982020', 'Description': 'Installation for SAP IGS integrated in SAP Kernel', 'Filesize': 134953, 'Infotype': 'SAR'},
{'Fastkey': '0020000000281972021', 'Description': 'Kernel Part I (781)', 'Filesize': 296386, 'Infotype': 'SAR'},
{'Fastkey': '0020000000281722021', 'Description': 'Kernel Part II (781)', 'Filesize': 7505, 'Infotype': 'SAR'},
{'Fastkey': '0020000000422652021', 'Description': 'Patch 2 for SOFTWARE UPDATE MANAGER 2.0 SP10', 'Filesize': 347058, 'Infotype': 'SAR'},
{'Fastkey': '0020000000410162020', 'Description': 'Predi. Analy. APL 2008 for SAP HANA 2.0 SPS03 and beyond', 'Filesize': 56889, 'Infotype': 'ZIP'},
{'Fastkey': '0030000001666752020', 'Description': 'S4CORE105_INST_EXPORT_1.zip', 'Filesize': 6, 'Infotype': 'ZIP'},
{'Fastkey': '0030000001666762020', 'Description': 'S4CORE105_INST_EXPORT_10.zip', 'Filesize': 1437597, 'Infotype': 'ZIP'},
{'Fastkey': '0030000001666772020', 'Description': 'S4CORE105_INST_EXPORT_11.zip', 'Filesize': 1353247, 'Infotype': 'ZIP'},
{'Fastkey': '0030000001666782020', 'Description': 'S4CORE105_INST_EXPORT_12.zip', 'Filesize': 976639, 'Infotype': 'ZIP'},
{'Fastkey': '0030000001666802020', 'Description': 'S4CORE105_INST_EXPORT_13.zip', 'Filesize': 1151293, 'Infotype': 'ZIP'},
{'Fastkey': '0030000001666842020', 'Description': 'S4CORE105_INST_EXPORT_14.zip', 'Filesize': 2017827, 'Infotype': 'ZIP'},
{'Fastkey': '0030000001666862020', 'Description': 'S4CORE105_INST_EXPORT_15.zip', 'Filesize': 1516728, 'Infotype': 'ZIP'},
{'Fastkey': '0030000001666872020', 'Description': 'S4CORE105_INST_EXPORT_16.zip', 'Filesize': 1456278, 'Infotype': 'ZIP'},
{'Fastkey': '0030000001666882020', 'Description': 'S4CORE105_INST_EXPORT_17.zip', 'Filesize': 1479934, 'Infotype': 'ZIP'},
{'Fastkey': '0030000001666892020', 'Description': 'S4CORE105_INST_EXPORT_18.zip', 'Filesize': 1955691, 'Infotype': 'ZIP'},
{'Fastkey': '0030000001666912020', 'Description': 'S4CORE105_INST_EXPORT_19.zip', 'Filesize': 1223741, 'Infotype': 'ZIP'},
{'Fastkey': '0030000001666922020', 'Description': 'S4CORE105_INST_EXPORT_2.zip', 'Filesize': 5, 'Infotype': 'ZIP'},
{'Fastkey': '0030000001666932020', 'Description': 'S4CORE105_INST_EXPORT_20.zip', 'Filesize': 1203006, 'Infotype': 'ZIP'},
{'Fastkey': '0030000001666942020', 'Description': 'S4CORE105_INST_EXPORT_21.zip', 'Filesize': 1418320, 'Infotype': 'ZIP'},
{'Fastkey': '0030000001666952020', 'Description': 'S4CORE105_INST_EXPORT_22.zip', 'Filesize': 1277856, 'Infotype': 'ZIP'},
{'Fastkey': '0030000001666982020', 'Description': 'S4CORE105_INST_EXPORT_23.zip', 'Filesize': 1626479, 'Infotype': 'ZIP'},
{'Fastkey': '0030000001666992020', 'Description': 'S4CORE105_INST_EXPORT_24.zip', 'Filesize': 989592, 'Infotype': 'ZIP'},
{'Fastkey': '0030000001667002020', 'Description': 'S4CORE105_INST_EXPORT_3.zip', 'Filesize': 154, 'Infotype': 'ZIP'},
{'Fastkey': '0030000001667012020', 'Description': 'S4CORE105_INST_EXPORT_4.zip', 'Filesize': 154, 'Infotype': 'ZIP'},
{'Fastkey': '0030000001667022020', 'Description': 'S4CORE105_INST_EXPORT_5.zip', 'Filesize': 154, 'Infotype': 'ZIP'},
{'Fastkey': '0030000001667032020', 'Description': 'S4CORE105_INST_EXPORT_6.zip', 'Filesize': 2177825, 'Infotype': 'ZIP'},
{'Fastkey': '0030000001667052020', 'Description': 'S4CORE105_INST_EXPORT_7.zip', 'Filesize': 2738497, 'Infotype': 'ZIP'},
{'Fastkey': '0030000001667062020', 'Description': 'S4CORE105_INST_EXPORT_8.zip', 'Filesize': 2203902, 'Infotype': 'ZIP'},
{'Fastkey': '0030000001667072020', 'Description': 'S4CORE105_INST_EXPORT_9.zip', 'Filesize': 1598012, 'Infotype': 'ZIP'}]

cnt     = 0
while cnt < len(results):
    r = results[cnt]
    assert("Description" in r and "Infotype" in r and "Fastkey" in r and "Filesize" in r), \
        "Result does not have all required keys (%s)" % (str(r))

    r["Filesize"]   = int(r["Filesize"])
    
    print("%s\n" % (r))
    cnt += 1
    basket.add_item(DownloadItem(
        id            = r["Fastkey"],
        desc          = r["Description"],
        size          = r["Filesize"],
        time          = basket.latest,
        base_dir      = download_dir,
        target_dir    = "Archives",
        skip_download = dryrun,
    ))

if len(basket.items) > 0:
    basket.filter_latest()
    basket.download_all()
