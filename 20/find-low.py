#!/usr/bin/python3
import sys

components = {}
signalqueue = []
buttonpress = 0

def low_signal(component):
  global signalqueue
  if components[component]["type"] == "broadcaster":
    for i in components[component]["outputs"]:
      if components[i]["type"] == "conj":
        for j in range(len(components[i]["inputs"])):
          if component == components[i]["inputs"][j]:
            components[i]["inputstate"][j] = 0
      signal = "low," + i
      signalqueue.append(signal)
  elif components[component]["type"] == "flip":
    if components[component]["state"] == 0:
      components[component]["state"] = 1
      for i in components[component]["outputs"]:
        if components[i]["type"] == "conj":
          for j in range(len(components[i]["inputs"])):
            if component == components[i]["inputs"][j]:
              components[i]["inputstate"][j] = 1
        signal = "high," + i
        signalqueue.append(signal)
    else:
      components[component]["state"] = 0
      for i in components[component]["outputs"]:
        if components[i]["type"] == "conj":
          for j in range(len(components[i]["inputs"])):
            if component == components[i]["inputs"][j]:
              components[i]["inputstate"][j] = 0
        signal = "low," + i
        signalqueue.append(signal)
  elif components[component]["type"] == "conj":
    for i in components[component]["outputs"]:
      if components[i]["type"] == "conj":
        for j in range(len(components[i]["inputs"])):
          if component == components[i]["inputs"][j]:
            components[i]["inputstate"][j] = 1
      signal = "high," + i
      signalqueue.append(signal)

def high_signal(component):
  global signalqueue
  global buttonpress
  if components[component]["type"] == "conj":
    is_low = 1
    for i in components[component]["inputstate"]:
      if i == 0:
        is_low = 0
    if is_low:
      for i in components[component]["outputs"]:
        if components[i]["type"] == "conj":
          for j in range(len(components[i]["inputs"])):
            if component == components[i]["inputs"][j]:
              components[i]["inputstate"][j] = 0
      if i == "rx":
        print(component + " -low-> " + i)
        print("buttonpress: " + str(buttonpress+1))
        sys.exit(0)
      signal = "low," + i
      signalqueue.append(signal)
    else:
      for i in components[component]["outputs"]:
        if components[i]["type"] == "conj":
          for j in range(len(components[i]["inputs"])):
            if component == components[i]["inputs"][j]:
              components[i]["inputstate"][j] = 1
        signal = "high," + i
        signalqueue.append(signal)

for line in sys.stdin:
    cname,coutputs = line.strip().split(" -> ")
    component = {}
    olist = coutputs.split(", ")
    cn = ""
    if cname == "broadcaster":
      cn = "broadcaster"
      component = {
        "type": "broadcaster",
        "state": 0,
        "outputs": olist,
        "inputs": [],
        "inputstate": []
      }
    elif cname[0] == "%":
      cn = cname[1:]
      component = {
        "type": "flip",
        "state": 0,
        "outputs": olist,
        "inputs": [],
        "inputstate": []
      }
    elif cname[0] == "&":
      cn = cname[1:]
      jname = cname[1:]
      inputs = []
      inputstate = []
      if jname in components:
        inputs = components[jname]["inputs"]
        inputstate = components[jname]["inputstate"]
      component = {
        "type": "conj",
        "state": 0,
        "outputs": olist,
        "inputs": inputs,
        "inputstate": inputstate
      }
    components[cn] = component
    for o in olist:
      if o in components:
        components[o]["inputs"].append(cn)
        components[o]["inputstate"].append(0)
      else:
        fcomp = {
          "type": "unknown",
          "state": 0,
          "outputs": [],
          "inputs": [ cn ],
          "inputstate": [ 0 ]
        }
        components[o] = fcomp

for buttonpress in range(100000):
  low_signal("broadcaster")

  while(len(signalqueue) > 0):
    type,dest = signalqueue.pop(0).split(",")
    if type == "low":
      low_signal(dest)
    else:
      high_signal(dest)

  display = 1
  diag = "press: " + str(buttonpress) + "; "
  for i in range(len(components["gh"]["inputs"])):
    if components["gh"]["inputstate"][i] == 0:
      display = 0
    diag += components["gh"]["inputs"][i] + "(" + str(components["gh"]["inputstate"][i]) + "); "
  if display == 1:
    print(diag)
