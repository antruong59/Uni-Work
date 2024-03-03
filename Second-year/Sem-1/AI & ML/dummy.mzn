% n-queen problem

include "alldifferent.mzn";

int :n;

set of int: Q = 1..n;

array[1..n] of var Q: QueenList; 

constraint alldifferent(QueenList);
constraint forall([abs(QueenList[i] - QueenList[j]) != abs(i - j) | i,j in 1..n where i < j]);

solve satisfy;

output [show(QueenList)];

% int: n;
% array[1..n, 1..n] of var {0, 1}: table;


% solve satisfy;








