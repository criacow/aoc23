#!/usr/bin/perl

use strict;

sub z_coord_sort{
  my ($astart, $aend) = split(/~/, $a);
  my ($ax, $ay, $az) = split(/,/, $astart);

  my ($bstart, $bend) = split(/~/, $b);
  my ($bx, $by, $bz) = split(/,/, $bstart);

  if ($az < $bz) { return -1; }
  elsif ($az == $bz) { return 0; }
  else { return 1; }
}

my @inputs;

while (<>) {
  push(@inputs, $_);
}

my @outputs = sort z_coord_sort @inputs;

for my $x ( 0 .. $#outputs ) {
  print($outputs[$x]);
}
