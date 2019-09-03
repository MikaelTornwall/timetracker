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
7. [Further development](#development)
8. [Contributors](#contributors)

<a name="description"></a>
## 1. Description

Timetracker is a personal work hour tracking tool for teachers and students who want to record and monitor the progress of a course or a project. Students can keep track of their daily work hours and update logs on several courses and projects. Teachers can create courses and monitor student specific course progress.

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

With user story related SQL queries I'm indicating query parameters both with `Table(param1, param2...) VALUES(?, ?)` syntax as well as with `:example_id` depending on the query type. In addition, by default all INSERT queries also include id, date_created and date_modified parameters with corresponding values.

__3.2.1. Student__

"As a student I want to be able to enroll in different courses and projects. I want to be able to write detailed descriptions about what I have done during a specific task and also log the duration of that task. I want to see my progress within each course. I want be able to see the list of the latest logs I have created for a specific course and modify these logs. I also want to see the complete list of all the courses I have enrolled in."

As a student I can
 - Log in to the tool

 - Enroll/unenroll myself in a course

 `INSERT INTO Usercourse(user_id, course_id) VAlUES(?, ?);`

 - See all courses within the tool

 `SELECT * FROM Course;`

 - See all the courses I have enrolled in

 `SELECT * FROM Course
 JOIN Usercourse ON Course.id = Usercourse.course_id
 WHERE Usercourse.user_id = :user_id
 GROUP BY Course.id;`

 - See five courses with most recent activity (i.e. new/updated logs)

`SELECT Course.id, Course.course_id, Course.title, COUNT(*) FROM Log
LEFT JOIN Course ON Log.course_id = Course.id
GROUP BY Course.id
HAVING Log.user_id = :user_id
ORDER BY Log.date_created DESC, Log.date_modified DESC
LIMIT 5`

 - See all my course specific logs, total work hours and progress

*Course specific logs:*

`SELECT * FROM Log
WHERE Log.user_id = :user_id AND Log.course_id = :course_id;`

*Total work hours for a course:*

`SELECT SUM(duration) FROM Log
WHERE Log.course_id = :course_id AND Log.user_id = :user_id;`

*Course progress:*

`SELECT Course.id, Course.course_id, Course.title, Course.duration, Course.deadline, SUM(Log.duration) as progress FROM Log
LEFT JOIN Course ON Log.course_id = Course.id
WHERE Log.user_id = :user_id
GROUP BY Course.id;`

 - Create a log that contains the description of the tasks I have done today, the duration it took to complete those tasks and today's date

 `INSERT INTO Log(user_id, course_id, description, duration) VALUES(?, ?, ?, ?);`

 - Add hours to the duration of the specific day's log I have created

`UPDATE Log SET duration = :duration WHERE id = :log_id;`

 - Update any logs I have created by modifying the description and duration

`UPDATE Log SET description = :description, duration = :duration WHERE id = :log_id;`

 - Delete any log I have created

`DELETE FROM Log WHERE id = :log_id;`

__3.2.2. Teacher__

"As a teacher I want to be able to create courses. I want to be able see students who are enrolled in a specific course and the total number of students in each course. I also want to be able to follow the progress of an individual student within a specific course, read the logs and see the student's personal information."

 As a teacher I can
  - Log in to the tool

  - Create new courses so that students can log their progress  

`INSERT INTO Course(user_id, course_id, title, description, duration, deadline) VALUES(?, ?, ?, ?, ?, ?)`

  - See all the courses I have created

`SELECT * FROM Course
JOIN Usercourse ON Course.id = Usercourse.course_id
WHERE Usercourse.user_id = :user_id;`

  - See an overview on any of my courses

`SELECT * FROM Course
JOIN Usercourse ON Course.id = Usercourse.course_id
WHERE Usercourse.user_id = :user_id AND Usercourse.course_id = :course_id;`

*Number of students:*

`SELECT COUNT(*) FROM Account
LEFT JOIN Userrole ON Userrole.user_id = Account.id
LEFT JOIN Role ON Role.id = Userrole.role_id
LEFT JOIN Usercourse ON Usercourse.user_id = Account.id
LEFT JOIN Course ON Course.id = Usercourse.course_id
WHERE Course.id = :course_id AND Role.name = 'STUDENT';`

  - See who's participating in any course I'm responsible for

`SELECT * FROM Account
LEFT JOIN Userrole ON Userrole.user_id = Account.id
LEFT JOIN Role ON Role.id = Userrole.role_id
LEFT JOIN Usercourse ON Usercourse.user_id = Account.id
LEFT JOIN Course ON Course.id = Usercourse.course_id
WHERE Course.id = :course_id AND Role.name = 'STUDENT'
ORDER BY Account.firstname, Account.lastname;`


  - See course progress and logs of a specific student within a specific course

*Student and course specific logs:*

`SELECT * FROM Log
WHERE Log.user_id = :user_id AND Log.course_id = :course_id;`

*Course progress:*

`SELECT Course.id, Course.course_id, Course.title, Course.duration, Course.deadline, SUM(Log.duration) as progress FROM Log
LEFT JOIN Course ON Log.course_id = Course.id
WHERE Log.user_id = :user_id
GROUP BY Course.id;`

  - Update any of my course's details

`UPDATE Course SET course_id = :course_id, title = :title, description = :description, duration = :duration, deadline = :deadline
WHERE id = :course_id;`

  - Delete any of my courses

`DELETE FROM Course WHERE id = :course_id;`

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

[Additional information about the database](https://github.com/MikaelTornwall/timetracker/blob/master/documentation/database.md)

<a name="chart"></a>
### 4.1. Database chart

![database chart](https://github.com/MikaelTornwall/timetracker/blob/master/documentation/timetracker.png)

[Link to the chart](https://drive.google.com/file/d/176zQnYk9ukeFViq_n_RI6qthSVZ2TaM1/view?usp=sharing)

<a name="queries"></a>
### 4.2. SQL queries

Below can be found the SQL queries for creating the database and the most important aggregate queries.

[Link to the queries](https://github.com/MikaelTornwall/timetracker/blob/master/documentation/sqlqueries.md)

<a name="techstack"></a>
## 5. Technology stack

* Flask
* Jinja2
* SQLite/PostgreSQL

<a name="design"></a>
## 6. Design

Front-end framework in use is [Foundation by Zurb](https://foundation.zurb.com/). In addition to that the application uses some custom CSS. Icons are from [FontAwesome](https://fontawesome.com/).

__Colors:__

*Main:*
- ![#1a1a1a](https://placehold.it/15/1a1a1a/000000?text=+) `#1a1a1a`

*Main background:*
- ![#969696](https://placehold.it/15/969696/000000?text=+) `#969696`

*Student:*
- ![#ffb400](https://placehold.it/15/ffb400/000000?text=+) `#ffb400`

*Teacher:*
- ![#1e0064](https://placehold.it/15/1e0064/000000?text=+) `#1e0064`

<a name="development"></a>
## 7. Further development

[Link to the further development ideas](https://github.com/MikaelTornwall/timetracker/blob/master/documentation/furtherdevelopment.md)

<a name="contributors"></a>
## 8. Contributors

* [@MikaelTornwall](https://github.com/MikaelTornwall/)
