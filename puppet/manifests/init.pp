Exec {
    user => "vagrant",
    logoutput => on_failure
}

class anyhosting {
    file { "/etc/nginx":
        owner => vagrant,
        group => vagrant,
        mode => 664,
        recurse => true,
        source => "/vagrant/puppet/files/etc/nginx",
        ensure => directory,
        require => Package["nginx"]
    }
}

exec {
    "/usr/bin/apt-get update":
        alias => "apt-get-update",
        cwd => "/root",
        user => "root"
}

package {
    "nginx":
        ensure => latest,
        require => Exec["apt-get-update"]
}

group { "puppet":
    ensure => "present"
}

include anyhosting
