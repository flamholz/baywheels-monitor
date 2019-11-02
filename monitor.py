#!/usr/local/bin/python3

import logging
import os
import time
import threading

from urllib.request import urlretrieve
from os import path


def timestamp(): 
	"""Time in ms as a string."""
	return str(int(time.time()*1000))


def save_station_status(interval, status_url, outdir):
	"""Code to run on a fixed interval."""
	out_fname = "station_status_%s.json" % timestamp()
	out_path = path.join(outdir, out_fname)
	logging.info('Saving station status to %s', out_path)
	actual_interval = interval

	try:
		urlretrieve(status_url, out_path)
	except Exception as e:
		logging.error(e)
		logging.info('Backing off by a factor of 2 due to error.')
		actual_interval = interval*2

	logging.info('Scheduling next download in %d minutes', interval/60.0)
	t = threading.Timer(actual_interval, save_station_status,
		args=[interval, status_url, outdir])
	t.start()


if __name__ == '__main__':
	logging.basicConfig(level=logging.DEBUG)

	outdir = 'downloads'
	url = "https://gbfs.baywheels.com/gbfs/en/station_status.json"
	interval = 60*5   # 5 minute interval

	if not path.exists(outdir):
		os.mkdir(outdir)

	save_station_status(interval, url, outdir)



