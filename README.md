# Lab: Authentication & Production Server
## Overview
Let’s move our API closer to production grade by adding Authentication and switching to a Production Server

## Feature Tasks and Requirements
### Features - Django
- Add JWT Authentication to your API.
  - Install needed libraries in project configuration and/or site settings.
- Keep any pre-existing authentication so DRF Browsable API still usable.
  - Install needed libraries in project configuration and/or site settings.
### Features - Docker
- Create a boilerplate Dockerfile and docker-compose.yml so you don’t need to start from scratch each time.
  - E.g. as a VS Code snippet, or a gist.
- Switch to using Gunicorn instead of Django’s built in development server.
  - _mind the number of workers to avoid sluggishness_
- **Warning** You will run into styling issues when you switch over to Gunicorn.
- On Django side you’ll need to properly handle static files using Whitenoise
Storage Options
- Use PostgreSQL
- Adjust docker-compose.yml so that data is persisted in a volume outside of container.
- These steps are different depending on whether SQLite or PostgreSQL is being used.
### Stretch Goals
- Research deployment options for Docker/Postgres/Django and report findings to class
- Research separate PostgreSQL hosting
- Create/Find a seed project so that you can have a running start on next DRF project.
### Implementation Notes
User Acceptance Tests
- Include steps to manually test using httpie or Postman.
- No unit tests required.