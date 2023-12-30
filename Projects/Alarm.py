## BY This Alarm.py You can add the alarm in your System. Just paste path to any sound in your system .
## It is also can be imported To any Other Py file just by import Alarm
## Made By Kartikey Saran
## Github : @CodeYard01
import datetime
import os
import time
def alarm(timing):
    altime = str(datetime.datetime.now().strptime(timing,"%I:%M %p"))
    altime = altime[11:-3]
    Horeal = altime[:2]
    Horeal = int(Horeal)
    Mireal = altime[3:5]
    Mireal = int(Mireal)
    print(f'Done, Alarm is set for {timing}')

    while True:
        if Horeal==datetime.datetime.now().hour:
            if Mireal==datetime.datetime.now().minute:
                print('Alarm is Ringing')
                os.startfile('path to a ringing sound')
                break
            elif Mireal<datetime.datetime.now().minute:
                break


if __name__=="__main__":
    alarm('3:47 AM')
