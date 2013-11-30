AnyHosting Web Control Panel

Installation
-------------

First, set up your environment:

  $ sudo pip install virtualenvwrapper
  $ source /usr/local/bin/virtualenvwrapper.sh 
  $ mkvirtualenv webpanel

Then, install dependencies:

  $ pip install -r requirements.txt

Finally, run it:

  $ python manage.py runserver

If all went well, you should see something similar to the following:

  Validating models...

  0 errors found
  November 30, 2013 - 01:30:53
  Django version 1.6, using settings 'webpanel.settings'
  Starting development server at http://127.0.0.1:8000/
  Quit the server with CONTROL-C.

Your dev site is now available at http://127.0.0.1:8000
