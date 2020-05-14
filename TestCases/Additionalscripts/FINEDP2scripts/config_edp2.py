#!/usr/bin/python
# -*- coding: utf-8 -*-
import requests
import json
import csv
import os
import time
#import datetime

from ..dumptocsv import *
import time
url = 'https://interop-qp-oma.admin-paas-om-qualifr.itn.intraorange/edp2interophpstxn/v1/'
headers = \
    {'Authorization': '27512fa7ab591131453147c46b324b015e73eedea0d94697ee8a3863421c931f'}
