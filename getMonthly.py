#!/usr/bin/env python2
import calendar
from ecmwfapi import ECMWFDataServer
server = ECMWFDataServer()
 
def retrieve_interim():
    """        
       Change the variables below to adapt the iteration to your needs.
       You can use the variable 'target' to organise
       the outputs (in this case, all reanalysis will be wrote 
       in the format "interimERA_daily_YYYYMM.nc")
    """
    yearStart = 2014
    yearEnd = 2014
    monthStart = 1
    monthEnd = 3
    
    
    for year in list(range(yearStart, yearEnd + 1)):
        for month in list(range(monthStart, monthEnd + 1)):
            startDate = '%04d%02d%02d' % (year, month, 1)
            numberOfDays = calendar.monthrange(year, month)[1]
            lastDate = '%04d%02d%02d' % (year, month, numberOfDays)
            target = "interimERA_daily_%04d%02d.nc" % (year, month)
            requestDates = (startDate + "/TO/" + lastDate)
            interim_request(requestDates, target)
 
def interim_request(requestDates, target):
    """      
        An ERA interim request for analysis total precipitation (228.228) 
        and temperature 2m (167.128).
    """
    server.retrieve({
   "class": "ei",
    "dataset": "interim",
    "date": requestDates,
    "expver": "1",
    "grid": "0.75/0.75",
    "levtype": "sfc",
    "param": "228.128/167.128",
    "step": "12",
    "stream": "oper",
    "time": "00:00:00/12:00:00",
    "type": "fc",
    "target": target,
    "format": "netcdf",
})

if __name__ == '__main__':
    retrieve_interim()