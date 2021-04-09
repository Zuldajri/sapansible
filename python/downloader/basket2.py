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


results = [{'Fastkey': '0030000001665652020', 'Description': 'S4HANAOP105_ERP_LANG_AR.SAR', 'Filesize': 444070, 'Infotype': 'SAR'},
{'Fastkey': '0030000001665662020', 'Description': 'S4HANAOP105_ERP_LANG_BG.SAR', 'Filesize': 394521, 'Infotype': 'SAR'},
{'Fastkey': '0030000001665682020', 'Description': 'S4HANAOP105_ERP_LANG_CA.SAR', 'Filesize': 379145, 'Infotype': 'SAR'},
{'Fastkey': '0030000001665692020', 'Description': 'S4HANAOP105_ERP_LANG_CS.SAR', 'Filesize': 648239, 'Infotype': 'SAR'},
{'Fastkey': '0030000001665712020', 'Description': 'S4HANAOP105_ERP_LANG_DA.SAR', 'Filesize': 437244, 'Infotype': 'SAR'},
{'Fastkey': '0030000001665632020', 'Description': 'S4HANAOP105_ERP_LANG_DE.SAR', 'Filesize': 272960, 'Infotype': 'SAR'},
{'Fastkey': '0030000001665722020', 'Description': 'S4HANAOP105_ERP_LANG_EL.SAR', 'Filesize': 428898, 'Infotype': 'SAR'},
{'Fastkey': '0030000001665642020', 'Description': 'S4HANAOP105_ERP_LANG_EN.SAR', 'Filesize': 498589, 'Infotype': 'SAR'},
{'Fastkey': '0030000001665742020', 'Description': 'S4HANAOP105_ERP_LANG_ES.SAR', 'Filesize': 849374, 'Infotype': 'SAR'},
{'Fastkey': '0030000001665752020', 'Description': 'S4HANAOP105_ERP_LANG_ET.SAR', 'Filesize': 282804, 'Infotype': 'SAR'},
{'Fastkey': '0030000001665802020', 'Description': 'S4HANAOP105_ERP_LANG_FI.SAR', 'Filesize': 430154, 'Infotype': 'SAR'},
{'Fastkey': '0030000001665852020', 'Description': 'S4HANAOP105_ERP_LANG_FR.SAR', 'Filesize': 839817, 'Infotype': 'SAR'},
{'Fastkey': '0030000001665892020', 'Description': 'S4HANAOP105_ERP_LANG_HE.SAR', 'Filesize': 452704, 'Infotype': 'SAR'},
{'Fastkey': '0030000001665962020', 'Description': 'S4HANAOP105_ERP_LANG_HI.SAR', 'Filesize': 730133, 'Infotype': 'SAR'},
{'Fastkey': '0030000001665972020', 'Description': 'S4HANAOP105_ERP_LANG_HR.SAR', 'Filesize': 414036, 'Infotype': 'SAR'},
{'Fastkey': '0030000001665992020', 'Description': 'S4HANAOP105_ERP_LANG_HU.SAR', 'Filesize': 477177, 'Infotype': 'SAR'},
{'Fastkey': '0030000001666042020', 'Description': 'S4HANAOP105_ERP_LANG_IT.SAR', 'Filesize': 765586, 'Infotype': 'SAR'},
{'Fastkey': '0030000001666052020', 'Description': 'S4HANAOP105_ERP_LANG_JA.SAR', 'Filesize': 789319, 'Infotype': 'SAR'},
{'Fastkey': '0030000001666062020', 'Description': 'S4HANAOP105_ERP_LANG_KK.SAR', 'Filesize': 718868, 'Infotype': 'SAR'},
{'Fastkey': '0030000001666082020', 'Description': 'S4HANAOP105_ERP_LANG_KO.SAR', 'Filesize': 451150, 'Infotype': 'SAR'},
{'Fastkey': '0030000001666092020', 'Description': 'S4HANAOP105_ERP_LANG_LT.SAR', 'Filesize': 289582, 'Infotype': 'SAR'},
{'Fastkey': '0030000001666122020', 'Description': 'S4HANAOP105_ERP_LANG_LV.SAR', 'Filesize': 288675, 'Infotype': 'SAR'},
{'Fastkey': '0030000001666142020', 'Description': 'S4HANAOP105_ERP_LANG_MS.SAR', 'Filesize': 332062, 'Infotype': 'SAR'},
{'Fastkey': '0030000001666152020', 'Description': 'S4HANAOP105_ERP_LANG_NL.SAR', 'Filesize': 492036, 'Infotype': 'SAR'},
{'Fastkey': '0030000001666172020', 'Description': 'S4HANAOP105_ERP_LANG_NO.SAR', 'Filesize': 422301, 'Infotype': 'SAR'},
{'Fastkey': '0030000001666192020', 'Description': 'S4HANAOP105_ERP_LANG_PL.SAR', 'Filesize': 481707, 'Infotype': 'SAR'},
{'Fastkey': '0030000001666212020', 'Description': 'S4HANAOP105_ERP_LANG_PT.SAR', 'Filesize': 792231, 'Infotype': 'SAR'},
{'Fastkey': '0030000001666222020', 'Description': 'S4HANAOP105_ERP_LANG_RO.SAR', 'Filesize': 418082, 'Infotype': 'SAR'},
{'Fastkey': '0030000001666242020', 'Description': 'S4HANAOP105_ERP_LANG_RU.SAR', 'Filesize': 508694, 'Infotype': 'SAR'},
{'Fastkey': '0030000001666252020', 'Description': 'S4HANAOP105_ERP_LANG_SH.SAR', 'Filesize': 378237, 'Infotype': 'SAR'},
{'Fastkey': '0030000001666272020', 'Description': 'S4HANAOP105_ERP_LANG_SK.SAR', 'Filesize': 465519, 'Infotype': 'SAR'},
{'Fastkey': '0030000001666292020', 'Description': 'S4HANAOP105_ERP_LANG_SL.SAR', 'Filesize': 399392, 'Infotype': 'SAR'},
{'Fastkey': '0030000001666322020', 'Description': 'S4HANAOP105_ERP_LANG_SV.SAR', 'Filesize': 434204, 'Infotype': 'SAR'},
{'Fastkey': '0030000001666332020', 'Description': 'S4HANAOP105_ERP_LANG_TH.SAR', 'Filesize': 410497, 'Infotype': 'SAR'}]

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
