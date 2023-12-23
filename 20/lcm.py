#!/usr/bin/python

cdval = [3793,3795,3809,3811,4017,4019,4033,4035]
cdmult = 4032
rkval = [3733,3735,3749,3751,3765,3767,3781,3783,3925,3927,3941,3943,3957,3959,3973,3975]
rkmult = 3968
qxval = [4057,4059,4085,4087]
qxmult = 4088
zfval = [3947,3951,3963,3967,4075,4079,4091,4095]
zfmult = 4096
bigdict = {}

keep_going = 1
while keep_going == 1:
  for i in range(len(cdval)):
    if cdval[i] in bigdict:
      val = bigdict[cdval[i]]
      val += 1
      bigdict[cdval[i]] = val
      if val == 4:
        print("VALUE: " + val)
        keep_going = 0
    else:
      bigdict[cdval[i]] = 1
    cdval[i] += cdmult
  for i in range(len(rkval)):
    if rkval[i] in bigdict:
      val = bigdict[rkval[i]]
      val += 1
      bigdict[rkval[i]] = val
      if val == 4:
        print("VALUE: " + val)
        keep_going = 0
    else:
      bigdict[rkval[i]] = 1
    rkval[i] += rkmult
  for i in range(len(qxval)):
    if qxval[i] in bigdict:
      val = bigdict[qxval[i]]
      val += 1
      bigdict[qxval[i]] = val
      if val == 4:
        print("VALUE: " + val)
        keep_going = 0
    else:
      bigdict[qxval[i]] = 1
    qxval[i] += qxmult
  for i in range(len(zfval)):
    if zfval[i] in bigdict:
      val = bigdict[zfval[i]]
      val += 1
      bigdict[zfval[i]] = val
      if val == 4:
        print("VALUE: " + val)
        keep_going = 0
    else:
      bigdict[zfval[i]] = 1
    zfval[i] += zfmult

