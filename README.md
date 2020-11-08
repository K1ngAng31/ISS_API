# ISS_API

First API Mini-Project

This was a fun API project that used:
- http://api.open-notify.org/iss-pass.json (1)
- http://api.open-notify.org/astros.json (2)

Libraries used:
- Pandas as pd
- requests as rq
- json
- from datetime import datetime

I took in the response using requests.get() to find the current people in space and when the ISS will pass next. 

I aslo created a states.csv file that has the state abreviation, lat, and lon. This was used to pass as paramaters to our API(2).
This allowed for outputing duration and risetime. 
Then I used the datetime library to conver the risetime timestamp format to datetime. This is to be more comprehnesible to the public.

When running this file on your terinal or on an editor, it will ask you to enter a state, please used an abbreviated form. 

Some potential changes:
- When a wrong abbreviation is entered, give a warning and ask to do it again. 
- Add a loop so user can keep entering states after state has output information.

