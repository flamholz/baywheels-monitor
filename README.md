# baywheels-monitor

Code for continuous downloading and subsequent analysis of BayWheels station status information. BayWheels API is, fortunately, in the [General Bikeshare Feed Specification](https://github.com/NABSA/gbfs/blob/master/gbfs.md) JSON format and more details can be found on [their website](https://www.lyft.com/bikes/bay-wheels/system-data). 

See: 
* monitor.py for continuous API downloading code.
* data/stations_timeseries.csv.zip for the parsed data. It's a big file.
* notebooks/1_process_downloads.ipynb for parsing BayWheels data into a spreadsheet.
* notebooks/2_station_analysis.ipynb for analysis and plotting.