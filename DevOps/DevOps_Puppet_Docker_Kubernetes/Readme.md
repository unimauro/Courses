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

t@cookbook ~$ puppet-lint puppet-lint.pp

t@cookbook ~$ puppet-lint puppet-lint.pp

t@cookbook ~$ puppet-lint --no-80chars-check

t@cookbook:~$ mkdir -p .puppet/modules

t@cookbook:~$ cd .puppet/modules

t@cookbook:~/.puppet/modules$ puppet module generate thomas-memcached

t@cookbook:~/.puppet/modules$ ln –s thomas-memcached memcached


