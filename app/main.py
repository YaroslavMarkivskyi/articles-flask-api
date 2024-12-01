from .settings import app, db
from .auth import auth_bp
from .auth.models import User


app.register_blueprint(auth_bp)

with app.app_context():
    db.create_all()

if __name__ == '__main__':
    app.run()
