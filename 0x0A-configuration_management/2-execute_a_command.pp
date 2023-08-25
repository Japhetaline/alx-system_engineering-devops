# script to execute a command using puppet
exec { 'killmenow':
  command => 'pkill -f killmenow',
  path    => '/usr/bin/',
  onlyif  => 'pgrep -f killmenow',
}
