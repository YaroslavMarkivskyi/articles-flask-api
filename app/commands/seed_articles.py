from app.setup.settings import db
import click
from flask.cli import with_appcontext
import sys
from app.modules.users.models import User
from app.modules.articles.models import Article
from faker import Faker


fake = Faker()


def get_all_user_ids():
    user_ids = db.session.query(User.id).all()  # Запитуємо всі id користувачів
    return [user_id[0] for user_id in user_ids]

@click.command('seed-articles')
@click.option('--count', default=2, type=int, help='Number of articles to create')
def seed_articles(count):
    # Отримуємо всі id користувачів
    users_id = get_all_user_ids()

    # Створюємо кількість статей
    for _ in range(count):
        title = fake.sentence(nb_words=6)
        description = fake.sentence(nb_words=12)
        body = fake.text(max_nb_chars=1000)

        # Вибір випадкового автора
        author_id = fake.random_element(users_id)

        # Створення нового запису статті
        article = Article(
            author_id=author_id,
            title=title,
            description=description,
            body=body
        )

        # Додавання статті в сесію
        db.session.add(article)

    # Підтвердження змін в базі даних
    db.session.commit()
    click.echo(f'{count} articles have been created successfully!')
