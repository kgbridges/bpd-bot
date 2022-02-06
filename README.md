##Open Data -> Twitter Bot Project

#Background Info- 

I was talking with a friend about the need for more technology in Public Safety, and one of the issues we discussed was the lack of knowledge about what the Police actually do. As I was thinking about how to make this more available, I thought of the City of Boulder’s Open Data Hub, which updates daily with all of the calls for service BPD responds to, as well as all the Offenses. How cool would it be to take that data, store it, aggregate it, and tweet it out every day?! Hence, this idea. 
I’m likely doing a lot of things out of order, but ultimately projects like this require a change of focus if I’m continually hitting a roadblock, and I’m just trying to document how I made progress on this. 

Alright- Here we go!

#Step 1: 
Easy set-up of Twitter
Set-up a Twitter develop account as a bot. You won’t need this for several weeks or months, but it feels like a good step to get going on. 

The developer portal is here, and you’ll also need to create a separate Twitter account if you don’t already have one for the project (and make sure to add your phone number, since that is required for development). 

Still to do here: actually feed data in and create and schedule tweets. Small Steps. 

#Step 2: 
Work to understand how to get initial data out of ArcGIS platform. The City of Boulder uses ArcGIS, and has a nice API explorer that generates the Query URL of what you’re looking for. I initially was just looking at counts, but I realized later that I wanted to do the count myself and thus wanted to pull in Report ID/Incident ID, and Report Date/Incident Date for both Calls for Service and Offenses. I want to pull everything in initially, with the hope of just appending new records once everything is up and going. 

#Step 3: 
Maybe this is cheating, but who really cares. I’ll take the small things where I can. Install Postman. Use the Query URL as your Get request, and then when you verify it’s working and returning what you expect,  on the right side, you can choose to see the Code Snippet in Python.
 
#Step 4: 
Accidentally try to go to 4.5 and remember you need to install Python- whoops! You can use Anaconda or whatever you like; I ended up just downloading through python.org

#Step 4.5: 
This one may change later, but for now, I was looking for a Python IDE that would let me do some further editing on the snippet above (essentially just pull in arrays for each ID/Date that I could insert into a table). I downloaded PyCharm Community Edition, and after lots (and lots) of googling, finally figured out how to parse and loop through the JSON object. The code below provided arrays for each incident for Offenses:

Note to self: parsing JSON is hard. Kevin reminded me that their interviews for Senior Software Engineers involves parsing JSON, and most people still struggle with it. Ergh, but patience… 

#Step 5: 
Set-up a PostGres database and tables. You can do this in several ways (through command line, installation, etc.) I ended up trying the command line (psql) and getting frustrated, so after I downloaded it, I set-up an instance locally and I worked in pgAdmin, where I found it easier to set-up the database and an admin account. I also created the two tables I wanted and added the columns and column types. I did verify I could access the database from the command line though. 
To do that, I installed psql, then used: psql <database_name> postgres (and then the password). I was able to log-in and then see <my_database_name>#.  
Note: there are lots of things that need to be installed first (including homebrew, pip, and psycopg2). I seemed to have a lot of issues with old installer versions and importing once installed due to things being in different locations. Make sure you clean everything up (aka upgrade it) if you already have it installed, and don’t be sloppy about the directories things are saved in. 
Note: You could also set-up a PostGres database in Docker, which I may explore later, but for now, I think locally is fine to learn with. 

—Ok, now all the easy stuff is over :)

#Step 6: 
Write out dataframe to Postgres tables using Python

In trying to do this, I first learned that the PyCharm Community edition no longer allows database connection set-ups, so unless you want to pay, you’ll have to find another way. 

There are also seemingly a million methods, and I couldn’t get any of them to work well. 
