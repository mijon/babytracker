# Baby tracker

With a newborn, it's helpful to track changes and feeds, and potentially any medication that mother or baby migh t be taking. 
This is a simple Flask app designed to be self-hosted on which these activities can be tracked.

## Docker image

To build the image:

```
docker build -f Dockerfile . -t babytracker
```

## Setting up the DB

Inside the docker container, run 

```
flask --app babytracker init-db
```
