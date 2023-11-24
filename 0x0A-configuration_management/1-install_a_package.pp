#!/usr/bin/pup


package { 'flask':
  ensure   => '2.1.0',
  provider => 'pip3',
}

notify { 'Flask installed':
  message => 'Flask version 2.1.0 has been installed.',
}
