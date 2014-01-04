Exec {
    user => "vagrant",
    logoutput => on_failure,
}

class anyhosting {
    file { "/etc/nginx":
        owner => vagrant,
        group => vagrant,
        mode => 664,
        recurse => true,
        source => "/vagrant/puppet/files/etc/nginx",
        ensure => directory,
        require => Package["nginx"];
    }
}

exec {
    "apt-get-update":
        command => "/usr/bin/apt-get update",
        cwd => "/root",
        user => "root";

    "add-docker-key":
        command => "/usr/bin/curl https://get.docker.io/gpg | apt-key add -",
        cwd => "/root",
        user => "root";

    "add-docker-repo":
        command => '/usr/bin/apt-add-repository "deb http://get.docker.io/ubuntu docker main"',
        require => Exec["add-docker-key"],
        cwd => "/root",
        user => "root";

    "apt-get-update-docker-repo":
        command => "/usr/bin/apt-get update",
        require => Exec["add-docker-repo"],
        cwd => "/root",
        user => "root";
}

package {
    ["nginx", "linux-image-extra-3.8.0-19-generic", "mysql-server"]:
        ensure => latest,
        require => Exec["apt-get-update"];

    "lxc-docker":
        ensure => latest,
        require => Exec["apt-get-update-docker-repo"];
}

group {
    "puppet":
        ensure => "present";
}

include anyhosting
