import sys
#print sys.path
#sys.path.append('C:\Users\RZFW9607\PycharmProjects\MOROCS\TestcasesP2PMORROCOW\EDP2testsuite\FINEDP2')
from edp1_config import *
from ..dumptocsv import *
#print(len(sys.path))
from ..FINEDP2scripts.gettangodataedp2 import *


def getTxnStatus(interopId):
    txnsuccess=0
    getTxnStatususrl=url+'transactions/'+interopId+'/en'
    time.sleep(10)
    response=requests.get(getTxnStatususrl,headers=headers,verify=False)
    response=response.text
    assert response.status_code==200
    print response.status_code
    out=json.loads(response)
    len1=len(out['data'])
    assert len(out['data'])!=0,out['message']
    print("Final Transaction Status: "+out['data'][0]['status'])
    if(out['data'][0]['status']=='Transaction Success'):
        transaction_time=out['data'][0]['transactionSubmitTime']
        m=transaction_time.find('.')
        transaction_time=transaction_time[:m]
        print('Transaction Time:'+transaction_time)
        if(str(out['data'][1]['extOrgRefId']).startswith('PP')):
            txnid=out['data'][1]['extOrgRefId']
            txnsuccess=1
            hps_id=''
            edp2_txnid=''
        else:
            txnid=out['data'][3]['extOrgRefId']
            hps_id=out['data'][4]['extOrgRefId']
            print hps_id
            op=getTangoDATA_edp2(transaction_time)
            print(op)
            for i in range(len(op['data'])):

                if(op['data'][i]['transactionStatus']=='TS' and op['data'][i]['hpsstransactionId']==hps_id):
                    print('Transaction was successful')
                    edp2_txnid=op['data'][i]['omTransactionId']
                    txnsuccess=1
                    break
    assert txnsuccess==1,'End to End Transaction Was not successful'
    dump_to_csv(out,'gettxnstatus')
    return txnid,hps_id,edp2_txnid
