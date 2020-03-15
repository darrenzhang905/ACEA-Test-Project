# ACEA-Test-Project
data scraping test project for ACEA

The code is contianed in items.py and inside the spider folder, specifically online_courses.py.
The scraped data is in items.csv

Technique:

I started on the first subject page on onlinecourses.com which was accounting. Using the "view
page source" feature on Google Chrome, I was able to find the CSS selectors to get the course
name and tags. To get access to the URL, I used a Google Chrome extension called Selector Gadget
to find the right selectors. I realized all the subject pages were similiar to I was able to 
scrape all the subject pages on this website. The results are in items.csv.
