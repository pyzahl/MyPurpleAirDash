# MyPurpleAirDash

As I am lacking a nice app to have a nice overview of my own sensor station’s data plus have my own logging to a database I created my own setup – in addition to the public sharing to PurpleAir’s map.

Here is how my dashboard looks. Work on a phone’s. browser as great as well.

A little bridging script fetches local json from my PurpleAir and dumps it every 10 minutes into a influx data base. Then a Grafana web front end to present the dash. (Ignore the kWh display, that other data from my PV system…)
