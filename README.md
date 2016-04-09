## csv2ics - Convert a CSV file to a ICS calendar file useable by Mac OS X Calendar

I end up doing a surprising amount of scraping documents and turning them into
calendars. Finally I decided to create something reusable rather than kludging
up a bespoke perl script each time.

### Python Dependencies

* dateparser
* ics
* csv

### Usage

Your CSV file will need the following columns:

* summary - title of your event
* location - the where
* dtstart - start time
* dtend - end time

The times are parsed by the dateparser python module which does pretty well
with a variety of formats.

Here's a typical invocation:

```
$ head out.csv 
summary,location,dtstart,dtend
AI: A Return to Meaning,Salon A,2016 April 11 8:45 AM EDT,2016 April 11 9:45 AM EDT
"Realm - a New, Easy to Use Mobile Database & Object Framework",Salon A,2016
April 11 10:15 AM EDT,2016 April 11 11:15 AM EDT
From Zero to Application Delivery with NixOS,Salon B,2016 April 11 10:15 AM
EDT,2016 April 11 11:15 AM EDT
...
$ ./csv2ics.py <out.csv >out.ics
$ open out.ics
```
