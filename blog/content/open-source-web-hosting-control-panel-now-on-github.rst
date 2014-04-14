Open Source Web Hosting Control Panel Now On Github
###################################################
:date: 2014-04-13 10:24
:author: Robert Helmer
:category: web hosting
:tags: web hosting, control panel, github, open source

A few years ago I mentioned_ that I was working on an open-source
web hosting control panel, and I have recently picked this back up
based on the latest AnyHosting setup (which is basically nginx+php-fpm
in front, and proxying to Docker_ instances where something more custom
is needed).

I've pushed everything that I am currently working on, including mockups_
(and even this blog!) to the `anyhosting repo`_ on my github account.
NOTE - most things aren't functional yet, I am just working on it in the
open.

The basic architecture is that there is a Django application in the 
webpanel_ directory with two apps - Files and Reports. Files is a file
management application, and Reports gives a basic resource utilization
report for a given website.

There will be an administrative app for creating/destroying sites which
puts messages in RabbitMQ for the wrangler_ application. Wrangler is a
Celery_ worker which creates nginx virtual hosts, and populates
Docker instances using Shipper_.

If you're interested in helping out, now's a great time - open an issue
or pull request on the `anyhosting repo`_ or email me (rhelmer@anyhosting.com)

.. _mentioned: http://anyhosting.com/blog/2010/03/18/new-open-source-web-hosting-control-panel/
.. _Docker: http://docker.io/
.. _`anyhosting repo`: https://github.com/rhelmer/anyhosting
.. _webpanel: https://github.com/rhelmer/anyhosting/tree/master/webpanel
.. _mockups: http://rhelmer.github.io/anyhosting/mockups/reports.html 
.. _wrangler: https://github.com/rhelmer/anyhosting/tree/master/wrangler
.. _Celery: http://r.duckduckgo.com/l/?kh=-1&uddg=http%3A%2F%2Fwww.celeryproject.org%2F
.. _Shipper: https://github.com/mailgun/shipper
