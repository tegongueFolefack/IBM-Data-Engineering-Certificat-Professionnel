select year,city, AVG(wastecollected)
from "myfacttrips"
left join "mydimdate"
on "myfacttrips".dateid = "mydimdate".dateid
left join "dimstation"
on "myfacttrips".stationid="dimstation".stationid
group by cube(year,city)
order by year, city;