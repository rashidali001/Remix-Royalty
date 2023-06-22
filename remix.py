from app import app, db
from app.models import User

app.app_context().push()

if __name__ == "__main__":
    app.run(debug=True)