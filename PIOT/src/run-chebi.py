#!/usr/bin/env python
# coding=utf-8
import os
import time
import subprocess
from signal import SIGTERM   
inputFilePathDic = ["/chebi-3/", "/chebi-3-2/", "/chebi-3-3/","/chebi-4/","/chebi-4-2/" ,"/chebi-4-3/"];
queryFileName = "../examples/chebi-query";
def command_line():
  for inputFilePath in inputFilePathDic:
    for i in range(1,5):
      if (i == 1) and (inputFilePath != "/chebi-3/"):
        continue;
      cmd = "{ time ./cal " + str(i) + " ";
      cmd += "../examples" + inputFilePath + " ";
      if (i==3) or (i==4):
        cmd += "chebi-with-priority";
      elif (i==2):
        cmd += "chebi-with-weight";
      else:
        cmd += "chebi";
      cmd += " ../result" + inputFilePath + " " + queryFileName + "; } 2>../result"+inputFilePath+"Time"+str(i);
      print(cmd);
      p = subprocess.Popen(cmd, shell=True);
      t = 0
      while (p.poll() is None):
        time.sleep(1);
        t += 1;
        if (t > 1800):
          p.terminate();
  
command_line()
