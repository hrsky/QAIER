QSAT
=====
This project is for the experiment of query entailment of inconsistent ontology

Install
=====
1. compile the qrepair: g++ src/*.cpp -o qrepair
2. download the Minisat 2.2.0:
    from http://minisat.se/MiniSat.html
    or sudo apt-get install minisat in Linux
    or sudo brew install minisat in Mac OS

Usage
=====
1. Input file should be added query and already grounded. 
   Warning: query form is q :- a(X,Y), b(Y). and after grounded it would be q :-. which is empty in body.
2. Put the input file in res/input/;
3. Run command:
   ./qrepair res/input/YOUR FILE | minisat
   Certainly, you can use one of them alone, like: ./qrepair res/input/YOUR FILE res/output/ will print the output of qrepair into the document.
4. Result:
   If our program find a success repair and find the query, it will print SAT, otherwise Unsat. 

Examples
=====
Some examples are in res/input/lubm/, which is transformed from the benchmark of the experiment in paper: Query Answering with Inconsistent Existential Rules under Stable Model Semantics, ID: IJCAI2015-KR #222.
The examples has different database size and two kinds of TBox which cause inconsistent.
the last number in file name represents the number of incorrect rules in TBox. 2 means there is 3 incorrect rules and 3 means 5.
If you want to run a examples, input: ./qrepair res/input/lubm/lubm-u5-2 | minisat.