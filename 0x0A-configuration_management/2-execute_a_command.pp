# kill process killmenow

exec { 'killmenow':
  command  => 'pkill killmenow',
}
