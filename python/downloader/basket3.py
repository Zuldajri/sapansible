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


results = [{'Fastkey': '0030000001666342020', 'Description': 'S4HANAOP105_ERP_LANG_TR.SAR', 'Filesize': 448939, 'Infotype': 'SAR'},
{'Fastkey': '0030000001666362020', 'Description': 'S4HANAOP105_ERP_LANG_UK.SAR', 'Filesize': 379844, 'Infotype': 'SAR'},
{'Fastkey': '0030000001666372020', 'Description': 'S4HANAOP105_ERP_LANG_VI.SAR', 'Filesize': 720496, 'Infotype': 'SAR'},
{'Fastkey': '0030000001666392020', 'Description': 'S4HANAOP105_ERP_LANG_ZF.SAR', 'Filesize': 418092, 'Infotype': 'SAR'},
{'Fastkey': '0030000001666412020', 'Description': 'S4HANAOP105_ERP_LANG_ZH.SAR', 'Filesize': 597893, 'Infotype': 'SAR'},
{'Fastkey': '0020000000363342021', 'Description': 'SAP HOST AGENT 7.21 SP51', 'Filesize': 87193, 'Infotype': 'SAR'},
{'Fastkey': '0020000000703122018', 'Description': 'SAP IGS Fonts and Textures', 'Filesize': 61489, 'Infotype': 'SAR'},
{'Fastkey': '0010000001645292020', 'Description': 'SAP_UI 755: SP 0001', 'Filesize': 202303, 'Infotype': 'SAR'},
{'Fastkey': '0020000000149592021', 'Description': 'SP12 Patch3 for UMML4HANA 1', 'Filesize': 268, 'Infotype': 'ZIP'},
{'Fastkey': '0010000000216182021', 'Description': 'SPAM/SAINT Update - Version 755/0077', 'Filesize': 9932, 'Infotype': 'SAR'},
{'Fastkey': '0010000001984822020', 'Description': 'ST-PI 740: SP 0014', 'Filesize': 8529, 'Infotype': 'SAR'},
{'Fastkey': '0020000000515542021', 'Description': 'SWPM20SP08', 'Filesize': 164897, 'Infotype': 'SAR'},
{'Fastkey': '0010000001013272020', 'Description': 'UIAPFI70 800: Add-On Installation', 'Filesize': 265495, 'Infotype': 'SAR'},
{'Fastkey': '0010000000638612020', 'Description': 'UIBAS001 600: Add-On Installation', 'Filesize': 107187, 'Infotype': 'SAR'},
{'Fastkey': '0010000019183952017', 'Description': 'UIHR002 100: Add-On Installation', 'Filesize': 2610, 'Infotype': 'SAR'},
{'Fastkey': '0010000020421312017', 'Description': 'UIHR002 100: SP 0001', 'Filesize': 4383, 'Infotype': 'SAR'},
{'Fastkey': '0010000000493432018', 'Description': 'UIHR002 100: SP 0002', 'Filesize': 5328, 'Infotype': 'SAR'},
{'Fastkey': '0010000001141912018', 'Description': 'UIHR002 100: SP 0003', 'Filesize': 7399, 'Infotype': 'SAR'},
{'Fastkey': '0010000001934802018', 'Description': 'UIHR002 100: SP 0004', 'Filesize': 8819, 'Infotype': 'SAR'},
{'Fastkey': '0010000000045522019', 'Description': 'UIHR002 100: SP 0005', 'Filesize': 11104, 'Infotype': 'SAR'},
{'Fastkey': '0010000000464552019', 'Description': 'UIHR002 100: SP 0006', 'Filesize': 8851, 'Infotype': 'SAR'},
{'Fastkey': '0010000001273902019', 'Description': 'UIHR002 100: SP 0007', 'Filesize': 15356, 'Infotype': 'SAR'},
{'Fastkey': '0010000001810332019', 'Description': 'UIHR002 100: SP 0008', 'Filesize': 13415, 'Infotype': 'SAR'},
{'Fastkey': '0010000000341482020', 'Description': 'UIHR002 100: SP 0009', 'Filesize': 23241, 'Infotype': 'SAR'},
{'Fastkey': '0010000000979992020', 'Description': 'UIHR002 100: SP 0010', 'Filesize': 15356, 'Infotype': 'SAR'},
{'Fastkey': '0010000000696272016', 'Description': 'UIMDG001 200: Add-On Installation', 'Filesize': 19342, 'Infotype': 'SAR'},
{'Fastkey': '0010000014298612017', 'Description': 'UIMDG001 200: SP 0002', 'Filesize': 21180, 'Infotype': 'SAR'},
{'Fastkey': '0010000019125502017', 'Description': 'UIMDG001 200: SP 0003', 'Filesize': 19934, 'Infotype': 'SAR'},
{'Fastkey': '0010000019849022017', 'Description': 'UIMDG001 200: SP 0004', 'Filesize': 9691, 'Infotype': 'SAR'},
{'Fastkey': '0010000020421762017', 'Description': 'UIMDG001 200: SP 0005', 'Filesize': 16374, 'Infotype': 'SAR'},
{'Fastkey': '0010000000493392018', 'Description': 'UIMDG001 200: SP 0006', 'Filesize': 16371, 'Infotype': 'SAR'},
{'Fastkey': '0010000001935022018', 'Description': 'UIMDG001 200: SP 0007', 'Filesize': 10835, 'Infotype': 'SAR'},
{'Fastkey': '0010000000464372019', 'Description': 'UIMDG001 200: SP 0008', 'Filesize': 10736, 'Infotype': 'SAR'},
{'Fastkey': '0010000001029322016', 'Description': 'UIMDG001 200: Support Package 0001', 'Filesize': 15880, 'Infotype': 'SAR'},
{'Fastkey': '0010000001013212020', 'Description': 'UIS4HOP1 600: Add-On Installation', 'Filesize': 843021, 'Infotype': 'SAR'},
{'Fastkey': '0010000001909232018', 'Description': 'UITRV001 300: Add-On Installation', 'Filesize': 7934, 'Infotype': 'SAR'},
{'Fastkey': '0010000000045572019', 'Description': 'UITRV001 300: SP 0001', 'Filesize': 7423, 'Infotype': 'SAR'},
{'Fastkey': '0010000001273832019', 'Description': 'UITRV001 300: SP 0002', 'Filesize': 9986, 'Infotype': 'SAR'},
{'Fastkey': '0010000001810452019', 'Description': 'UITRV001 300: SP 0003', 'Filesize': 8637, 'Infotype': 'SAR'},
{'Fastkey': '0010000000341512020', 'Description': 'UITRV001 300: SP 0004', 'Filesize': 10244, 'Infotype': 'SAR'}]

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
