# Creating a Twitter bot to show the calls for service and offenses that BPD responds to (daily)

## Using Open Data to create a tweet
This project is my first attempt at lots of things; I'll be using ESRI's REST API to pull the City of Boulder's Open Data on BPD Calls for Service and Offenses. 

Using Python, I'll update the date in the API call daily, and write it out to MongoDB. 

I'll use the maximum date (in both calls for service and offenses data) from these tables to create a tweet for that day, giving the count of calls for service and offenses. 

### Wny?

Police analytics are important, and being able to access them via OpenData is awesome. This is a small attempt to show folks across the community all of the work that BPD does in a slightly more accessible way (er... people use Twitter, right?)

### Other Notes

I'm starting from 0 here so lots of things to do-

-Twitter developer account (and tokens)
-Install Python3 and necessary packages
-Create MongoDB/Atlas account
