# Database

On this page you can find some further information about the database. First I'm going to highlight some important details and provide some instructions on how to use the database management systems. Below that can be found the database chart and a link to important SQL queries.

## Normalization and special characteristics

The database has been normalized and, to my understanding, satisfies the third normal form. However, there are some details I want to highlight:

__Account__

Account has two candidate keys: *id* and *email*, since *email* attribute is unique. I wanted to use *id* as the primary key, since all the other tables use it as well, and this also allowed using the same abstract class as a parent as other classes did.

__Course__

Course table contains primary key *id* and *course_id*. It's important to notice, that these two keys are completely separate attributes and *course_id* is not necessarily unique, especially if the tool gets expanded and allows multiple organizations.

## How to open the database management system

### On your local machine

Locally the application uses SQLite database management system. After setting up the application locally [(instructions on how install the application locally)](https://github.com/MikaelTornwall/timetracker/blob/master/documentation/installation.md#locally), follow these steps:

1. Open command line and navigate to project root
2. Navigate to application folder `$ cd application`
3. Start database management system `$ sqlite3 logs.db`

### In Heroku

In Heroku the application uses the PostgreSQL HobbyDev -package provided by Heroku. After setting up the application in Heroku [(instructions on how install the application in Heroku)](https://github.com/MikaelTornwall/timetracker/blob/master/documentation/installation.md#heroku), follow these steps:

1. Open command line and navigate to project root
2. Navigate to application folder `$ cd application`
3. Start database management system `$ heroku pg:psql`

## Database chart

![database chart](https://github.com/MikaelTornwall/timetracker/blob/master/documentation/timetracker.png)

[Link to the chart](https://drive.google.com/file/d/176zQnYk9ukeFViq_n_RI6qthSVZ2TaM1/view?usp=sharing)

## SQL queries

[CREATE TABLE and aggregate queries](https://github.com/MikaelTornwall/timetracker/blob/master/documentation/sqlqueries.md)
