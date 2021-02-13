# News aggregator

It's an app that has been created as a test-task for "AppEvent" company


# Install

```bash
$ git clone https://github.com/nbox363/news_aggregator
$ cd news_aggregator
```

Create a virtualenv and activate it:
```bash
$ python3 -m venv venv
$ . venv/bin/activate
```

Install pip packages:
```bash
$ pip install -r requirements.txt
```

# Init database 
you may need to stop local mysql before starting docker compose
```
sudo service mysql stop
```
to run mysql database
```bash
docker-compose up
```
get data
```bash
python manage.py shell < db.py
```

# Run
```bash
python manage.py runserver
```
