# PrincetonPounceRedux

After I didn't get into a course I wanted, and discovered [Pounce](https://pounce.tigerapps.org/) to be non-functional, I slapped this together: a quick and dirty Twilio-based Princeton enrollment-opening notification service.

Using a trial Twilio account (which is easily created and set up), all one would have to do is update the corresponding token, SSID, and service phone #, to send text messages to yourself if a course were to open.

## Notes about functionality

The following solution is dependent upon the formatting of the course offerings website (the course enrollment is obtained through scraping the site rather than accessing some internal University API), and moreover assumes that the course indicative regarding the enrollment of the course is the first one to appear in the enrollment/section table.  If precepts, for example, were to come before the lecture, then this assumption would break down. 
