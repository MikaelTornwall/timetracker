# TimeTracker

## Description

TimeTracker is a personal work hour tracking tool. Students can keep track of their daily working hours and update logs. Teachers can monitor student specific course progress. Courses also have a target duration that students should achieve.

[Link to the demo](https://tsoha-timetracker.herokuapp.com/)

## How to run locally?

1. Clone repository to your local machine
2. Download dependencies `pip install -r requirements.txt`
3. Run the project `python3 run.py`
4. Navigate to [http://localhost:5000](http://localhost:5000)

## Features

* Registration
  - [ ] Teacher
  - [ ] Student
* Login
  - [ ] Teacher
  - [ ] Student
- [ ] Creating courses
- [ ] Logging work hours with duration and description
- [ ] Updating log duration and description
- [ ] Deleting logs
- [ ] Adding students and teachers to courses
- [ ] Deleting students and teachers from courses
- [ ] Deleting courses
- [ ] Course specific overview reports for teachers

## Database

For development: SQLite

For production: PostgreSQL

### Database chart

![database chart](https://github.com/MikaelTornwall/timetracker/blob/master/timetracker.png)

[Link to the chart](https://drive.google.com/file/d/176zQnYk9ukeFViq_n_RI6qthSVZ2TaM1/view?usp=sharing)

## Technology stack

* Flask
* Jinja2
* SQLite/PostgreSQL

## Contributors

* [@MikaelTornwall](https://github.com/MikaelTornwall/)
