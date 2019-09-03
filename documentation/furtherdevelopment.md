# Further development

Here are some ideas for further development, some of which couldn't be executed within the scope of this course.

## Organizations

Currently the application is only suitable for the use of a single organization. By adding organizations as a database table and adding corresponding authorization we can easily expand the application into a proper SAAS -service. Then separate organizations could have their own environments.

## Allowing several teachers to administer a course

Each course could include several teachers. This would require some modifications to the authorization configurations as well as the database queries. For clarity it could possibly be wise to separate students and teachers altogether withing the course entity.

## Timer

Adding a timer feature for students would enchance the user experience. In detail this would mean a timer that could for example be implemented within the log form. This way when starting the day's work, a student could write a description about what one is going to do and start the timer. When one is finished with the task, the timer could be stopped. By saving the log, the exact time and description would be saved into the database.
