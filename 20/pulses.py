#!/usr/bin/python3
import sys

components = {}
signalqueue = []
total_low_count = 0
total_high_count = 0

def low_signal(component):
  global signalqueue
  if components[component]["type"] == "broadcaster":
    for i in components[component]["outputs"]:
      if components[i]["type"] == "conj":
        for j in range(len(components[i]["inputs"])):
          if component == components[i]["inputs"][j]:
            components[i]["inputstate"][j] = 0
#      print(component + " -low-> " + i)
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
#        print(component + " -high-> " + i)
        signal = "high," + i
        signalqueue.append(signal)
    else:
      components[component]["state"] = 0
      for i in components[component]["outputs"]:
        if components[i]["type"] == "conj":
          for j in range(len(components[i]["inputs"])):
            if component == components[i]["inputs"][j]:
              components[i]["inputstate"][j] = 0
#        print(component + " -low-> " + i)
        signal = "low," + i
        signalqueue.append(signal)
  elif components[component]["type"] == "conj":
    for i in components[component]["outputs"]:
      if components[i]["type"] == "conj":
        for j in range(len(components[i]["inputs"])):
          if component == components[i]["inputs"][j]:
            components[i]["inputstate"][j] = 1
#      print(component + " -high-> " + i)
      signal = "high," + i
      signalqueue.append(signal)
  global total_low_count
  total_low_count += 1

def high_signal(component):
  global signalqueue
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
#      print(component + " -low-> " + i)
      signal = "low," + i
      signalqueue.append(signal)
    else:
      for i in components[component]["outputs"]:
        if components[i]["type"] == "conj":
          for j in range(len(components[i]["inputs"])):
            if component == components[i]["inputs"][j]:
              components[i]["inputstate"][j] = 1
#        print(component + " -high-> " + i)
        signal = "high," + i
        signalqueue.append(signal)
  global total_high_count
  total_high_count += 1

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

for i in range(1000):
  low_signal("broadcaster")
#  print("button: " + str(i+1))

  while(len(signalqueue) > 0):
    type,dest = signalqueue.pop(0).split(",")
    if type == "low":
      low_signal(dest)
    else:
      high_signal(dest)

print("low: " + str(total_low_count))
print("high: " + str(total_high_count))
print("return: " + str(total_low_count * total_high_count))
