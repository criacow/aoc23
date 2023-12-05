#!/usr/bin/perl

use strict;

my @seeds;
my @seed_soil_map;
my @soil_fert_map;
my @fert_watr_map;
my @watr_ligh_map;
my @ligh_temp_map;
my @temp_humi_map;
my @humi_loca_map;

  # seeds
  @seeds = split(" ", <>);
  my $skip = <>;

  # seed to soil
  my $skip = <>;
  while (<>) {
    if ($_ eq "\n") { last; }
    my @dsr = split(" ", $_);
    push @seed_soil_map, [ @dsr ];
  }

  my $skip = <>;
  while (<>) {
    if ($_ eq "\n") { last; }
    my @dsr = split(" ", $_);
    push @soil_fert_map, [ @dsr ];
  }

  my $skip = <>;
  while (<>) {
    if ($_ eq "\n") { last; }
    my @dsr = split(" ", $_);
    push @fert_watr_map, [ @dsr ];
  }

  my $skip = <>;
  while (<>) {
    if ($_ eq "\n") { last; }
    my @dsr = split(" ", $_);
    push @watr_ligh_map, [ @dsr ];
  }

  my $skip = <>;
  while (<>) {
    if ($_ eq "\n") { last; }
    my @dsr = split(" ", $_);
    push @ligh_temp_map, [ @dsr ];
  }

  my $skip = <>;
  while (<>) {
    if ($_ eq "\n") { last; }
    my @dsr = split(" ", $_);
    push @temp_humi_map, [ @dsr ];
  }

  my $skip = <>;
  while (<>) {
    if ($_ eq "\n") { last; }
    my @dsr = split(" ", $_);
    push @humi_loca_map, [ @dsr ];
  }

  my $location = -1;

  shift(@seeds);
  foreach (@seeds) {
    my $soil = -1;
    for my $dsr ( @seed_soil_map ) {
      if (($_ >= @$dsr[1]) && ($_ < (@$dsr[1] + @$dsr[2]))) {
        $soil = $_ - @$dsr[1] + @$dsr[0];
      }
    }
    if ($soil == -1) {
      $soil = $_;
    }

    my $fert = -1;
    for my $dsr ( @soil_fert_map ) {
      if (($soil >= @$dsr[1]) && ($soil < (@$dsr[1] + @$dsr[2]))) {
        $fert = $soil - @$dsr[1] + @$dsr[0];
      }
    }
    if ($fert == -1) {
      $fert = $soil;
    }

    my $watr = -1;
    for my $dsr ( @fert_watr_map ) {
      if (($fert >= @$dsr[1]) && ($fert < (@$dsr[1] + @$dsr[2]))) {
        $watr = $fert - @$dsr[1] + @$dsr[0];
      }
    }
    if ($watr == -1) {
      $watr = $fert;
    }

    my $ligh = -1;
    for my $dsr ( @watr_ligh_map ) {
      if (($watr >= @$dsr[1]) && ($watr < (@$dsr[1] + @$dsr[2]))) {
        $ligh = $watr - @$dsr[1] + @$dsr[0];
      }
    }
    if ($ligh == -1) {
      $ligh = $watr;
    }

    my $temp = -1;
    for my $dsr ( @ligh_temp_map ) {
      if (($ligh >= @$dsr[1]) && ($ligh < (@$dsr[1] + @$dsr[2]))) {
        $temp = $ligh - @$dsr[1] + @$dsr[0];
      }
    }
    if ($temp == -1) {
      $temp = $ligh;
    }

    my $humi = -1;
    for my $dsr ( @temp_humi_map ) {
      if (($temp >= @$dsr[1]) && ($temp < (@$dsr[1] + @$dsr[2]))) {
        $humi = $temp - @$dsr[1] + @$dsr[0];
      }
    }
    if ($humi == -1) {
      $humi = $temp;
    }

    my $loca = -1;
    for my $dsr ( @humi_loca_map ) {
      if (($humi >= @$dsr[1]) && ($humi < (@$dsr[1] + @$dsr[2]))) {
        $loca = $humi - @$dsr[1] + @$dsr[0];
      }
    }
    if ($loca == -1) {
      $loca = $humi;
    }

    print "$_,$soil,$fert,$watr,$ligh,$temp,$humi,$loca\n";
    if ($location == -1) {
      $location = $loca;
    } elsif ($loca < $location) {
      $location = $loca;
    }
    print "new location: $location\n";
  }

print "$location\n";
