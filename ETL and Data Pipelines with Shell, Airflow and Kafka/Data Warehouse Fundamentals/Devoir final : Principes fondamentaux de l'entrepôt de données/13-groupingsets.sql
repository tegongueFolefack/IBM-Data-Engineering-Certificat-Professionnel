SELECT 
    myfacttrips.stationid,
    mydimtruck.trucktype,
    SUM(myfacttrips.wastecollected) AS totalwastecollected
FROM 
    myfacttrips
LEFT JOIN 
    dimstation
ON 
    myfacttrips.stationid = dimstation.stationid
LEFT JOIN 
    mydimtruck
ON 
    myfacttrips.truckid = mydimtruck.truckid
GROUP BY 
    GROUPING SETS (myfacttrips.stationid, mydimtruck.trucktype);
