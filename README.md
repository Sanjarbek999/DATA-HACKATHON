# DATA-HACKATHON

This is flask template for DATA hackathon event

## Installation

```shell
$ git clone https://github.com/KhasanovR/DATA-HACKATHON.git
$ cd DATA-HACKATHON
$ python3 -m venv myenv
$ source myenv/bin/activate
$ pip3 install -r requirements.txt
$ flask run
```

## Usage

Replace the values in **.env.example** with your values and rename this file to **.env**:

* `FLASK_APP`: Entry point of your application (should be `wsgi.py`).
* `FLASK_ENV`: The environment to run your app in (either `development` or `production`).
* `SQLALCHEMY_DATABASE_URI`: SQLAlchemy connection URI to a SQL database.

*Remember never to commit secrets saved in .env files to Github.*
