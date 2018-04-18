import requests
import csv
from tweeter import Twitter
import sys
import os
from os import environ
import json
import datetime

historyFile = os.path.join(os.path.dirname(__file__), 'riverLevel.csv')

def read_csv():
        with open(historyFile) as csvfile:
                reader = csv.DictReader(csvfile)
                _ = {}
                for row in reader:
                        _['time'] = row['time']
                        _['level'] = row['level']
                if _:
                        return _
                return None

def write_csv(time, level):
        _row = {'time':time, 'level':level}
        with open(historyFile, 'w') as csvfile:
                writer = csv.DictWriter(csvfile,fieldnames=['time','level'])
                writer.writeheader()
                writer.writerow(_row)
        return

def checkWater():
        history = read_csv()
        history['level'] = float(history['level'])
        data = requests.get(url='http://environment.data.gov.uk/flood-monitoring/id/stations/L1607')
        json_data = data.json()
        time = json_data['items']['measures']['latestReading']['dateTime']
        level = float(json_data['items']['measures']['latestReading']['value'])

        if time != history['time']:
                if history['level'] > level:
                        msg = 'River level is at %sM and falling.' % level
                elif history['level'] < level:
                        msg = 'River level is at %sM and rising.' % level
                else:
                        msg = 'River level is at %sM and stable.' % level
                if level >= 0.9:
                        msg += ' Water looks a bit high for rowing.'
                else:
                        msg += ' Water looks ok for rowing.'
                tweeter = Twitter()
                tweeter.tweet(msg)
                write_csv(time, level)

if __name__ == '__main__':
        checkWater()
