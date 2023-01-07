# simple-web-scraper

![Python package](https://github.com/KenMwaura1/simple-web-scraper/workflows/Python%20package/badge.svg)

This repository contains code for a webscraper for [Lifetime Leaderboards \| UMG Gaming](https://www.umggaming.com/leaderboards)
Making use of the beatifulsoup4 and requests
Postgres as a Database
SQLAlchemy is used as a ORM to insert data into the db

## Accompanying Blog Post

[Get Started with a Web Scraping Project](https://dev.to/ken_mwaura1/getting-started-with-a-web-scraping-project-10ej)

## Installation

1. Clone this Repo

`git clone https://github.com/KenMwaura1/simple-web-scraper`

2. Change into into the simple-web-scraper folder

`cd simple-web-scraper`

3. Create a virtualenv

`python3 -m virtualenv env`

4. Activate virtualenv

`source /bin/activate` OR use pipenv `pipenv install`

5. Install the required dependecies

`python3 -m pip install -r requirements.txt`

## Database

Ensure Postgres is installed locally and running on port 5432

OR

run a Postgres container on Docker [Easy PostgreSQL 10 and pgAdmin 4 Setup with Docker](https://info.crunchydata.com/blog/easy-postgresql-10-and-pgadmin-4-setup-with-docker) container on port 5432

The default db credentials are:

* host: localhost
* port: 5432
* user: test
* db: xp_db
* password: testpassword

Optionally can also set the db credentials as environment variables

```shell
export DATABASE_URL='postgres://test:testpassword@localhost:5432/xp_db'
```

or copy the included .env example file

```shell
cp .env.example .env
```

Add your credentials to the .env file.

## Usage

1.Run the scraper

  1a. To run the scraper and insert xp data into the db

  ```shell
  python xp_scrape.py
  ```

  1b. To run the scraper and insert earnings data into the db

  ```shell
  python earnings_scrape.py
```

## Tests

To run the tests run the following command at the root of the project.

```shell
pytest . 
```
