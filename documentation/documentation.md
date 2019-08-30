# Timetracker

## Overview

Personal work hour tracking tool.

## Table of contents

1. [Description](#description)
2. [How to use](#howtouse)
    1. [Heroku](#heroku)
    2. [Installation guide](#installation)    
3. [Use cases](#usecases)  
    1. [User groups](#usergroups)
    2. [User stories](#userstories)
    3. [Structure](#structure)
4. [Database](#database)
    1. [Database chart](#chart)
    2. [SQL queries](#queries)
5. [Technology stack](#techstack)
6. [Design](#design)
7. [Contributors](#contributors)

<a name="description"></a>
## 1. Description

Timetracker is a personal work hour tracking tool for teachers and students that want to record and monitor the progress of a course or a project. Students can keep track of their daily work hours and update logs on several courses and projects. Teachers can create courses and monitor student specific course progress.

[Link to the demo](https://tsoha-timetracker.herokuapp.com/)

<a name="howtouse"></a>
## 2. How to use

The application can be used either locally or in Heroku. Below can be found instructions on how view the application demo in Heroku and how to install and use the application locally or in Heroku.

<a name="heroku"></a>
### 2.1. Heroku

__Credentials:__

| Email               | Password      | Role     |
| --------------------|---------------|----------|
| `student@email.com` | `student123`  | Student  |
| `teacher@email.com` | `teacher123`  | Teacher  |

Navigate to [login](https://tsoha-timetracker.herokuapp.com/auth/login) and use the credentials above.

<a name="installation"></a>
### 2.2. Installation guide

[Link to the installation guide](https://github.com/MikaelTornwall/timetracker/blob/master/documentation/installation.md)

<a name="usecases"></a>
## 3. Use cases

<a name="usergroups"></a>
### 3.1. User groups

__3.1.1. Student__

Any person who want's to log their progress on a course or a project that exists within the tool.

__3.1.2. Teacher__

Any person who wants to supervise a course or a project.

<a name="userstories"></a>
### 3.2. User stories

__3.2.1. Student__

"As a student I want to be able to enroll in different courses and projects. I want to be able to write detailed descriptions about what I have done during a specific task and also log the duration of that task. I want to see my progress within each course. I want be able to see the list of the latest logs I have created for a specific course and modify these logs. I also want to see the complete list of all the courses I have enrolled in."

As a student I can
 - Log in to the tool
 - Enroll/unenroll myself in a course
 - See all courses within the tool
 - See all the courses I have enrolled in
 - See all my course specific logs, total work hours and progress
 - Create a log that contains the description of the tasks I have done today, the duration it took to complete those tasks and today's date
 - Add hours to the duration of the specific day's log I have created
 - Update any logs I have created by modifying the description and duration
 - Delete any log I have created

__3.2.2. Teacher__

"As a teacher I want to be able to create courses. I want to be able see students who are enrolled in a specific course and the total number of students in each course. I also want to be able to follow the progress of an individual student within a specific course, read the logs and see the student's personal information."

 As a teacher I can
  - Log in to the tool
  - Create new courses so that students can log their progress  
  - See an overview of any of my courses
  - See who's participating in any course I'm responsible for
  - See course progress and logs of a specific student within a specific course
  - Update any of my course's details
  - Delete any of my courses

<a name="structure"></a>
### 3.3. Structure

Structure of the tool and features of each page for unauthorized users, and student and teacher accounts:

__Unauthorized__

Homepage: _/_
- Tool's description and navigation bar for registration and login

_/auth/signup/_
- Select which account type to create

_/auth/signup/student/_
- Create a new student account

_/auth/signup/teacher/_
- Create a new teacher account

_/auth/login/_
- Log in to the tool

__Student__

_/courses/_
- View all the courses
- Enroll/unenroll in a course

_/courses/:courseId_
- View course details
- Enroll/unenroll in a course

_/logs/_
- View all the courses the student is registered for

_/:courseId/logs/_
- Track progress on a specific course or project
- View all the logs and increase the duration of a log

_/:courseId/logs/:logId/_
- Update or delete a log

_/:courseId/logs/new/_
- Create a new log for a specific course

__Teacher__

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

_/:courseId/logs/:studentId/log_
- View course specific logs of a student

<a name="database"></a>
## 4. Database

For development: SQLite

For production: PostgreSQL

<a name="chart"></a>
### 4.1. Database chart

![database chart](https://github.com/MikaelTornwall/timetracker/blob/master/documentation/timetracker.png)

[Link to the chart](https://drive.google.com/file/d/176zQnYk9ukeFViq_n_RI6qthSVZ2TaM1/view?usp=sharing)

<a name="queries"></a>
### 4.2 SQL queries

Below can be found the SQL queries for creating the database and the most important aggregate queries.

[Link to the queries](https://github.com/MikaelTornwall/timetracker/blob/master/documentation/sqlqueries.md)

<a name="techstack"></a>
## 5. Technology stack

* Flask
* Jinja2
* SQLite/PostgreSQL

<a name="design"></a>
## 7. Design

Front-end framework in use is [Foundation by Zurb](https://foundation.zurb.com/). In addition to that the application uses some custom CSS.

__Colors:__

*Main:*
- ![#1a1a1a](https://placehold.it/15/1a1a1a/000000?text=+) `#1a1a1a`

*Main background:*
- ![#969696](https://placehold.it/15/969696/000000?text=+) `#969696`

*Student:*
- ![#ffb400](https://placehold.it/15/ffb400/000000?text=+) `#ffb400`

*Teacher:*
- ![#1e0064](https://placehold.it/15/1e0064/000000?text=+) `#1e0064`

<a name="contributors"></a>
## 7. Contributors

* [@MikaelTornwall](https://github.com/MikaelTornwall/)
