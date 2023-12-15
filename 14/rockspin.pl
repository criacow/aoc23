#!/usr/bin/perl

use strict;

my @dishmap;
my @rocks;

my $y = 0;
my $max_x = 0;
my $max_y = 0;
while (<>) {
  my @row = split(undef, $_);
  $max_x = $#row;

  for my $x ( 0 .. $#row ) {
    if ($row[$x] eq "O") {
      push(@rocks, "$x,$y");
    }
  }

  push @dishmap, [ @row ];
  $y++;
}

$max_y = $#dishmap;

#print "before:\n";
#for my $g ( 0 .. $#rocks ) {
#  print "Rock $g: $rocks[$g]\n";
#}

my @previous_spin;
my $iter = 1;
my $keep_going = 1;
while ($iter <= 1000000000 and $keep_going) {
#while ($iter <= 1 and $keep_going) {
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

#  for my $m ( 0 .. $#dishmap) {
#    for my $a ( 0 .. $max_x ) {
#      print $dishmap[$m][$a];
#    }
#  }
#  print "\n";

  @rocks = sort x_coord_sort @rocks;

  for my $r ( 0 .. $#rocks) {
    my ($rockx,$rocky) = split(/,/, $rocks[$r]);
    if ($rockx > 0) {
      my $going = 1;
      while ($going) {
        if (($dishmap[$rocky][$rockx-1] eq ".") and ($rockx > 0)) {
          $dishmap[$rocky][$rockx-1] = "O";
          $dishmap[$rocky][$rockx] = ".";
          $rockx--;
        } else {
          $going = 0;
        }
      }
    $rocks[$r] = "$rockx,$rocky";        
    }
  }

#  for my $m ( 0 .. $#dishmap) {
#    for my $a ( 0 .. $max_x ) {
#      print $dishmap[$m][$a];
#    }
#  }
#  print "\n";

  @rocks = reverse sort y_coord_sort @rocks;

  for my $r ( 0 .. $#rocks) {
    my ($rockx,$rocky) = split(/,/, $rocks[$r]);
    if ($rocky < $max_y) {
      my $going = 1;
      while ($going) {
        if (($dishmap[$rocky+1][$rockx] eq ".") and ($rocky < $max_y)) {
          $dishmap[$rocky+1][$rockx] = "O";
          $dishmap[$rocky][$rockx] = ".";
          $rocky++;
        } else {
          $going = 0;
        }
      }
    $rocks[$r] = "$rockx,$rocky";        
    }
  }

#  for my $m ( 0 .. $#dishmap) {
#    for my $a ( 0 .. $max_x ) {
#      print $dishmap[$m][$a];
#    }
#  }
#  print "\n";

  @rocks = reverse sort x_coord_sort @rocks;

  for my $r ( 0 .. $#rocks) {
    my ($rockx,$rocky) = split(/,/, $rocks[$r]);
    if ($rockx < $max_x) {
      my $going = 1;
      while ($going) {
        if (($dishmap[$rocky][$rockx+1] eq ".") and ($rockx < $max_x)) {
          $dishmap[$rocky][$rockx+1] = "O";
          $dishmap[$rocky][$rockx] = ".";
          $rockx++;
        } else {
          $going = 0;
        }
      }
    $rocks[$r] = "$rockx,$rocky";        
    }
  }

  print "iter: $iter, ";
#  for my $m ( 0 .. $#dishmap) {
#    for my $a ( 0 .. $max_x ) {
#      print $dishmap[$m][$a];
#    }
#  }
#
  my $weight = 0;
  for my $r ( 0 .. $#rocks) {
    my ($rockx,$rocky) = split(/,/, $rocks[$r]);
    $weight += ($max_y + 1 - $rocky);  
  }
  print "weight: $weight\n";
#  print "---\n";

  @rocks = sort y_coord_sort @rocks;

#  if (isIdentical(\@previous_spin,\@rocks)) {
#  if (@previous_spin ~~ @dishmap) {
#    $keep_going = 0;
#  }
#  print @previous_spin;
#  print "\n";
#  print @rocks;
#  print "\n";

  @previous_spin = @dishmap;

  $iter++; 

  if (!($iter % 1000000)) { print "$iter\n"; }
}
print "after:\n";
for my $g ( 0 .. $#rocks ) {
  print "Rock $g: $rocks[$g]\n";
}
print "iter: $iter\n";

my $weight = 0;
my $maxweight = $#dishmap + 1;
for my $r ( 0 .. $#rocks) {
  my ($rockx,$rocky) = split(/,/, $rocks[$r]);
  $weight += ($maxweight - $rocky);  
}

#my $weight = 0;
#for my $r ( 0 .. $#rocks) {
#  my ($rockx,$rocky) = split(/,/, $rocks[$r]);
#  $weight += $rockx + 1;
#}

print "$weight\n";
exit 0;

sub x_coord_sort{
  my ($ax, $ay) = split(/,/, $a);
  my ($bx, $by) = split(/,/, $b);
  if ($ax < $bx) { return -1; }
  elsif ($ax == $bx) { return 0; }
  else { return 1; }
}

sub y_coord_sort{
  my ($ax, $ay) = split(/,/, $a);
  my ($bx, $by) = split(/,/, $b);
  if ($ay < $by) { return -1; }
  elsif ($ay == $by) { return 0; }
  else { return 1; }
}

sub isIdentical {
   my( $left, $right ) = @_;
   return 0 if scalar @$left != scalar @$right;
   my %hash;
   @hash{ @$left, @$right } = ();
   return scalar keys %hash == scalar @$left;
}
