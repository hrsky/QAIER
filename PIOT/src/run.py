#!/usr/bin/env python
# coding=utf-8
import os
import subprocess
queryFileName = "../examples/lubm-query";
inputFilePathDic = ["/lubm-u9-3/"];
def cline():
  for inputFilePath in inputFilePathDic:
    for i in range(2,3):
      cmd = "{ time ./cal " + str(i) + " ";
      cmd += "../examples" + inputFilePath + " ";
      if (i == 3) or (i == 4):
        cmd += "lubm-with-priority";
      elif (i == 2):
        cmd += "lubm-with-weight";
      else:
        cmd += "lubm";
      cmd += " ../result" + inputFilePath + " " + queryFileName + " ;} 2>";
      cmd += " ../result" + inputFilePath + "Time-" + str(i);
      print(cmd);
      os.system(cmd);
cline()
