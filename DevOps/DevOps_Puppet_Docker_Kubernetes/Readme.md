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

t@cookbook:~/.puppet/manifests$ puppet apply site.pp
t@cookbook:~/puppet/manifests$ cat /tmp/hello

t@cookbook ~$ puppet apply puppet-lint.pp Notice: Compiled catalog
t@cookbook ~$ gem list puppet-lint *** LOCAL GEMS *** puppet-lint


