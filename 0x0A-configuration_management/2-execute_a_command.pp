# kill process killmenow

exec { 'killmenow':
  command  => 'pkill killmenow',
  path => '/usr/bin/:/usr/local/bin/:/bin/',
}
