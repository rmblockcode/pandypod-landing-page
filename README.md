# PANDYPOD LANDING PAGE

## Instructions

### Clone repository:

    git clone git@github.com:rmarquez1/pandypod-landing-page.git


### Dependencies

    Create virtualenv using python>=3.9 and install dependencies:

    pip install -r requirements.txt


### What to do when psycopg2 cannot be installed? Execute the following command in Debian/Ubuntu:

    sudo apt install libpq-dev python3-dev


### Environment variables

    # Postgres database credentials:
    export DATABASE_NAME=pd_landingpage
    export DATABASE_USER=postgres
    export DATABASE_PASSWORD=postgres
    export DATABASE_HOST=127.0.0.1
    export DATABASE_PORT=5432


    # Debugger y host:
    export DEBUG=True
    export ALLOWED_HOSTS=*

    # Static files
    export STATIC_ROOT=/$HOME/static/
    export STATIC_URL=/static/
    export MEDIA_ROOT=/$HOME/media/
    export MEDIA_URL=/media/

    export MAIN_PAGE_URL=http://127.0.0.1:8101/
    export VISIT_US_BTN=https://linkr.bio/qxx6z5


### Migrations

    python manage.py makemigrations (If DB is new, it's not necessary run this command)
    python manage.py migrate


### Create superuser to manage users and content

    python manage.py createsuperuser

    (Follow instructions in console)


### Execute in local environment

    python manage.py runserver [HOST:PORT]
