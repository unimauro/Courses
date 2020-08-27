$facter uptime

$uptime

$sudo apt-get install rubygems

$sudo gem install puppet

$mkdir -p .puppet/manifests

$cd .puppet/manifests

$ cd .puppet/manifests

Crear el site.pp
_________________
node default {
file { '/tmp/hello':
content => "Hello, world!\n",
}
}
______________________


