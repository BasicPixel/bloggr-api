# bloggr-api

API Source code for the [bloggr](api/) anonymous blog.

Built using Django with Django REST Framework and hosted using Heroku.

- [bloggr-api](#bloggr-api)
  - [Setup](#setup)
  - [API Documentation](#api-documentation)

## Setup

Start cloning this repository:

```sh
git clone
cd bloggr-api
```

Then create a virtual environment and activate it:

```sh
# On Windows
python -m venv env
env\Scripts\activate
```

Install the dependancies:

```sh
pip install -r requirements.txt
```

After installing the dependancies migrate then run the server:

```sh
python manage.py makemigrations
python manage.py migrate
python manage.py runserver
```

## API Documentation

| API Route        | Method accepted | Description                                               |
| ---------------- | --------------- | --------------------------------------------------------- |
| /api             | GET             | API base route                                            |
| /api/posts       | GET             | Returns all available posts                               |
| /api/post/[id]   | GET             | Returns post with specified id, or 404 error if not found |
| /api/add-post    | POST            | Adds a new post with the posted data                      |
| /api/update/[id] | PUT             | Updates a post (chosen by id) with specified info         |
| /api/delete/[id] | DELETE          | Deletes the post with the specified id                    |
