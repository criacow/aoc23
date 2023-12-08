#!/usr/bin/perl

use strict;

my %nodelist;
my $path = <>;
chomp $path;
my $skip = <>;

while (<>) {
  $_ =~ /^(\w*) = \((\w*), (\w*)\)$/;
  my $name = $1;
  my $left = $2;
  my $right = $3;
  $nodelist{"$name-L"} = $left;
  $nodelist{"$name-R"} = $right;
}

my $steps;
my $cur_loc = "AAA";

while (1) {
  for my $i (0..(length($path)-1)) {
    my $direction = substr($path, $i, 1);
    $cur_loc = $nodelist{"$cur_loc-$direction"};
    $steps++;
    if ($cur_loc eq "ZZZ") { last; }
  }
  if ($cur_loc eq "ZZZ") { last; }
}    

print "$steps\n";
