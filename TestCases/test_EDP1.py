#!/usr/bin/python
# -*- coding: utf-8 -*-

from Additionalscripts.FINscripts.excelobjlib import *
import requests
import json
import random
import time
from Additionalscripts.dumptocsv import *
import os
import ssl
import pytest
from Additionalscripts.FINscripts.gettxnstatus import *
from Additionalscripts.getenrollmentstatus import *
from Additionalscripts.FINscripts.txncorredp1 import *
from Additionalscripts.FINEDP2scripts.txncorredp2 import *
head = \
    {'Authorization': '27512fa7ab591131453147c46b324b015e73eedea0d94697ee8a3863421c931f',
     'accept': 'application/json;charset=UTF-8'}


@pytest.fixture()
def fixture_NF(scope='module'):
    global url_nonfin
    url_nonfin = \
        'https://interop-qp-oma.admin-paas-om-qualifr.itn.intraorange/edp1interophps/v1/users/'


@pytest.fixture()
def fixture_FIN(scope='module'):
    global url_fin
    url_fin = \
        'https://interop-qp-oma.admin-paas-om-qualifr.itn.intraorange/edp1interophpstxn/v1/'


def test_initenroll_NF(fixture_NF):
    refid = random.randrange(1, 10000)
    lang = 'en'
    fl = open("ConfigEDP1\msisdns_edp1.txt", 'r')
    lns = fl.readlines()
    msisdns = []
    for i in lns:
        msisdns.append(i.strip())

        # print(i)

    print msisdns

    # enrolluserinit('asdasdsa')

    # msisdn=str(raw_input("Enter Msisdn"))

    fl2 = open('ConfigEDP1/interop_ids_edp1.txt', 'w')
    fl3 = open('ConfigEDP1/confirminteropids.txt', 'w')
    for msisdn in msisdns:
        reqs = 'ussd'
        enrollurl = url_nonfin
        mdata = {
            'extOrgRefId': refid,
            'lang': lang,
            'msisdn': msisdn,
            'requestSource': 'ussd',
        }

        # print(type(mdata),type(head))

        response = requests.post(enrollurl, json=mdata, headers=head,
                                 verify=False)
        assert response.status_code == 200

        # print(response.text)
        # print(response.content)
        # print(response.status_code)
        # print(response.content)
        # assert response.status_code

        time.sleep(8)
        myd = json.loads(response.text)

        # print myd
        # print(response.content)

        assert myd['code'] == 'HPS_00000', myd['message']

        fl2.write(myd['msisdn'] + ',' + myd['interopRefId'] + ','
                  + myd['message'] + '\n')
        fl3.write(myd['msisdn'] + ',' + myd['interopRefId'] + '\n')

        # messages.append(myd['msisdn'], myd['interopRefId'])
        # return interop_id

    fl2.close()
    fl3.close()


def test_confirmenrollment_NF(fixture_NF):

    # confirmenrollment(interop_id)

    fl = open('ConfigEDP1/interop_ids_edp1.txt', 'r')

    lns = fl.readlines()
    for i in lns:
        i.strip()
        if not i.startswith('#'):
            arr = i.strip().split(',')
            print len(arr)
            assert arr[2].strip() == 'SUCCESS'
    fl2 = open('ConfigEDP1/confirminteropids.txt', 'r')
    lns2 = fl2.readlines()
    for i in lns2:
        i = i.strip()
        if i.startswith('#'):
            continue
        arr2 = i.split(',')
        otp = arr2[2].strip()
        conf_url = '%s/activation' % arr2[1]
        conf_url_data = {'lang': 'en', 'otp': otp}
        response = requests.post(url_nonfin + conf_url,
                                 json=conf_url_data, headers=head,
                                 verify=False)
        output = json.loads(response.text)

        # print(output)

        assert output['code'] == 'HPS_00000', \
            'REGISTERATION UNSUCCESSFUL BECAUSE ' + output['message']


