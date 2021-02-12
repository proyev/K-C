# Gruppenprojekt g3-20

![Title](frontend/src/assets/images/kctitlebold.png)

_____________

# Overview

Developed as a final project for the course Komputer&Creativität(no spelling errors here) at TUM.

* [frontend/](./frontend) contains the Angular Web-App Source files
* [frontend/dist/frontend](./frontend/dist/frontend) contains the compiled static files for use in a Docker contanier
* [backend/](./backend) contains the Python Server and Text-Generation methods
* [doc-g3](./doc/doc-g3.pdf) is the official documentation

# Docker Deployment

Requried installs:

* [Docker](https://docs.docker.com/get-docker/)
* [Docker Compose](https://docs.docker.com/compose/install/)

Build the Backend image (this will download ~1.5GB and may take about 10 Minutes)

        cd ./backend
        docker build -t ww_backend .
        cd ..

Build the Frontend image

        cd ./frontend
        docker build -t ww_frontend .
        cd ..

Execute Docker compose (this will start both containers with appropriate port mapping)

        docker-compose up -d

**Note**: Docker will use about **5GB of RAM** running these containers

# Build locally
Instructions for local execution are provided in the respective README's

* [Frontend](./frontend/README.md)
* [Backend](./backend/README.md)

# Additional Data

The branch complete_repository_snapshot contains additional data that is not immediately relevant for the final product:

* meeting protocols (doc/logbook/)
* training datasets (datasets/)
* prototypes (prototypes/)
