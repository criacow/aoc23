#!/usr/bin/perl

use strict;

my @dishmap;
my @rocks;

my $y = 0;
while (<>) {
  my @row = split(undef, $_);

  for my $x ( 0 .. $#row ) {
    if ($row[$x] eq "O") {
      push(@rocks, "$x,$y");
    }
  }

  push @dishmap, [ @row ];
  $y++;
}

#print "before:\n";
#for my $g ( 0 .. $#rocks ) {
#  print "Rock $g: $rocks[$g]\n";
#}

for my $r ( 0 .. $#rocks) {
  my ($rockx,$rocky) = split(/,/, $rocks[$r]);
  if ($rocky > 0) {
    my $going = 1;
    while ($going) {
      if (($dishmap[$rocky-1][$rockx] eq ".") and ($rocky > 0)) {
        $dishmap[$rocky-1][$rockx] = "O";
        $dishmap[$rocky][$rockx] = ".";
        $rocky--;
      } else {
        $going = 0;
      }
    }
  $rocks[$r] = "$rockx,$rocky";        
  }
}

#print "after:\n";
#for my $g ( 0 .. $#rocks ) {
#  print "Rock $g: $rocks[$g]\n";
#}

my $weight = 0;
my $maxweight = $#dishmap + 1;
for my $r ( 0 .. $#rocks) {
  my ($rockx,$rocky) = split(/,/, $rocks[$r]);
  $weight += ($maxweight - $rocky);  
}

print "$weight\n";
