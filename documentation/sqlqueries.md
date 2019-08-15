# SQL Queries

## Initiate database

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

## Complicated and summarizing queries

*Count users that have the role student and who have enrolled on a specific course*

`SELECT COUNT(*) FROM Account
LEFT JOIN Userrole ON Userrole.user_id = Account.id
LEFT JOIN Role ON Role.id = Userrole.role_id
LEFT JOIN Usercourse ON Usercourse.user_id = Account.id
LEFT JOIN Course ON Course.id = Usercourse.course_id
WHERE Course.id = :id AND Role.name = 'STUDENT';`

*Return users that have the role student who have enrolled on a specific course, and order returned users alphabetically (primary: first name, secondary: last name)*

`SELECT * FROM Account
LEFT JOIN Userrole ON Userrole.user_id = Account.id
LEFT JOIN Role ON Role.id = Userrole.role_id
LEFT JOIN Usercourse ON Usercourse.user_id = Account.id
LEFT JOIN Course ON Course.id = Usercourse.course_id
WHERE Course.id = :id AND Role.name = 'STUDENT'
ORDER BY Account.firstname, Account.lastname;`
