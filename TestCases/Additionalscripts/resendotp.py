from getenrollmentstatus import *
def resendotp(msisdn):                                                                                                  #Function To resend OTP


    interop_id,status = get_enrollment_status(msisdn)
    print(interop_id)
    assert status=='Reg Ongoing','No registeration is ongoing for the user'
    resendotp_url = url + str(interop_id) + "/otpResend"
    data={ "lang": "en"}
    response=requests.post(resendotp_url, headers=head, json=data,verify=False)
    response=json.loads(response.text)
    print(response['message'])


resendotp('0616212314')
