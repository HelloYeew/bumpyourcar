![SUSSY BAKA](emergency/static/img/drivelikesus.png)

# bumpyourcar
 eXceed camp project to help you when you bump or drowned your car, and you are currently feel bad that you broke your car and not able to help but you still need help by an emergency.

## Developing bumpyourcar

Please make sure you have the following prerequisites:

- [Python 3.9 or higher](https://www.python.org/)
- [Git](https://git-scm.com/)

**Note:** Before continue, for Windows users, replace `/` in paths with `\`. 

### Step 1 : Cloning the repository

There are two ways to go about it, one being downloading as a zip file and the other being cloning via git command line. We will guide you through the latter method since the former is pretty straight forward (download and extract files).

Navigate to your desired directory, then clone this repository by entering the following command into your git command line:

```shell
git clone https://github.com/HelloYeew/bumpyourcar.git
```

### Step 2 : Setting up the virtual environment

We recommend to use the virtual environment to make sure on the package version and make sure that you have the seperate environment for this project.

Install virtualenv by running as a global package via this command:

```shell
pip install virtualenv
```

Then navigate to `.../bumpyourcar` and run the following command:
```shell
virtualenv [virtual environment name]
```

Now that you have your virtual environment set up, you can now activate the virtual environment by running either one of the following commands:

```shell
# MacOS or Linux
source [virtual environment name]/bin/activate
# Windows
[virtual environment name]/Scripts/activate
```

After activating the virtual environment, to install all the required modules run the following command:
```shell
pip install -r requirements.txt
```

And that's all for Python. Now for Django, we have a tiny setup to do and we're golden.

### Step 3: Setup the database and run the server

Create the `.env` file with this template for your project's environment file:
```dotenv
SECRET_KEY=cool_secret_key_here
DEBUG=True
```

Place the `.env` in `...\bumpyourcar\bumpyourcar` (The directory that contains `manage.py`)

Before running the server we have to migrate the database using the following command:

```shell
python manage.py migrate
```

Now try running the server! Run the command below:
```shell
python manage.py runserver
```

Now you can access the server by going to `http://localhost:8000/`!

### Step 4: Create a new superuser

A superuser is a user that has all the permissions to manage the database. We can create a superuser by running the following command:

```shell
python manage.py createsuperuser
```

Then follow the prompts to create a superuser.