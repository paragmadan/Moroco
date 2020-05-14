from config_edp1_NF import *

def test_getallmsisdn_edp1():
    newurl = url + '?lang=en&offset=0'
    response1 = requests.get(newurl, headers=head,verify=False)
    out1 = response1.text
    existusers = []
    regongoingusers = []
    datas = json.loads(out1)
    #print datas
    for i in range(len(datas['data'])):
        if datas['data'][i]['defaultWalletStatus'] == 'Y':
            existusers.append(datas['data'][i]['msisdn'])
        elif datas['data'][i]['defaultWalletStatus'] == 'Reg Ongoing':
            regongoingusers.append(datas['data'][i]['msisdn'])

    dump_to_csv(datas,test_getallmsisdn.__name__)
    print (existusers, regongoingusers)
