# SQL Queries

## Initialize database

__User__ *(Account)*

`CREATE TABLE account (
	id INTEGER NOT NULL,
	date_created DATETIME,
	date_modified DATETIME,
	firstname VARCHAR(144) NOT NULL,
	lastname VARCHAR(144) NOT NULL,
	email VARCHAR(144) NOT NULL,
	password VARCHAR(144),
	PRIMARY KEY (id),
	UNIQUE (email)
)`

__Course__

`CREATE TABLE course (
	id INTEGER NOT NULL,
	date_created DATETIME,
	date_modified DATETIME,
	"courseId" VARCHAR(144),
	title VARCHAR(144) NOT NULL,
	description VARCHAR(144) NOT NULL,
	duration INTEGER NOT NULL,
	deadline DATETIME,
	PRIMARY KEY (id)
)`

__Log__

`CREATE TABLE log (
	id INTEGER NOT NULL,
	date_created DATETIME,
	date_modified DATETIME,
	description VARCHAR(144) NOT NULL,
	duration FLOAT NOT NULL,
	user_id INTEGER NOT NULL,
	course_id INTEGER NOT NULL,
	PRIMARY KEY (id),
	FOREIGN KEY(user_id) REFERENCES account (id),
	FOREIGN KEY(course_id) REFERENCES course (id)
)`

__Role__

`CREATE TABLE role (
	id INTEGER NOT NULL,
	date_created DATETIME,
	date_modified DATETIME,
	name VARCHAR(32) NOT NULL,
	superuser BOOLEAN NOT NULL,
	PRIMARY KEY (id),
	UNIQUE (name),
	CHECK (superuser IN (0, 1))
)`

__Usercourse__

`CREATE TABLE usercourse (
	user_id INTEGER,
	course_id INTEGER,
	FOREIGN KEY(user_id) REFERENCES account (id) ON DELETE CASCADE,
	FOREIGN KEY(course_id) REFERENCES course (id) ON DELETE CASCADE
)`

__Userrole__

`CREATE TABLE userrole (
	user_id INTEGER,
	role_id INTEGER,
	FOREIGN KEY(user_id) REFERENCES account (id) ON DELETE CASCADE,
	FOREIGN KEY(role_id) REFERENCES role (id)
)`

## Aggregate queries

*Fetch five most recent courses with activity (i.e. with added or updated logs) of a specific student and order them by most recent activity*

`SELECT Course.id, Course.course_id, Course.title, COUNT(*) FROM Log
LEFT JOIN Course ON Log.course_id = Course.id
GROUP BY Course.id
HAVING Log.user_id = :user_id
ORDER BY Log.date_created, Log.date_modified DESC
LIMIT 5;`

*Fetch courses with logs of a specific student and count the sum of hours within each course*

`SELECT Course.id, Course.course_id, Course.title, Course.duration, Course.deadline, SUM(Log.duration) as progress FROM Log
LEFT JOIN Course ON Log.course_id = Course.id
WHERE Log.user_id = :user_id
GROUP BY Course.id;`

*Find courses and count enrolled students in each course*

`SELECT Course.id, Course.courseId, Course.title, Course.description, Course.duration, Course.deadline, COUNT(Usercourse.user_id)-1  AS Students FROM Course
LEFT JOIN Usercourse ON Course.id = Usercourse.course_id
GROUP BY Course.id;`

*Find courses and count enrolled students in each course that match the search term*

`SELECT Course.id, Course.course_id, Course.title, Course.description, Course.duration, Course.deadline, COUNT(Usercourse.user_id)-1 AS Students FROM Course
LEFT JOIN Usercourse ON Course.id = Usercourse.course_id
WHERE Course.course_id LIKE :search_term OR Course.title LIKE :search_term
GROUP BY Course.id;`
