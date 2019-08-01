# TimeTracker

## Table of contents

1. [Description](#description)
2. [How to run locally](#howtorun)
3. Use cases
  3. 1. User groups
    3. 1.1. Student
    3. 1.2. Teacher
  3. 2. User stories
    3. 2.1. Student
    3. 2.2. Teacher
  3. 3. Structure
4. Database
  4. 1. Database chart
5. Technology stack
6. Contributors


## 1. Description <a name="description"></a>

TimeTracker is a personal work hour tracking tool. Students can keep track of their daily working hours and update logs. Teachers can monitor student specific course progress. Courses also have a target duration that students should achieve.

[Link to the demo](https://tsoha-timetracker.herokuapp.com/)

## 2. How to run locally? <a name="howtorun"></a>

1. Clone repository to your local machine
2. Download dependencies `pip install -r requirements.txt`
3. Run the project `python3 run.py`
4. Navigate to [http://localhost:5000](http://localhost:5000)

## 3. Use cases

### 3.1 User groups

__3.1.1 Student__

Any person who want's to log their progress on a course that exists within the tool.

__3.1.2 Teacher__

Any person who wants to supervise a course or a project. Teacher can control the course details, such as maximum number of students and create and delete courses.

### 3.2 User stories

__3.2.1 Student__

As a student I can
 - Log in
 - Register myself to a course
 - See an overview of the logs of any of the courses I'm participating in
 - Create a log that contains the description of the tasks I have done today, the duration it took to complete those tasks and today's date
 - Add hours to the duration of the specific day's log I have created
 - Update any logs I have created by modifying the description and duration
 - Delete any log I have created


__3.2.2 Teacher__

 As a teacher I can
  - Log in
  - Create new courses so that students can log their progress
  - See who's participating in any course I'm responsible for
  - See an overview of any of my courses
  - Add users to any of my courses
  - Delete students from any of my courses
  - Delete any of my courses

### 3.3 Structure

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

_/mycourses/_
- View all the courses the student is registered for

_/:courseId/logs/_
- Track progress on a specific course or project
- View all the logs and increase the duration of a log

_/:courseId/:logId/_
- Update or delete a log

_/:courseId/new/_
- Create new log for a specific course


__Teacher__

_/auth/signup/teacher/_
- Create a new teacher account

_/auth/login/_
- Log in to the tool

_/courses/_
- View all courses teacher is responsible for

_/courses/new/_
- Create new course

_/courses/:courseId/_
- Overview of a specific course, such as number of participants
- Delete course

_/courses/:courseId/participants/_
- List of students who participate to this course and the total hours out of the maximum they have logged
- Remove students from the course and add students for the course (?)

_/courses/:courseId/:studentId/_
- Course specific logs of a student

## 4. Database

For development: SQLite

For production: PostgreSQL

### 4.1 Database chart

![database chart](https://github.com/MikaelTornwall/timetracker/blob/master/documentation/timetracker.png)

[Link to the chart](https://drive.google.com/file/d/176zQnYk9ukeFViq_n_RI6qthSVZ2TaM1/view?usp=sharing)

## 5. Technology stack

* Flask
* Jinja2
* SQLite/PostgreSQL

## 6. Contributors

* [@MikaelTornwall](https://github.com/MikaelTornwall/)
