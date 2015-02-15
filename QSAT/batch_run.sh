#!/bin/bash

for i in `find res/input/lubm/ -type f`; do
  echo $i
  echo $i >> lubm_experiment_result
  { time ./qrepair -sat $i | minisat ;} 2>> lubm_experiment_result
done
