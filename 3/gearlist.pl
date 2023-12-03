#!/usr/bin/perl

use strict;

my @partmap;

while (<>) {
  my @row = split(undef, $_);
  push @partmap, [ @row ];
}

my $sum;
my $stornum;
my %gearcount;
my %geardata;

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

            for my $y ( $ystart .. $yend ) {
              for my $x ( $xstart .. $xend ) {
                if ($partmap[$y][$x] =~ /[*]/) {
		  my $key = "$y,$x";
                  $gearcount{"$key"} += 1;
                  if ($geardata{"$key"} == 0) {
                    $geardata{"$key"} += 1;
                  }
                  $geardata{"$key"} *= $stornum;
                }
              }
            }

            $stornum = "";
          }
        }
    }
}

for(keys %gearcount) {
   if ($gearcount{$_} == 2) {
      $sum += $geardata{$_};
   }
#   print "Coord: $_  Count: $gearcount{$_}  Product: $geardata{$_}\n";
}

print "$sum\n";
