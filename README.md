# [allergeez](https://allergeez.me)

Created for the Houston Hackathon 2018. Check out our [devpost submission](https://devpost.com/software/allergeez)

## Development

### Overview

 * Frontend built in Typescript with Angular (lives in `src/`)
 * Notifications using [Service Workers and Push Notifications](https://blog.angular-university.io/angular-push-notifications/)
 * Scraper written in Python 3 with `BeautifulSoup` and `requests`
 * Data is store in a MySQL database and accessed in Python with `PyMySQL`
 * API serves data and stores user data with Flask

### Getting started

 * Install and start MySQL
    * The easiest way to do this with local dev is run `./backend/start_mysql_docker.sh` (requires docker)
 * Install python dependencies with `pip install -r requirements.txt`
 * Create the database tables with `python db.py` 
 * Fill the database with the last five days of data with `python backend/scraper_populate.py`
 * Install npm dependencies with `npm install`
 * Build the frontend with `npm run build`
 * Start the backend server with `FLASK_ENV=development FLASK_APP=backend/server.py flask run`

