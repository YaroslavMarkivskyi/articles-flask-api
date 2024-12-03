# articles-flask-api

endpoints:

users:
[get] users/ - get users (allow all users)
[post] users/ - create user (allow only admin)
[get] users/<int:user_id> - get user by id (allow all users)
[put] users/<int:user_id> - update user by id (allow admin, editor, and userself)
[delete] users/<int:user_id> - delete user by id (allow only admin)
[get] users/search?username=<username> - get user by username (allow all users)
[get] users/<int:user_id> - get user own profile (allow all users)


articles:
[get] articles/ - get articles (allow all users)
[post] articles/ - create articles (allow all users)
[get] articles/<int:user_id> - get article by id (allow all users)
[put] articles/<int:user_id> - update user by id (allow admin, editor, and article owner)
[delete] articles/<int:user_id> - delete user by id (allow only admin)
[get] articles/search?title=<username> - get article by title (allow all users)


Command line interface:
init_db_command - initial database
create_user - create single user manual
seed_users - create many users(take count of users for every roles and password)
seed_articles - create many articles(take count of articles. Article owner is random in exist database).

blueprints:
users_bp - blueprint that responsibility by users module
articles_bp - blueprint that responsibility by articles module

structure:
app:
    /commands -
    /modules -
    /setup -
    main.py
gitignore
docker-compose.yml
docker-compose-deploy.yml
requirements.dev.txt
requirements.txt