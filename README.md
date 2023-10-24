# Lyfetree
This is the "Lyfetree" repository. Lyfetree is an app for documenting personal accomplishments and "skills" achieved in life. The purpose of this app is for it to be used as a personal online diary.
This project was brought to life purely for fun and we are not actively working on this repository.
## UX
No user experience requirements have been set yet.
### User Stories
No user stories have been created.
### Design
No design requirements have been set.
## Features
No explicit features have been requested/deployed.
## Technologies Used
- [django](https://www.djangoproject.com)
    - The project uses the **django** web framework as a base.

- [Python](https://www.python.org)
    - The project uses **Python** based on the django framework to serve functionality of the app.

- [SQLite](https://www.sqlite.org/index.html)
    - The project uses **SQLite** for databases.

- [HTML](https://www.w3.org/)
    - The project uses **HTML** to create pages inside the django project.

- [CSS](https://www.w3.org/)
    - The project uses **CSS** to style the application.
## Testing
No tests have been applied.
## Deployment
To be done.
## Installation
For this installation guide it is assumed you have already installed Python and the packaging tool ```pipenv``` on your local machine.
You can install the tool via ```pip install pipenv``` in your command line after installing the latest Python version.

How to install and run the "Lyfetree" app on a local server/machine:
1. Clone the repository.
2. Open the terminal and cd into the local repository folder.
3. In the repository, create a file called ".env" in the root folder of the repository for enviromental variables and generate a secret key (you can use whatever generator you like or type in any prefered combination of letters, numbers and symbols - but keep it strong, safe and secret)
4. Paste your secret key in quotation marks in the first line of the .env file like this:
```bash
DEBUG=True
ALLOWED_HOSTS=localhost,127.0.0.1
DB_ENGINE=django.db.backends.sqlite3
DB_NAME="yourdatabasename".db
DB_USER="yourusername"
DB_PASSWORD="yourpassword"
DB_HOST=localhost
DB_PORT="yourport"
SECRET_KEY="yoursecretkeygoeshere"
```
5. Now that security is set up, you can create the local enviroment. Type ```pipenv install``` 
to install the enviroment and all dependencies.
6. Type ```pipenv shell``` to open the local enviroment and the corresponding shell line.
7. Now migrate the app to create a local database with ```python manage.py migrate```.
8. Run the local server via ```python manage.py runserver```.
9. Click on the local server IP given in the terminal to open the app.
8. Have fun playing around!
## Credits
Credits to @CevikKubat and @JapahaPapaya for actively contributing to this project and working things out together.