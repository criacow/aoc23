#!/usr/bin/perl

use strict;

my %nodelist;
my $path = <>;
chomp $path;
my $skip = <>;
my %cur_locs;

while (<>) {
  $_ =~ /^(\w*) = \((\w*), (\w*)\)$/;
  my $name = $1;
  my $left = $2;
  my $right = $3;
  if ($name =~ m/A$/) {
    $cur_locs{"$name"} = $name;
  }
  $nodelist{"$name-L"} = $left;
  $nodelist{"$name-R"} = $right;
}

my $steps;

my $end_signal = 1;
while ($end_signal) {
  for my $i (0..(length($path)-1)) {
    my $direction = substr($path, $i, 1);
    my $not_end = 1;
    $steps++;

    for(keys %cur_locs) {
      $cur_locs{$_} = $nodelist{"$cur_locs{$_}-$direction"};
      if ($cur_locs{$_} !~ /Z$/) { $not_end = 0; }

      # Usually I clear my debugging before uploading. But this is the
      # one that helped me figure it out -- I thought I had maybe made
      # an infinite loop or something. But looking at the data I saw
      # six paths in test.txt and all repeated at regular intervals.
      # So the solution was to take the least common multiple of the six.

      # Glad that worked, as it was a 14-digit number, so brute forcing
      # it would've taken an eternity...
      if ($cur_locs{$_} =~ /Z$/) {
        print "step: $steps-$_\tgoing $direction\tto $cur_locs{$_}\n";
      }
    }
    if ($not_end == 1) { $end_signal = 0; last; }
  }
}    

print "$steps\n";
