# Installation guide

Below are the instructions on how to install and run the application both locally and in Heroku. The blocks highlighted with

`$ example command`

are commands that are meant to be typed on your [command line](https://en.wikipedia.org/wiki/Command-line_interface).

## Download project to your local machine

You have two options to achieve this. You can either clone the project using command line or download the the .zip -file from GitHub:

### Clone project using command line

Navigate to the preferred folder on your local machine. Then type one of the following commands depending on your preference:

__Using HTTPS__

`$ git clone https://github.com/MikaelTornwall/timetracker.git`

__Using SSH__

`$ git clone git@github.com:MikaelTornwall/timetracker.git`

More detailed instructions can be found [here](https://help.github.com/en/articles/cloning-a-repository).

### Download .zip -file

1. Navigate to [https://github.com/MikaelTornwall/timetracker](https://github.com/MikaelTornwall/timetracker)
2. Click the green "Clone or download" button
3. Click "Download ZIP" button
4. Go to the folder on your local machine, where the .zip -file was downloaded and unzip the file
5. Move the file to a preferred folder

## How to run locally

There are a few steps that have to be taken before the project can be run locally. First, make sure you have Python installed on your local machine, most preferably Python 3. If not, you can download it from [here](https://www.python.org/downloads/). Then follow these steps:

1. Navigate to the root folder of the project
2. Create *venv* module `python3 -m venv venv`
3. Activate the isolated virtual environment `source venv/bin/activate`
4. Download dependencies `pip install -r requirements.txt`
5. Run the project `python3 run.py`
6. Navigate to [http://localhost:5000](http://localhost:5000)

## How to deploy to Heroku

First you will need a Heroku account. You can create one [here](https://signup.heroku.com/). After you have successfully created a Heroku account follow these instructions:

1. Navigate to the root folder of the project

2. Create a Heroku project for your application:

`$ heroku create`

3. Link the project to your Heroku application

When you created the heroku app, Heroku returned two URLs. Copy the URL that has the following form: "https://git.heroku.com/project-name.git".

`$ git remote add heroku https://git.heroku.com/<project name>.git`

4. Push your application to Heroku

`$ git add .`

`$ git commit -m "initial commit"`

`$ git push heroku master`

Wait for the process to complete and navigate to the project URL that Heroku returned. If you face any problems, refer to Heroku's [deployment guide](https://devcenter.heroku.com/articles/git).

## How to create accounts, login and start using the application

Open the application in your browser.

There are two distinct user types, Student and Teacher. You can sign up as either one by clicking "Signup" in the navigation bar and then selecting the desired user type. After you have created an account you can log in.

Depending on your user type you can use different features. More detailed feature list can be found from the [main documentation](https://github.com/MikaelTornwall/timetracker/blob/master/documentation/documentation.md#structure).
