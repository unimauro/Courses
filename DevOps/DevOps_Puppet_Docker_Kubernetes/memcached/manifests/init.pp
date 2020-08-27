class memcached {
package { 'memcached':
ensure => installed,
}
file { '/etc/memcached.conf':
source => 'puppet:///modules/memcached/memcached.conf',
owner
=> 'root',
group
=> 'root',
mode
=> '0644',
require => Package['memcached'],
}
service {
ensure
enable
require
'memcached':
=> running,
=> true,
=> [Package['memcached'],
File['/etc/memcached.conf']],
}
}
