# [allergeez](https://allergeez.me)

Created for the Houston Hackathon 2018. Check out our [devpost submission](https://devpost.com/software/allergeez).

This application scrapes the Houston Heatlh Department [Pollen and Mold Page](http://www.houstontx.gov/health/Pollen-Mold/index.html)
and saves it in a database. Whenever the database is updated, notifications will be sent if any allergens are above a user's
configured threshold. 

The dashboard displays the most current pollen levels and graphs the last 5 days of data. Users
can choose which allergens they want to see, subscribe to notifications for them, and provide
feedback on how they're feeling.

## Development

### Overview

 * Frontend built in Typescript with Angular (lives in `src/`)
 * Notifications using [Service Workers and Push Notifications](https://blog.angular-university.io/angular-push-notifications/)
 * Scraper written in Python 3 with `BeautifulSoup` and `requests`
 * Data is store in a MySQL database and accessed in Python with `PyMySQL`
 * API serves data and stores user data with `Flask`

### Getting started

 * Install and start MySQL
    * The easiest way to do this with local dev is run `./backend/start_mysql_docker.sh` (requires docker)
 * Install python dependencies with `pip install -r requirements.txt`
 * Create the database tables with `python db.py` 
 * Fill the database with the last five days of data with `python backend/scraper_populate.py`
 * Install npm dependencies with `npm install`
 * Build the frontend with `npm run build`
 * Start the backend server in dev mode with `npm run backend`
 * For automatic reload of the frontend and backend, run `npm run dev`
