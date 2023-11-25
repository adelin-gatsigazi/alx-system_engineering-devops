# Puppet manifest to install Flask version 2.1.0

# Ensure Python is installed
class { 'python':
  version => 'present',
}

# Install python3-pip package
package { 'python3-pip':
  ensure => 'installed',
  require => Class['python'],
}

# Install Flask using pip
package { 'Flask':
  ensure   => '2.1.0',
  provider => 'pip',
  require  => Package['python3-pip'],
}

