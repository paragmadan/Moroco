from config_edp2 import *
def getTangoDATA_edp2(dt):       #date in format YYYY-MM-DDTHH:MM:
    #print('2020-04-28T14:16:08')
    #print(dt)
    # For reconcilation Between Tango and ADD ON
    dt=dt.split('T')
    dts2=dt[1].split(':')
    #fromdate = raw_input('Enter Date separated by - (YYYY-MM-DD)')
    gettangodataurl = url \
                      + 'MO/om-transactions?from={}T{}%3A{}%3A{}Z&limit=100'.format(dt[0],dts2[0],dts2[1],dts2[2])  # MA is the country code that can be changed as per req.
    print gettangodataurl
    response = requests.get(gettangodataurl, headers=headers,verify=False)
    output = response.text
    output1 = json.loads(output)
    return output1
