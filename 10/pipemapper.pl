#!/usr/bin/perl

use strict;

my @pipemap;
my @drawnmap;

while (<>) {
  my @row = split(undef, $_);
  push @pipemap, [ @row ];
  push @drawnmap, [ @row ];
}

my $distance;
my $direction;
my @coords;
my $do_continue = 1;

for my $y ( 0 .. $#pipemap ) {
    my $aref = $pipemap[$y];
    my $n = @$aref - 1;
    for my $x ( 0 .. $n ) {
        # store
        if ($pipemap[$y][$x] eq "S") {
           @coords = ($x + 1, $y);
           $direction = "E";
        }
        if ($pipemap[$y][$x] ne "\n") {
          $drawnmap[$y][$x] = ".";
        }
    }
}

while ($do_continue) {
    $distance++;
#    print "coords: " . $coords[0] . "," . $coords[1] . "; dir: $direction; dist: $distance\n";
    $drawnmap[$coords[1]][$coords[0]] = $pipemap[$coords[1]][$coords[0]];
    if ($direction eq "W" and $pipemap[$coords[1]][$coords[0]] eq "-") {
        $coords[0] = $coords[0] - 1;
    } elsif ($direction eq "W" and $pipemap[$coords[1]][$coords[0]] eq "L") {
        $coords[1] = $coords[1] - 1;
        $direction = "N";
    } elsif ($direction eq "W" and $pipemap[$coords[1]][$coords[0]] eq "F") {
        $coords[1] = $coords[1] + 1;
        $direction = "S";
    } elsif ($direction eq "E" and $pipemap[$coords[1]][$coords[0]] eq "-") {
        $coords[0] = $coords[0] + 1;
    } elsif ($direction eq "E" and $pipemap[$coords[1]][$coords[0]] eq "J") {
        $coords[1] = $coords[1] - 1;
        $direction = "N";
    } elsif ($direction eq "E" and $pipemap[$coords[1]][$coords[0]] eq "7") {
        $coords[1] = $coords[1] + 1;
        $direction = "S";
    } elsif ($direction eq "N" and $pipemap[$coords[1]][$coords[0]] eq "|") {
        $coords[1] = $coords[1] - 1;
    } elsif ($direction eq "N" and $pipemap[$coords[1]][$coords[0]] eq "7") {
        $coords[0] = $coords[0] - 1;
        $direction = "W";
    } elsif ($direction eq "N" and $pipemap[$coords[1]][$coords[0]] eq "F") {
        $coords[0] = $coords[0] + 1;
        $direction = "E";
    } elsif ($direction eq "S" and $pipemap[$coords[1]][$coords[0]] eq "|") {
        $coords[1] = $coords[1] + 1;
    } elsif ($direction eq "S" and $pipemap[$coords[1]][$coords[0]] eq "J") {
        $coords[0] = $coords[0] - 1;
        $direction = "W";
    } elsif ($direction eq "S" and $pipemap[$coords[1]][$coords[0]] eq "L") {
        $coords[0] = $coords[0] + 1;
        $direction = "E";
    } elsif ($pipemap[$coords[1]][$coords[0]] eq "S") {
        $do_continue = 0;
    } else {
#        print "halp\n";
    }
}

#print "$distance\n";
#print $distance / 2 . "\n";
for my $y ( 0 .. $#drawnmap ) {
    my $aref = $pipemap[$y];
    my $n = @$aref - 1;
    for my $x ( 0 .. $n ) {
        print $drawnmap[$y][$x];
    }
}
