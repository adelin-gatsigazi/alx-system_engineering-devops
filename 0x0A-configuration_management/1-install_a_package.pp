# Install flask with version 2.1.0 using pip
package { 'flask':
  ensure   => '2.1.0',
  provider => 'pip',
  require  => Package['python3'], # Ensure Python 3 is installed
}