def test_deleteuser_NF(fixture_NF):  # Function To Delete(Unenroll) a User

    # enrolluser()

    fl = open('ConfigEDP1\msisdndel_edp1.txt', 'r')
    msisdns = []
    lns = fl.readlines()
    for i in lns:
        msisdns.append(i.strip())
    for msisdn in msisdns:
        print msisdn
        (interop_id, status_1) = get_enrollment_status(msisdn)
        if interop_id:
            delete_user_url = url_nonfin + interop_id \
                              + '?reasonCode=03&lang=en'
            response_d = requests.delete(delete_user_url, headers=head,
                                         verify=False)
            out = json.loads(response_d.text)
            assert response_d.status_code == 200
            assert out['code'] == 'HPS_00000', out['message']


            # FINANCIAL FUNCTIONS
##################################################################################################################

def test_gettechnicalwallet_FIN(fixture_FIN):

    newurl = url_fin + 'MA/technical%E2%80%90wallets'
    print newurl

    response = requests.get(newurl, headers=head, verify=False)
    Out = response.text
    Out = json.loads(Out)

    # for i in Out["data"]:

    print Out
    print 'TECHNICAL WALLET MSISDN: ' + str(Out['data'][0]['msisdn'])


def test_createTransaction_FIN(fixture_FIN):
    createtxnurl = url_fin + 'transactions/'

    # for i in range(0,1):                        #no. of transactions to be performed

    txnid = ''
    fltxncor = open('txncorrfile.txt', 'w')
    file = open("C:\Users\RZFW9607\Desktop\p2p_1_edp1.json", 'r')
    json_input = file.read()
    req_json = json.loads(json_input)
    xlobj = xl('C:\\Users\\RZFW9607\\Desktop\\createtxn.xlsx', 'Sheet1')
    rows = xlobj.no_of_rows()
    colms = xlobj.no_of_cols()
    fl2 = open('C:\\Users\\RZFW9607\\Desktop\\smp.json', 'w')
    fln = open('txnidfile.txt', 'w')
    ls = xlobj.get_keys()

    # print(ls)

    print rows
    for i in range(2, rows + 1):

        # print("i====================================================={}".format(i))

        new_json_input = xlobj.get_data_per_row(req_json, i, ls)

        # new_json_input= json.loads(str(new_json_input))
        # fl2.write(str(new_json_input))(
        # print new_json_input
        # new_json_input['creditParty']=str(new_json_input['creditParty'])
        # print new_json_input['creditParty']
        # print new_json_input

        print 'Request:' + str(new_json_input)
        response = requests.post(createtxnurl, headers=headers,
                                 json=new_json_input, verify=False)

        # print(response.status_code)

        print response.status_code
        print 'Response' + response.content

        # print(response)

        response = response.text

        # print response

        out = json.loads(response)

        # print('asdasdadadasa')

        print out
        assert out['code'] == 'INTEROP_50046' or out['code'] \
               == 'BROKER_200', out['message']
        assert out['status'] == 'TS', out['message']
        interop_id = out['interopRefId']
        print out['message']

        # assert(out["code"]=='INTEROP_50046')

        # txnid=out["message"]
        # txnid=txnid[index:index+20]
        # print('Transaction Id:'+txnid)

        myfl = 0
        print 'Waiting to Generate Results ...'
        txnid, hps_id, edp2_txn_id = getTxnStatus(interop_id)

        # time.sleep(50)

        file.close()

        fln.write(txnid + ',' + ',' + hps_id + ',' + edp2_txn_id)
    fln.close()


def test_txncorr_edp1_FIN(fixture_FIN):
    filen=open('txncorrfile.txt','r')
    #tc_id2={}
    #tc_id1={}
    tc_result_file=open('tc_result.txt','w')
    lines=filen.readlines()
    assert len(lines)!=0,"Transaction did not happen therefore cannot proceed with Correction"
    for line in lines:
        line=line.split(',')
        if line[0].startswith('PP'):
            tc_id1[line[0]]=txnCorr_edp1(line[0])
            tc_result_file.write(line[0]+":  "+tc_id1)
        elif line[0].startswith('CO'):
            tc_id2[line[2]]=txnCorr_edp2(line[2])
            tc_id1[line[0]]=txnCorr_edp1(line[0])
            tc_result_file.write(line[0]+":  "+tc_id1+" , "+line[2]+":  "+tc_id1)
        #elif line.startswith('CO'):

