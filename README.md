## Python Developer Sample Project

The task is to create a simple web scraper and display the results on a webpage.

Python libraries you will use
- `requests`
- `BeautifulSoup4`
- `flask`

You will be scraping the Auto's section of the New York Daily News website.

- Trucks Page: http://www.nydailynews.com/autos/types/truck
- Sport Page: http://www.nydailynews.com/autos/types/sports-car

Scrape the list of vehicles reviewed (only results page 1) and store them locally (sqlite? json file? etc).

Then, using flask, create a simple webpage endpoint that displays an HTML table showing the title (year/make/model) and summary of the vehicle. You can have 1 table for Trucks, and one for Sport.

This task should be limited to 4 hours maximum, and you will be paid for this time. If you have questions, or get stuck, feel free to reach out and ask us. When the task is complete, please send us a link to a github repository showing your work.

Bonus features:
- Crawl pagination (results page 2, 3, etc of the car lists)
- Crawl vehicle price (how is it loaded into the page? :) )
- Allow the crawler / flask app to be run inside a docker container

## How to run 
`docker-compose up --build -d`

Browser to http://localhost and click to Sport or Truck Models links
