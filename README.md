# TimeTracker

## Description

TimeTracker is a personal work hour tracking tool. Students can keep track of their daily work hours and update logs. Teachers can monitor student specific course progress.

[Link to the demo](https://tsoha-timetracker.herokuapp.com/)

## How to use

### Heroku

Navigate to [login](https://tsoha-timetracker.herokuapp.com/auth/login).

__Credentials:__

| Email               | Password      | Role     |
| --------------------|---------------|----------|
| `student@email.com` | `student123`  | Student  |
| `teacher@email.com` | `teacher123`  | Teacher  |

### How to run locally?

1. Clone repository to your local machine
2. Download dependencies `pip install -r requirements.txt`
3. Run the project `python3 run.py`
4. Navigate to [http://localhost:5000](http://localhost:5000)

## Documentation

More extensive documentation can be found [here](https://github.com/MikaelTornwall/timetracker/blob/master/documentation/documentation.md).

## Features

Authentication and authorization
* General
- [x] Login

* Student
- [x] Signup
- [x] Authorization

* Teacher
- [x] Signup
- [x] Authorization

Course
* Student
- [x] View courses
- [x] View enrolled courses
- [x] Enroll/unenroll on a course (Student)

* Teacher
- [x] View created courses
- [x] Create courses
- [x] Update courses
- [x] Delete courses
- [x] View course specific enrolled students
- [ ] Course specific overview reports for teachers

Logs
* Student
- [x] View logs
- [x] Create logs
- [x] Update logs
- [x] Delete logs
- [x] View course specific total workhours

* Teacher
- [x] View course and user specific logs

## Database

For development: SQLite

For production: PostgreSQL

### Database chart

![database chart](https://github.com/MikaelTornwall/timetracker/blob/master/documentation/timetracker.png)

[Link to the chart](https://drive.google.com/file/d/176zQnYk9ukeFViq_n_RI6qthSVZ2TaM1/view?usp=sharing)

## Technology stack

* Flask
* Jinja2
* SQLite/PostgreSQL

## Contributors

* [@MikaelTornwall](https://github.com/MikaelTornwall/)
