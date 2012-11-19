Ever wondered how to deploy your Bottle application to Google App Engine with minimum efforts?   
This project is aimed to make prototyping with Bottle + GAE as simple as python apps are tended to be.   

##Installation##
To install **all** the stuf just run:

    python bootstrap.py
    ./bin/buildout

##Running the development server##
execute following command to run your app in Google App Engine development server:

    ./bin/dev_appserver parts/app/

##Run as a normal application##
It's also possible to run your app as a standalone Bottle app by executing following:

    ./bin/python parts/app/main.py

**Note**: This project is still in development, so stay tuned!