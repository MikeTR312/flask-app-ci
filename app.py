import os
from flask import Flask

app = Flask(__name__)

@app.route("/")
def hello():
    env = os.getenv("APP_ENV", "not set")
    db_pass = os.getenv("DB_PASSWORD", "not set")
    return f"Привет из контейнера! Режим: {env}<br>Пароль от БД: {db_pass}"

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=80)