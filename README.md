AnyHosting - Open Source Web Hosting

To build a local development VM, install Vagrant http://vagrantup.com/ and
Virtualbox http://virtualbox.org/ and then run:

  $ vagrant up

You can then connect to your new VM using:

  $ vagrant ssh

The rest of the directories in this repo are as follows:

- blog
    - public AnyHosting blog http://anyhosting.com/blog
- mockups
    - design concepts for webpanel
- puppet
    - Puppet https://puppetlabs.com/ manifests for AnyHosting
- webpanel
    - Django Web Control Panel
- wrangler
    - Celery worker for configuring Docker (using Shipper)
