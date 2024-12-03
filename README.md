# articles-flask-api
## ENDPOINTS:
### users:
- get `users/` - get users (allow all users)
- post `users/` - create user (allow only admin)
- get `users/<int:user_id>` - get user by id (allow all users)
- put `users/<int:user_id>` - update user by id (allow admin, editor, and userself)
- delete `users/<int:user_id>` - delete user by id (allow only admin)
- get `users/search?username=<username>` - get user by username (allow all users)
- get `users/<int:user_id>` - get user own profile (allow all users)
### articles:
- get `articles/` - get articles (allow all users)
- post `articles/` - create articles (allow all users)
- get `articles/<int:user_id>` - get article by id (allow all users)
- put `articles/<int:user_id>` - update user by id (allow admin, editor, and article owner)
- delete `articles/<int:user_id>` - delete user by id (allow only admin)
- get `articles/search?title=<username>` - get article by title (allow all users)


## Command line interface:
- init_db_command - initial database
- create_user - create single user manual
- seed_users - create multiple users (pass the number of users for each role and password)
- seed_articles - create many articles (pass the number of articles. The owner of the article is random in the existing database).

## Blueprints:
- users_bp -  assign responsibility for the users of the module
- articles_bp -  assign responsibility for the articles of the module
## STRUCTURE:
### app/:
#### commands/:
 This directory contains scripts for executing administrative and auxiliary commands, such as:
 - Initializing the database (init_database.py).
 - Creating users (create_user.py).
 - Filling the database with test articles (seed_articles.py) or users (seed_users.py).


#### modules/:
The main modular space of the application. This directory is organized by functionality. The same structure for articles and users:
 - models.py: the models for db.
 - crud_services.py: logic for processing CRUD operations.
 - validators.py: validation system.
 - routers.py: API routes.
 - serializers.py: serializers for converting models to JSON.
 - tests/: Test files
 - permissions.py: logic for checking access to resources.
#### setup/:
The directory for global settings and auxiliary utilities:
-  settings.py: A configuration file that stores the application settings
-  utils.py: Utility functions that can be used in different parts of the project.
#### main.py:
The main file of the application
### .gitignore:
Used to determine which files and directories should not be added to a Git repository
### Dockerfile:
 File that contains a set of instructions for creating a Docker image
### docker-compose.yml:
This is a file used to describe the Docker infrastructure of a project.
It defines how services (containers) interact with each other.
### docker-compose-deploy.yml:
 Similar to docker-compose.yml, but usually used to deploy a project to a server (e.g., staging or production).
### requirements.dev.txt:
 A file containing development dependencies (e.g., pytest, flake8, black).
### requirements.txt:
A file with the main project dependencies needed to get the project up and running.
### .github/workflows:
 The directory with GitHub Actions configurations that automate CI/CD processes (e.g., tests, linting, deploy).


 ## CI/CD:
 