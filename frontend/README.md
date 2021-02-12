# Local Development environment

## Required installs

* [NodeJS](https://nodejs.org/en/download/)
* Angular CLI (allows use of "ng" commands)

        npm install -g @angular/cli

## First time cloning 
Install necessary node_modules

        npm i

## Start
Host Web-App on port 8080 and opens the adress in the default browser

        ng serve -o --port 8080

___________________________
___________________________
# Build
Create compiled output that can be hosted by a Static File provider

        ng build --prod --build-optimizer
        
