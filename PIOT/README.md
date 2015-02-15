PIOT
=====
This project is for the experiment of query entailment of inconsistent ontology

Install
=====
1. Compile:
   cd src/
   make
2. Prepare benchmarks for experiment:
   Put your benchmarks in examples/, which should be a datalog program. If it is with priority or weight, please see the input form in examples/.
   Certainly, we prepare some benchmark in examples and you can use them, please see examples/README.
   Create the folder in result/ whose name is same as your benckmark located, such as lubm-u5-2.
3. Run a benchmark:
   ./cal 1 ../examples/lubm-u5-2/ lubm ../result/lubm-u5-2/ ../examples/lubm-query
   the parameters:
     first: 0 for IncMax, 1 for CardMax, 2 for WeightMax, 3 for PrefIncMax and 4 for PrefCardMax;
     second: the inputed file location;
     third: the inputed file name. please be care that the first and third parameter should be corresponding, 		such as 1 for lubm, 2 for lubm-with-weight and 3 for lubm-with-priority;
     fourth: the result output path;
     fifth: the inputed query file;
4. Batch run the benchmarks:
   We prepare some script in python for batch run the test. You can see them in src/run.py and src.run-chebi.py. For different tasks, you may need to modify them.
5. Result:
   The result will output to the path you inputed. Run time and satistic will be recorded.