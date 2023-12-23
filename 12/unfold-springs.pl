#!/usr/bin/perl

use strict;
use Memoize;

sub main {
  my $total = 0;
  memoize('permutate');
  while (<>) {
    my $row = $_;
    chomp $row;

    my $score = unfold("$row");
    print $score . "\n";
    $total += $score;
  }
  print $total . "\n";
}

sub unfold {
  my ($rawstring) = @_;

  my ($string, $check) = split(/ /, $rawstring);
  my $unfoldstr = "${string}?${string}?${string}?${string}?${string}";
  my $unfoldchk = "${check},${check},${check},${check},${check}";
#  print "$rawstring\n";
#  print "$unfoldstr $unfoldchk\n";
  return permutate("$unfoldstr $unfoldchk");
}

sub permutate {
  my ($string) = @_;
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
