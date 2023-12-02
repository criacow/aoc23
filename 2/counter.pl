#!/usr/bin/perl

use strict;

my $sum = 0;

# Main loop. Remove text characters and process first/last integer.
while (<>) {
  my $row = $_;
  chomp $row;
  $row =~ s/;/,/g;
  my ($game, $data) = split(/: /, $row);
  my @sets = split(/, /, $data);
  my $is_good = 1;
  foreach (@sets) {
    my ($value, $colour) = split(/ /, $_);
    if (($colour eq "red" && $value > 12) || ($colour eq "green" && $value > 13) || ($colour eq "blue" && $value > 14)) {
      $is_good = 0;
    }
  }
  if ($is_good) {
    my ($header, $gamenum) = split(/ /, $game);
    $sum += $gamenum;
  }
#  my $value = sprintf("%d%d", substr($row, 0, 1), substr($row, -1, 1));
#  $calibration += $value;
}

# A tiny bit of error handling.
if ($sum == 0) {
  print "No valid data received. Usage:\n";
  print "  perl 1.pl < text\n";
}

print $sum . "\n";
