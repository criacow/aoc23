#!/usr/bin/perl

use Games::Cards::Poker;
use strict;

my @hands;

while (<>) {
  my @row = split(undef, $_);
  my ($raw_hand, $bid) = split(" ", $_);
  my $hand_type;
  my $hand_type = 0;
  if ($raw_hand =~ m/J/) {
    for my $k (2..14) {
      my $token;
      if ($k == 14) { $token = "A"; }
      elsif ($k == 13) { $token = "K"; }
      elsif ($k == 12) { $token = "Q"; }
      elsif ($k == 11) { $token = "J"; }
      elsif ($k == 10) { $token = "T"; }
      else { $token = $k };
      my $test_hand = $raw_hand;
      $test_hand =~ s/J/$token/g;
      my $test_score = Games::Cards::Poker::HandScore(Games::Cards::Poker::SortCards(split(//, $test_hand)));
      my $test_hand_type;
      if ($test_score == 7462) { $test_hand_type = 7; }
      if (!$test_hand_type) {
        my $hand_name = Games::Cards::Poker::HandName($test_score);
        if ($hand_name eq "Four-of-a-Kind") { $test_hand_type = 6; }
        if ($hand_name eq "Full House") { $test_hand_type = 5; }
        if ($hand_name eq "Three-of-a-Kind") { $test_hand_type = 4; }
        if ($hand_name eq "Two Pair") { $test_hand_type = 3; }
        if ($hand_name eq "One Pair") { $test_hand_type = 2; }
        if (($hand_name eq "High Card") || ($hand_name eq "Straight")) { $test_hand_type = 1; }
      }
      if ($test_hand_type > $hand_type) { $hand_type = $test_hand_type; }
    }
  } else {
    my $score = Games::Cards::Poker::HandScore(Games::Cards::Poker::SortCards(split(//, $raw_hand)));
    if ($score == 7462) { $hand_type = 7; }
    if (!$hand_type) {
      my $hand_name = Games::Cards::Poker::HandName($score);
      if ($hand_name eq "Four-of-a-Kind") { $hand_type = 6; }
      if ($hand_name eq "Full House") { $hand_type = 5; }
      if ($hand_name eq "Three-of-a-Kind") { $hand_type = 4; }
      if ($hand_name eq "Two Pair") { $hand_type = 3; }
      if ($hand_name eq "One Pair") { $hand_type = 2; }
      if (($hand_name eq "High Card") || ($hand_name eq "Straight")) { $hand_type = 1; }
    }
  }
    
  my $sort_hand = $raw_hand;
  $sort_hand =~ s/A/S/g;
  $sort_hand =~ s/J/A/g;
  $sort_hand =~ s/T/J/g;
  $sort_hand =~ s/K/R/g;
  $sort_hand =~ tr/2-9/B-I/;
  push @hands, [ ($raw_hand,$sort_hand,$hand_type,$bid) ];
}

my @sort_hands = sort { ($a->[2] <=> $b->[2]) || 
                                ($a->[1] cmp $b->[1]) } @hands;

my $sum = 0;
for my $i ( 0 .. $#sort_hands ) {
    my $handnum = $i + 1;
    my $value = $handnum * $sort_hands[$i][3];
    $sum += $value;
}

print "$sum . \n";
