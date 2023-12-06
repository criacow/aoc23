#!/usr/bin/perl

#!/usr/bin/perl

use strict;

my @times = split(/\s{1,}/, <>);
my @distances = split(/\s{1,}/, <>);

shift @times;
shift @distances;
my $product = 1;

for my $i (0 .. $#times) {
  my $validcount = 0;

  for my $press (0 .. $times[$i]) {
    my $distance = ($times[$i] - $press) * $press;
    if ($distance > $distances[$i]) {
      $validcount++;
    }
  }
  print "$validcount\n";
  $product *= $validcount;
}

print $product . "\n";
