#!/usr/bin/perl

use strict;

my $sum = 0;

# Main loop. Break data down into component parts and calculate product.
while (<>) {
  my $row = $_;
  chomp $row;
  $row =~ s/;/,/g;
  my ($game, $data) = split(/: /, $row);
  my @sets = split(/, /, $data);
  my ($maxred, $maxgreen, $maxblue);
  foreach (@sets) {
    my ($value, $colour) = split(/ /, $_);
    if ($colour eq "red" && $value > $maxred) {
      $maxred = $value;
    }
    if ($colour eq "green" && $value > $maxgreen) {
      $maxgreen = $value;
    }
    if ($colour eq "blue" && $value > $maxblue) {
      $maxblue = $value;
    }
  }
  my $product = $maxred * $maxgreen * $maxblue;
  $sum += $product;
}

# A tiny bit of error handling.
if ($sum == 0) {
  print "No valid data received. Usage:\n";
  print "  perl 1.pl < text\n";
}

print $sum . "\n";
