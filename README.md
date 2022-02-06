# Open Data -> Twitter Bot Project

## Background Info- 

I was talking with a friend about the need for more technology in Public Safety, and one of the issues we discussed was the lack of knowledge about what the Police actually do. As I was thinking about how to make this more available, I thought of the City of Boulder’s Open Data Hub, which updates daily with all of the calls for service BPD responds to, as well as all the Offenses. How cool would it be to take that data, store it, aggregate it, and tweet it out every day?! Hence, this idea. 
I’m likely doing a lot of things out of order, but ultimately projects like this require a change of focus if I’m continually hitting a roadblock, and I’m just trying to document how I made progress on this. 

Alright- Here we go!

### Step 1: Twitter 101

Set-up of Twitter
Set-up a Twitter account (and make sure to add your phone number, since that is required for development) and then a Twitter developer account as a bot. You won’t need this for several weeks or months, but it feels like a good step to get going on. 
The developer portal is [here](https://developer.twitter.com/en).

### Step 2: ArcGIS API

Work to understand how to get data out of ArcGIS platform. The City of Boulder uses ArcGIS, and has a nice [API explorer](https://open-data.bouldercolorado.gov/datasets/8ef054b1a3ca4ac496d75ec28f17a117_0/api) that generates the Query URL of what you’re looking for. I initially was looking at counts, but realized that Ii'll want to do some aggregation and analysis and thus wanted to pull in Report ID/Incident ID, and Report Date/Incident Date for both Calls for Service and Offenses. Eventually, I'd like to just append records daily instead of requesting every report.

### Step 3: GET -> Python

Convert the API call to Python; I’ll take the small things where I can. Install Postman. Use the Query URL as your Get request, and then when you verify it’s working and returning what you expect,  on the right side, you can choose to see the Code Snippet in Python.
 
### Step 3.99: Install Python

*Accidentally try to go to 4.5 and remember you need to install Python- whoops!*

You can use Anaconda or whatever you like; I ended up just [downloading it](https://python.org). 

### Step 4: Parse JSON to dataframe

I downloaded PyCharm Community Edition (which is free), and after lots (and lots) of googling, parsed and looped through JSON objects, and wrote them out as a pandas dataframe. The code for that is [here](https://github.com/kgbridges/bpd-bot/blob/main/create_dataframe)

*Note to self: Parsing JSON is hard. Kevin reminded me that their interviews for Senior Software Engineers involves parsing JSON, and most people still struggle with it. Be kind to yourself.*

### Step 5: PostGres set-up

Set-up a PostGres database and tables. You can do this in several ways (through command line, installation, etc.) I ended up trying the command line (psql) and getting frustrated, so after I [downloaded](https://www.postgresql.org/download/) it, I set-up an instance locally and I worked in pgAdmin, where I found it easier to set-up the database and an admin account. I also created the two tables I wanted and added the columns and column types. I did verify I could access the database from the command line though. 
To do that, I installed psql, then used: psql <database_name> postgres (and then the password). I was able to log-in and then see <my_database_name>#.  

*Note: Lots of things need to be installed first (including [homebrew](https://brew.sh/), [pip](https://pip.pypa.io/en/stable/installation/), and [psycopg2](https://pypi.org/project/psycopg2/)). I also had issues with old installer versions and importing due to things being in different directories. Make sure you clean everything up (aka upgrade it) if you already have Python installed, and don’t be sloppy about where things are saved.*

*Project for later:*
The PostGres database could also be set-up in Docker, which I may explore later, but for now, am sticking with running it locally to learn. 

—Ok, now all the easy stuff is over :)

### Step 6: 

Write out dataframe to Postgres tables using Python

In trying to do this, I first learned that the PyCharm Community edition no longer allows database connection set-ups, so unless you want to pay, you’ll have to find another way. 

There are also seemingly a million methods, and I couldn’t get any of them to work well. 
