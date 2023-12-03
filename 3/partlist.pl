#!/usr/bin/perl

use strict;

my @partmap;

while (<>) {
  my @row = split(undef, $_);
  push @partmap, [ @row ];
}

my $sum;
my $stornum;

for my $i ( 0 .. $#partmap ) {
    my $aref = $partmap[$i];
    my $n = @$aref - 1;
    for my $j ( 0 .. $n ) {
        # store
        if ($partmap[$i][$j] =~ /\d/) {
           $stornum .= $partmap[$i][$j];
        } else {
          # process
          if ($stornum) {
            my $xstart = $j - (length($stornum)) - 1;
            if ($xstart < 0) { $xstart = 0 }
            my $ystart = $i - 1;
            if ($ystart < 0) { $ystart = 0 }
            my $xend = $j;
            if ($xend > ($n - 1)) { $xend = ($n - 1); }
            my $yend = $i + 1;
            if ($yend > $#partmap) { $yend = $#partmap; }

            my $add_it = 0;
            for my $y ( $ystart .. $yend ) {
              for my $x ( $xstart .. $xend ) {
                if ($partmap[$y][$x] =~ /[^0-9.]/) {
		  $add_it = 1;
                }
              }
            }

            if ($add_it == 1) {
              $sum += $stornum;
            }            
            $stornum = "";
          }
        }
    }
}

print "$sum\n";
