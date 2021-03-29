# Lab: Authentication & Production Server
## Overview
Let’s move our API closer to production grade by adding Authentication and switching to a Production Server

## Feature Tasks and Requirements
### Features - Django
- [x] Add JWT Authentication to your API.
  - Install needed libraries in project configuration and/or site settings.
- [x] Keep any pre-existing authentication so DRF Browsable API still usable.
  - Install needed libraries in project configuration and/or site settings.
### Features - Docker
- Create a boilerplate Dockerfile and docker-compose.yml so you don’t need to start from scratch each time.
  - E.g. as a VS Code snippet, or a gist.
- [x] Switch to using Gunicorn instead of Django’s built in development server.
  - _mind the number of workers to avoid sluggishness_
- [x] **Warning** You will run into styling issues when you switch over to Gunicorn.
  - [x] handled when implementing whitenoise and running `$ docker-compose run web python manage.py collectstatic` 
- [x] On Django side you’ll need to properly handle static files using Whitenoise
Storage Options
- [x] Use PostgreSQL
- [x] Adjust docker-compose.yml so that data is persisted in a volume outside of container.
- These steps are different depending on whether SQLite or PostgreSQL is being used.

### Implementation Notes
User Acceptance Tests
- [x] Include steps to manually test using httpie or Postman.
  - httpie used
  - `$ http post http://127.0.0.1:8000/api/token/ username= password=` 
  - Copy and paste access token 
    - `http http://127.0.0.1:8000/api/v1/task/ "Authorization: Bearer"` -> paste access token between "Bearer and quotes"
  - When access token expires
    - `http post http://127.0.0.1:8000/api/token/refresh/ refresh=` Paste refresh token from first step
- No unit tests required.

# Lab: API Deployment

## Feature Tasks and Requirements
- NOTE: You can use previous lab’s Application as a starting point or start from scratch.
- [x] Modify your application to store SECRET_KEY, ALLOWED_HOSTS, DEBUG and DATABASE information in .env file.
- [x] All the code changes will be in settings.py so check the demo code for Env related lines.
- [x] In a nutshell - make your own Application similar to the demo, and put it on the web
- Add CORS headers using django-cors-headers
- Whitelist allowed origins
- Handle collecting static files so that browsable API renders nicely.
## Stretch Goals
- Host database in a location other than where Django site is hosted.
## Deployment Requirements
- Research web hosting sites capable of working with Docker
- NOTE no money is required for this lab but you may choose to create a trial account.
- But you are responsible for making sure you don’t hit with charges when trial is complete.
## Implementation Notes
- You are not required to use Poetry since the requirements.txt is being supplied.
- However if you run into issues with supplied requirements.txt then you are responsible for rebuilding.
- You are NOT required to use Database from an external source, but it’s nice if you do.
- You ARE required to have Database settings read from environment variables.
### Useful Terminal Commands
- docker-compose up --build
- docker-compose up -d --build (runs in detached mode)
- docker-compose down
- docker-compose restart
- docker-compose exec web python manage.py migrate
  - run after build
- docker-compose exec web python manage.py collectstatic
  - make sure whitenoise is configured in settings
### User Acceptance Tests
- Manually confirm API using Postman/HTTPie.
- Remember to use deployed url for postman requests.
