import click
from faker import Faker

from app.modules.articles.models import Article
from app.modules.users.models import User
from app.setup.settings import db

fake = Faker()


def get_all_user_ids():
    user_ids = db.session.query(User.id).all()
    return [user_id[0] for user_id in user_ids]


@click.command("seed-articles")
@click.option(
    "--count", default=2, type=int, help="Number of articles to create"
)
def seed_articles(count):
    users_id = get_all_user_ids()

    for _ in range(count):
        title = fake.sentence(nb_words=6)
        description = fake.sentence(nb_words=12)
        body = fake.text(max_nb_chars=1000)

        author_id = fake.random_element(users_id)

        article = Article(
            author_id=author_id,
            title=title,
            description=description,
            body=body
        )

        db.session.add(article)

    db.session.commit()
    click.echo(f"{count} articles have been created successfully!")
