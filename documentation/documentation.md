# TimeTracker

## Overview

Personal work hour tracking tool.

## Table of contents

1. [Description](#description)
2. [How to run](#howtorun)
    1. [Heroku](#heroku)
    2. [Locally](#locally)
3. [Use cases](#usecases)  
    1. [User groups](#usergroups)
    2. [User stories](#userstories)
    3. [Structure](#structure)
4. [Database](#database)
    1. [Database chart](#chart)
5. [Technology stack](#techstack)
6. [Contributors](#contributors)

<a name="description"></a>
## 1. Description

TimeTracker is a personal work hour tracking tool. Students can keep track of their daily working hours and update logs. Teachers can monitor student specific course progress. Courses also have a target duration that students should achieve.

[Link to the demo](https://tsoha-timetracker.herokuapp.com/)

<a name="howtorun"></a>
## 2. How to run

<a name="heroku"></a>
### 2.1. Heroku

Navigate to [login](https://tsoha-timetracker.herokuapp.com/auth/login).

__Credentials:__

| Email               | Password      | Role     |
| --------------------|---------------|----------|
| `student@email.com` | `student123`  | Student  |
| `teacher@email.com` | `teacher123`  | Teacher  |

<a name="locally"></a>
### 2.2. Locally

1. Clone repository to your local machine
2. Download dependencies `pip install -r requirements.txt`
3. Run the project `python3 run.py`
4. Navigate to [http://localhost:5000](http://localhost:5000)

<a name="usecases"></a>
## 3. Use cases

<a name="usergroups"></a>
### 3.1. User groups

__3.1.1. Student__

Any person who want's to log their progress on a course that exists within the tool.

__3.1.2. Teacher__

Any person who wants to supervise a course or a project.

<a name="userstories"></a>
### 3.2. User stories

__3.2.1. Student__

As a student I can
 - Log in to the tool
 - Enroll/unenroll myself to a course
 - See all courses within the tool
 - See all the courses I have enrolled on
 - See all my course specific logs and total workhours
 - Create a log that contains the description of the tasks I have done today, the duration it took to complete those tasks and today's date
 - Add hours to the duration of the specific day's log I have created
 - Update any logs I have created by modifying the description and duration
 - Delete any log I have created

__3.2.2. Teacher__

 As a teacher I can
  - Log in to the tool
  - Create new courses so that students can log their progress
  - See who's participating in any course I'm responsible for
  - See an overview of any of my courses
  - See course progress of a specific student within a specific course
  - Update any of course's details
  - Delete any of my courses

<a name="structure"></a>
### 3.3. Structure

Structure of the tool and features of each page for student and teacher accounts:

Homepage: _/_
- Tool's description and navigation bar for registration and login

__Student__

_/auth/signup/student/_
- Create a new student account

_/auth/login/_
- Log in to the tool

_/courses/_
- View all the courses
- Enroll/unenroll on a course

_/courses/:courseId_
- View course details
- Enroll/unenroll on a course

_/logs/_
- View all the courses the student is registered for

_/:courseId/logs/_
- Track progress on a specific course or project
- View all the logs and increase the duration of a log

_/:courseId/logs/:logId/_
- Update or delete a log

_/:courseId/new/_
- Create a new log for a specific course


__Teacher__

_/auth/signup/teacher/_
- Create a new teacher account

_/auth/login/_
- Log in to the tool

_/courses/mycourses/_
- View all the courses the teacher is responsible for

_/courses/new/_
- Create a new course

_/courses/:courseId/_
- View an overview of a specific course, such as number of participants
- Delete the course
- View a list of students who participate to this course

_/courses/:courseId/edit/_
- Edit the course details

_/:courseId/logs/:studentId/_
- View course specific logs of a student

<a name="database"></a>
## 4. Database

For development: SQLite

For production: PostgreSQL

<a name="chart"></a>
### 4.1. Database chart

![database chart](https://github.com/MikaelTornwall/timetracker/blob/master/documentation/timetracker.png)

[Link to the chart](https://drive.google.com/file/d/176zQnYk9ukeFViq_n_RI6qthSVZ2TaM1/view?usp=sharing)

<a name="techstack"></a>
## 5. Technology stack

* Flask
* Jinja2
* SQLite/PostgreSQL

<a name="contributors"></a>
## 6. Contributors

* [@MikaelTornwall](https://github.com/MikaelTornwall/)
