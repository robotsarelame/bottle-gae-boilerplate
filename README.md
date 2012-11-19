Ever wonder how to deploy your Bottle application to Google App Engine with minimum effort?
This project is aimed to make prototyping with Bottle + GAE as simple as python apps are tended to be.   

##Installation##
to install **all** the stuff just run:

    python bootstrap.py
    ./bin/buildout

##Running the Development Server##
execute following command to run your app in Google App Engine development server:

    ./bin/dev_appserver parts/app

##Running as a Normal Application##
it's also possible to run your app as a standalone Bottle app by executing following:

    ./bin/python parts/app/main.py

##Deploying to Real World##
deploy your application to Google App Engine by executing following:

    ./bin/appcfg update parts/app

more info concerning _appcfg_ can be found in [official Google's documentation](https://developers.google.com/appengine/docs/python/tools/uploadinganapp)

**Note**: This project is still in development, so stay tuned!