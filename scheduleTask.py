#!/usr/bin/env python
'''scheduleTask.py: Schedules tasks using schedule lib & time'''

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
