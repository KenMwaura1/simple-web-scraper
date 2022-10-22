# simple-web-scraper

![Python package](https://github.com/KenMwaura1/simple-web-scraper/workflows/Python%20package/badge.svg)

This repository contains code for a webscraper for [Lifetime Leaderboards \| UMG Gaming](https://www.umggaming.com/leaderboards)
Making use of the beatifulsoup4 and requests
Postgres as a Database
SQLAlchemy is used as a ORM to insert data into the db

## Installation

1.Clone this Repo

`git clone https://github.com/KenMwaura1/simple-web-scraper`

2.Cd into the simple-web-scraper folder

`cd simple-web-scraper`

3.Create a virtualenv

`python3 -m virtualenv env`

4.Activate virtualenv

`source /bin/activate` OR use pipenv `pipenv install`

5.Install the required dependecies

`python -m pip install -r requirements.txt`

## Database

Ensure Postgres is installed and running on port 5432

OR

run a Postgres docker ([Easy PostgreSQL 10 and pgAdmin 4 Setup with Docker](https://info.crunchydata.com/blog/easy-postgresql-10-and-pgadmin-4-setup-with-docker) ) container on port 5432

The default db credentials are host: localhost port: 5432 user: test db: scrapedb password: testpaassword
Optionally can also set the db credentials as environment variables

`export DATABASE_URL='postgres://test:testpassword@localhost:5432/scrapedb'`

## Usage

1.Run the scraper

`python scrape.py`
