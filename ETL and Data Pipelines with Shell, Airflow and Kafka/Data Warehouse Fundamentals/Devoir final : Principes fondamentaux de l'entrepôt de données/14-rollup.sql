select year,city, sum(wastecollected) as totalwastecollected
from "myfacttrips"
left join "mydimdate"
on "myfacttrips".dateid = "mydimdate".dateid
left join "dimstation"
on "myfacttrips".stationid="dimstation".stationid
group by rollup(year,city)
order by year, city;