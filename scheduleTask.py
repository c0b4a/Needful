#!/usr/bin/env python
'''scheduleTask.py: Schedules tasks using schedule lib & time'''

__author__ = 'ISAIAH COLEMAN'
__credits__ = ['Isaiah Coleman']
__status__ = 'Prototype'

#imports
import schedule
import time

def job():
    print('Working')

#ways to schedule
schedule.every(20).seconds.do(job)
schedule.every().hour.do(job)

while True:
    schedule.run_pending()
    time.sleep(1)
