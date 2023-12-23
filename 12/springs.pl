#!/usr/bin/perl

use strict;

sub main {
  my $total = 0;
  while (<>) {
    my $row = $_;
    chomp $row;

    my $score = permutate("$row");
    print $score . "\n";
    $total += $score;
  }
  print $total . "\n";
}

sub permutate {
  my $string = $_[0];
  my $score;

  if ($string !~ /\Q?\E/) {
#    print $string . "\n";
    return process($string);
  }

  $string =~ /\Q?\E/;
  my $index = $-[0];
  my $z = substr($string, $index, 1, '.');
  $score += permutate($string);
  my $z = substr($string, $index, 1, '#');
  $score += permutate($string);
  return $score;
}

sub process {
  my ($rawstring) = @_;
  my ($string, $check) = split(/ /, $rawstring);
  my @matches = ($string =~ m/(#+)/g);
  my @lengths = ($check =~ m/(\d+)/g);

  # verify same length
  my $a = scalar @matches;
  my $b = scalar @lengths;
  if ($a != $b) { return 0; }

  for (my $iter = 0; $iter < $a; $iter++) {
    my $c = length $matches[$iter];
    if ($c != $lengths[$iter]) {
      return 0;
    }
#    print $iter . ",";
#    print $matches[$iter] . ",";
#    print $c . ",";
#    print $lengths[$iter] . "\n";
  }
#  print "MATCH\n";
  return 1;
}

main();
