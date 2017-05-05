#!/usr/bin/env python2
import calendar
from ecmwfapi import ECMWFDataServer

server = ECMWFDataServer()

"""        
       Change the variables below to adapt the iteration to your needs.
       You can use the variable 'target' to organise
       the outputs. 
       
       period can be 'y' yearly for a single .nc file or monthly 'm' for monthly files.
       Coordinates should be provided in 90 -90 e 180 -180 format
"""
period = 'y'

date = {
        "yearStart" : 1992,
        "yearEnd" : 2015,
        "monthStart" : 01,
        "monthEnd" : 12      
    }
    
coordinates = {
        "nlat" : -3.5,
        "wlon" : -35.,
        "slat" : -11.,
        "elon" : -40.          
    }

 
def retrieve_interim(period, date, coordinates):
 
    # get extent of locations list, plus 5 degrees either side as long as we are within 90/-180/-90/180
    area = [min(coordinates['nlat']+10,90), max(coordinates['wlon']-10,-180), max(coordinates['slat']-10,-90), min(coordinates['elon']+10,180)]

    # make the area list into a string to use it in the met_data_file function
    area = "/".join(map(str, area))
    # test if lat and lon are in valid range  
    
    if period == 'm':
        for year in list(range(date['yearStart'], date['yearEnd'] + 1)):
            for month in list(range(date['monthStart'], date['monthEnd'] + 1)):
                startDate = '%04d%02d%02d' % (year, month, 1)
                numberOfDays = calendar.monthrange(year, month)[1]
                lastDate = '%04d%02d%02d' % (year, month, numberOfDays)
                target = "interimERA_daily_%04d%02d.nc" % (year, month)
                requestDates = (startDate + "/to/" + lastDate)
                interim_request(requestDates, target, area)
    else:
        if period == 'y':
                startDate = '%04d%02d%02d' % (date['yearStart'], date['monthStart'], 1)
                lastDate = '%04d%02d%02d' % (date['yearEnd'], date['monthEnd'], 31)
                target = "interimERA_daily_%04d%02dto%04d%02d.nc" % (date['yearStart'],date['monthStart'], date['yearEnd'], date['monthEnd'])
                requestDates = (startDate + "/to/" + lastDate)
                interim_request(requestDates, target, area)
    
def interim_request(requestDates, target, area):
    """      
        An ERA interim request for analysis total precipitation (228.128) 
        temperature 2m (167.128), mx2t and mn2t
    """
    server.retrieve({
    "class": "ei",
    "dataset": "interim",
    "date": requestDates,
    "expver": "1",
    "grid": "0.75/0.75",
    "levtype": "sfc",
    "param": "167.128/201.128/202.128/228.128",
    "step": "3/6/9/12",	
    "stream": "oper",
    "time": "00:00:00/12:00:00",
    "area" : area,
    "type": "fc",
    "target": target,
    "format": "netcdf",
})

if __name__ == '__main__':
    retrieve_interim(period, date, coordinates)

