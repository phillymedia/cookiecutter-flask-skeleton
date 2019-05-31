# Flask Skeleton

Forked from [realpython](https://github.com/realpython/cookiecutter-flask-skeleton).
* Added to requirements.txt:
  * [Flask-JSON](https://pythonhosted.org/Flask-JSON/)==0.3.3
  * [python_dotenv](https://github.com/theskumar/python-dotenv)==0.10.2
* Added blueprint for an API (which uses Flask-JSON)
* Todo:
  * Add tests for API

Flask starter project for [Cookiecutter](https://github.com/audreyr/cookiecutter).

[![Build Status](https://travis-ci.org/realpython/cookiecutter-flask-skeleton.svg?branch=master)](https://travis-ci.org/realpython/cookiecutter-flask-skeleton)

## Quick Start

Install Cookiecutter globally:

```sh
$ pip install cookiecutter
```

Generate the boilerplate:

```sh
$ cookiecutter https://github.com/realpython/cookiecutter-flask-skeleton.git
```

Once generated, review the setup guides, within the newly created project directory, to configure the app:

1. [setup-with-docker.md](%7B%7Bcookiecutter.app_slug%7D%7D/setup-with-docker.md)
1. [setup-without-docker.md](%7B%7Bcookiecutter.app_slug%7D%7D/setup-without-docker.md)
