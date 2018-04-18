import datetime
import matplotlib as mpl
mpl.use('Agg')
import matplotlib.pyplot as plt
import matplotlib.dates as mdates
import requests
import os

from tweeter import Twitter

graphFile = os.path.join(os.path.dirname(__file__), 'riverLevel.png')

def dailyGraph():

        data = requests.get(url='http://environment.data.gov.uk/flood-monitoring/id/stations/L1607/readings?since=%s' % datetime.date.today())
        data = data.json()
        data = {datetime.datetime.strptime(d['dateTime'],'%Y-%m-%dT%H:%M:%SZ'):d['value'] for d in data['items']}
        times = sorted(data.keys())
        values = [data[x] for x in times]

        plt.plot(times,values)
        axis = plt.gca()

        axis.xaxis.set_major_formatter(mdates.DateFormatter('%H:%M'))
        axis.xaxis.set_major_locator(mdates.HourLocator(interval=2))
        axis.set_xlabel('Time')
        axis.set_ylabel('Level')
        axis.set_title('River level for: %s' % (str(datetime.date.today())))

        plt.gcf().autofmt_xdate()

        plt.savefig(graphFile)
        
	tweeter = Twitter()
        tweeter.tweet('River level for: %s' % (str(datetime.date.today())), graphFile)

if __name__ == '__main__':
	dailyGraph()

