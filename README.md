# The Liner Notes

The Liner Notes is a minimalistic album review website. It displays the latest review on the front of the site and allows readers to go back and fourth linearly or view an index of reviews.

## Setup

To set up the local instance of this site, simply run:

``` python
python manage.py migrate
```
This will run the required migrations. Next you must set up the first admin account:

``` python
python manage.py createsuperuser
```
Follow the prompts and an admin account will be created. Finally run the server at `http://localhost:8000` using:

```python
python manage.py runserver
```