#!/usr/bin/python
# -*- coding: utf-8 -*-
import requests
import json
import random
import time
from dumptocsv import *
import os, ssl



#url = 'http://localhost:9001/v1/users/'                                                                 # URL WHERE NON-FINANCIAL REQUEST HITS
url='https://interop-qp-oma.admin-paas-om-qualifr.itn.intraorange/edp1interophps/v1/users/'
# urlext=url+'?lang=en&offset=0&limit=10'

head = \
    {'Authorization': '27512fa7ab591131453147c46b324b015e73eedea0d94697ee8a3863421c931f',
     'accept': 'application/json;charset=UTF-8'}                                                       #AUTHORIZATION and ACCEPR REQUEST PASSED AS HEADER TO GET REQUSET
