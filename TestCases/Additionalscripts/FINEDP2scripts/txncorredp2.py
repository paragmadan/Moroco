
from config_edp2 import *
def txnCorr_edp2(txnid):
    txnCorrUrl=url+'transactions/txn_correction?transactionId='+txnid
    response=requests.post(txnCorrUrl,headers=headers,verify=False)
    op=json.loads(response.text)
    #print(op)
    if(response.status_code!=200):
        print("Some error Occured : "+op["message"])
    else:
        response=response.text
        out=json.loads(response)
        assert out['transactionId']!=None,"Some error while performing TC"
        return out['transactionId']
