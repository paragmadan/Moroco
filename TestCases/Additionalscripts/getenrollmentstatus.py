import requests
import json
from TestCases.Additionalscripts.getallmsisdns import *
url='https://interop-qp-oma.admin-paas-om-qualifr.itn.intraorange/edp1interophps/v1/users/'
head={'Authorization': '27512fa7ab591131453147c46b324b015e73eedea0d94697ee8a3863421c931f',
      'accept': 'application/json;charset=UTF-8'}
def get_enrollment_status(p):                                                                          # enroll a msisdn
    newurl = url + '?lang=en&offset=0'
    response1 = requests.get(newurl, headers=head,verify=False)

    # regusers,ongoing=getallmsisdn(out1)                                                              #Get all registered and registeration Ongoing Users

    get_by_msisdn = newurl + '&msisdn=%s' % p


    response2 = requests.get(get_by_msisdn, headers=head,verify=False)



    if response2.status_code == 200:
        out = json.loads(response2.text)
        assert out["code"]=="INTEROP_40078",out["message"]



        return out['data'][0]['interopRefId'],out['data'][0]['defaultWalletStatus']

