# -*- mode: ruby -*-
# vi: set ft=ruby :

Vagrant::Config.run do |config|
  config.vm.box = "thinkstack-raring64.box"
  config.vm.box_url = "https://dl.dropboxusercontent.com/u/547671/thinkstack-raring64.box"

  # Boot with a GUI so you can see the screen. (Default is headless)
  # config.vm.boot_mode = :gui

  MOUNT_POINT = '/home/vagrant/src/anyhosting'
  config.vm.share_folder("vagrant-root", MOUNT_POINT, ".", :nfs => false)

  config.vm.network :hostonly, "10.11.12.13"

  config.vm.provision :puppet do |puppet|
    puppet.manifests_path = "puppet/manifests"
    puppet.manifest_file = "init.pp"
  end
end
