import requests
def changepassword():                                  #not tested yet dangerous to test
    newurl='https://interop-qp-oma.admin-paas-om-qualifr.itn.intraorange/edp1interophps/v1/edp/changePassword'
    newpass=raw_input("Please enter new password")
    mydata={"edpNewPassword": newpass}
    response=requests.post(newurl,json=mydata,headers=head,vverify=False)
    print(response.text)
