#!/usr/bin/env python3
# 
#       SMP Downloader
#
#

import json
import os.path

import requests
from requests.adapters import HTTPAdapter


class HTTPSession(requests.Session):
    def __init__(self, auth=None, headers=None, retry=5):
        super(HTTPSession, self).__init__()
        if auth:
            self.auth    = auth
        if headers:
            self.headers = headers
        if Config.debug.proxies:
            self.proxies = Config.debug.proxies
        if Config.debug.cert:
            self.verify  = Config.debug.cert
        adapter = HTTPAdapter(max_retries=retry)
        self.mount("http://", adapter)
        self.mount("https://", adapter)


class ConfigSection(object):
    param   = {}
    iterpos = 0
    def __init__(self, *args, **kwargs):
        dictionary = {}
        if args:
            dictionary    = args[0]
        elif kwargs:
            dictionary    = kwargs
        for k in list(dictionary.keys()):
            self.param[k] = dictionary[k]
            setattr(self, k, self.param[k])

    def __iter__(self):
        return self

    def __next__(self):
        if self.iterpos < len(list(self.param.keys())):
            k = list(self.param.keys())[self.iterpos]
            v = self.param[k]
            self.iterpos += 1
            return {k: v}
        else:
            raise StopIteration


class Config(object):
    debug   = ConfigSection(
        cert    = None,
        proxies = None,
    )
    credentials = ConfigSection(
        sap_user     = None,
        sap_password = None,
    )
    scenarios    = []
    app_scenario = None
    db_scenario  = None
    rti_scenario = None
    bastion_os   = []

    @staticmethod
    def load(filename):
        assert(os.path.isfile(filename)), \
            "Config file %s does not exist" % filename

        with open(filename) as f:
            input_json = json.load(f)

        assert(("software" in input_json and "downloader" in input_json["software"])), \
            "Software and downloader fields are required in input.json"

        data = input_json["software"]["downloader"]

        # Debug section
        if "debug" in data:
            if "enabled" in data["debug"] and data["debug"]["enabled"]:
                Config.debug = ConfigSection(
                    proxies = data["debug"]["proxies"] if "proxies" in data["debug"] else None,
                    cert  = data["debug"]["cert"] if "cert" in data["debug"] else None
                )

        # Credentials section
        assert("credentials" in data and \
            "sap_user" in data["credentials"] and \
            "sap_password" in data["credentials"]), \
            "SAP credentials need to be specified"
        Config.credentials = ConfigSection(
            sap_user    = data["credentials"]["sap_user"],
            sap_password  = data["credentials"]["sap_password"]
        )

       
