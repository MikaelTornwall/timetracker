# Timetracker

## Description

Timetracker is a personal work hour tracking tool for teachers and students. With the tool students can keep track of their daily work hours within all of their courses. Teachers can create courses and monitor student specific course progress.

## Heroku demo

You can try the application demo by using the following credentials:

__Credentials:__

| Email               | Password      | Role     |
| --------------------|---------------|----------|
| `student@email.com` | `student123`  | Student  |
| `teacher@email.com` | `teacher123`  | Teacher  |

Navigate to [login](https://tsoha-timetracker.herokuapp.com/auth/login) and use the credentials above.

## Documentation

More extensive documentation can be found [here](https://github.com/MikaelTornwall/timetracker/blob/master/documentation/documentation.md).

## To do

### CRUD features

__Authentication and authorization__

*General*
- [x] Login

*Student*
- [x] Signup
- [x] Authorization

*Teacher*
- [x] Signup
- [x] Authorization

__Course__

*Student*
- [x] View courses
- [x] View enrolled courses
- [x] Enroll/unenroll on a course (Student)

*Teacher*
- [x] View created courses
- [x] Create courses
- [x] Update courses
- [x] Delete courses
- [x] View course specific enrolled students
- [x] Course specific reports for teachers

__Logs__

*Student*
- [x] View logs
- [x] Create logs
- [x] Update logs
- [x] Delete logs
- [x] View course specific total workhours

*Teacher*
- [x] View course and user specific logs

### Database

*Aggregate queries*
- [x] First aggregate query
- [x] Second aggregate query

### Other features

__Usability and accessibility__

*User interface*
- [x] Forms are constructed properly
- [x] Headers use correct tags

## Installation

[Link to installation instructions](https://github.com/MikaelTornwall/timetracker/blob/master/documentation/installation.md)

## Database

[Link to database details](https://github.com/MikaelTornwall/timetracker/blob/master/documentation/database.md)

For development: SQLite

For production: PostgreSQL

[Link to the SQL queries](https://github.com/MikaelTornwall/timetracker/blob/master/documentation/sqlqueries.md)

### Database chart

![database chart](https://github.com/MikaelTornwall/timetracker/blob/master/documentation/timetracker.png)

[Link to the chart](https://drive.google.com/file/d/176zQnYk9ukeFViq_n_RI6qthSVZ2TaM1/view?usp=sharing)

## Technology stack

* Flask
* Jinja2
* SQLite/PostgreSQL

## Contributors

* [@MikaelTornwall](https://github.com/MikaelTornwall/)
