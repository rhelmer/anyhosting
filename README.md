AnyHosting - Open Source Web Hosting

To build a local development VM, install Vagrant http://vagrantup.com/ and
Virtualbox http://virtualbox.org/ and then run:

  $ vagrant up

You can then connect to your new VM using:

  $ vagrant ssh

The rest of the directories in this repo are as follows:

- blog
    - public AnyHosting blog http://anyhosting.com/blog
- control\_panel
    - Django Web Control Panel
- mockups
    - design concepts for control\_panel
- puppet
    - Puppet https://puppetlabs.com/ manifests for AnyHosting
