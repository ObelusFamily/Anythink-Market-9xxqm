# Welcome to the Anythink Market repo

To start the app use Docker. It will start both frontend and backend, including all the relevant dependencies, and the db.

Please find more info about each part in the relevant Readme file ([frontend](frontend/readme.md) and [backend](backend/README.md)).

## Development

When implementing a new feature or fixing a bug, please create a new pull request against `main` from a feature/bug branch and add `@vanessa-cooper` as reviewer.

## First setup

1. First thing’s first - [install Docker](https://docs.docker.com/get-docker/). You can verify docker is ready by running the following commands in your terminal: `docker -v` and `docker-compose -v`.
2. Run `docker-compose up` from project root directory - this will start the backend and frontend.
3. Once the containers are running, point your browser to http://localhost:3000/api/ping to test the backend.
4. Now, time to check the frontend and make sure it’s connected to the backend. If everything is working properly, you’ll be able to create a new user at `http://localhost:3001/register`.

And you're all set!

## Next steps

Make sure that you run all scripts on one of the containers created by `docker-compose up`. Also, you can use `docker exec` to run commands on a running container.