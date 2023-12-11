#!/usr/bin/perl

use strict;

my @galaxymap;

while (<>) {
  my @row = split(undef, $_);
  push @galaxymap, [ @row ];
}

my %galaxies;
my $gcount = 0;
my $max_x;
my $max_y = $#galaxymap;

# Find all the galaxies.
for my $y ( 0 .. $#galaxymap ) {
    my $aref = $galaxymap[$y];
    $max_x = @$aref - 1;
    for my $x ( 0 .. $max_x ) {
        if ($galaxymap[$y][$x] eq '#') {
           $galaxies{"$gcount-X"} = $x;
           $galaxies{"$gcount-Y"} = $y;
           $gcount++;
        }
    }
}

$gcount--;

#print "before:\n";
#for my $g ( 0 .. $gcount ) {
#    print "Galaxy $g: (" . $galaxies{"$g-X"} . "," . $galaxies{"$g-Y"} . ")\n";
#}

# Expand space. For parts one and two, adjust the constant below.
my $expand_rate = 999999;
my $x = 0;
while ($x <= $max_x ) {
    my $expand = 1;
    for(keys %galaxies) {
      if ($_ =~ /X$/) {
        if ($galaxies{$_} == $x) { $expand = 0 };
      }
    }

    if ($expand) {
      for(keys %galaxies) {
        if ($_ =~ /X$/) {
          if ($galaxies{$_} > $x) { $galaxies{$_} += $expand_rate; }
        }
      }
      $max_x += $expand_rate;
      $x += $expand_rate;
    }
    $x++;
}

my $y = 0;
while ($y <= $max_y ) {
    my $expand = 1;
    for(keys %galaxies) {
      if ($_ =~ /Y$/) {
        if ($galaxies{$_} == $y) { $expand = 0 };
      }
    }

    if ($expand) {
      for(keys %galaxies) {
        if ($_ =~ /Y$/) {
          if ($galaxies{$_} > $y) { $galaxies{$_} += $expand_rate; }
        }
      }
      $max_y += $expand_rate;
      $y += $expand_rate;
    }
    $y++;
}

#print "after:\n";
#for my $g ( 0 .. $gcount ) {
#    print "Galaxy $g: (" . $galaxies{"$g-X"} . "," . $galaxies{"$g-Y"} . ")\n";
#}

# Create path list.
my %paths;
for my $g ( 0 .. $gcount ) {
  for my $h ( 0 .. $gcount ) {
    if ($g < $h) {
      $paths{"$g-$h"} = 1;
    }
  }
}

# Calculate each path.
my $total_distance;
for(keys %paths) {
  my ($start, $end) = split(/-/, $_);
  my $x = abs($galaxies{"$end-X"} - $galaxies{"$start-X"});
  my $y = abs($galaxies{"$end-Y"} - $galaxies{"$start-Y"});
#  print "$start-$end\t$x,$y\n";
  $paths{$_} = $x + $y;
#  print "path $_: $paths{$_}\n";
  $total_distance += ($x + $y);
}

print "$total_distance\n";
