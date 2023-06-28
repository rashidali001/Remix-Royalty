from app import app, db
from app.models import User

app.app_context().push()

@app.shell_context_processor
def shell_processor():
    return {"db":db, "user":User}

if __name__ == "__main__":
    app.run(debug=True)