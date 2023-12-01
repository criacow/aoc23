#!/usr/bin/perl

use strict;

my $calibration = 0;

# Main loop. Remove text characters and process first/last integer.
while (<>) {
  my $row = $_;
  chomp $row;

  # This is hideous but I haven't had my coffee and it was the fastest
  # solution I could think of
  $row =~ s/one/o1ne/g;
  $row =~ s/two/t2wo/g;
  $row =~ s/three/th3ree/g;
  $row =~ s/four/fo4ur/g;
  $row =~ s/five/fi5ve/g;
  $row =~ s/six/si6x/g;
  $row =~ s/seven/se7ven/g;
  $row =~ s/eight/ei8ght/g;
  $row =~ s/nine/ni9ne/g;

  $row =~ tr/a-zA-Z//d;

  my $value = sprintf("%d%d", substr($row, 0, 1), substr($row, -1, 1));
  $calibration += $value;
}

# A tiny bit of error handling.
if ($calibration == 0) {
  print "No valid data received. Usage:\n";
  print "  perl 1.pl < text\n";
}

print $calibration . "\n";
