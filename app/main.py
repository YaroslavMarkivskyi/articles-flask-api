from .settings import app, db
from .auth import auth_bp
from .articles import articles_bp
from .auth.models import User
from .articles.models import Article


app.register_blueprint(auth_bp)
app.register_blueprint(articles_bp)

with app.app_context():
    db.create_all()

if __name__ == '__main__':
    app.run()
