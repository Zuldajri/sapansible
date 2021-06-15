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


results = [{'Fastkey': '0020000000381822021', 'Description': 'SAP HANA CLIENT Version 2.7', 'Filesize': 206671, 'Infotype': 'SAR'},
{'Fastkey': '0020000000381762021', 'Description': 'SAP HANA CLIENT Version 2.7', 'Filesize': 125420, 'Infotype': 'SAR'},
{'Fastkey': '0020000000392102021', 'Description': 'Revision 255.00 for SAP HANA STUDIO 2', 'Filesize': 1076514, 'Infotype': 'SAR'},
{'Fastkey': '0020000000392142021', 'Description': 'Revision 255.00 for SAP HANA STUDIO 2', 'Filesize': 1041717, 'Infotype': 'SAR'},
{'Fastkey': '0020000002208852020', 'Description': 'SAPCAR', 'Filesize': 4378, 'Infotype': 'EXE'},
{'Fastkey': '0020000000392162021', 'Description': 'Revision 2.00.055.0 (SPS05) for HANA DB 2.0', 'Filesize': 3611696, 'Infotype': 'SAR'}]

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
