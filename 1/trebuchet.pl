#!/usr/bin/perl

use strict;

my $calibration = 0;

# Main loop. Remove text characters and process first/last integer.
while (<>) {
  my $row = $_;
  chomp $row;
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
