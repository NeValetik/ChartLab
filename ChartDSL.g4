grammar ChartLab;

command: START_PROGRAM 'with data from' table 'chart:' chartFunction END_PROGRAM;

START_PROGRAM: 'BEGIN';
END_PROGRAM: 'END';

chartFunction:
    'compare' var 'for' cases
    | 'differences' var 'for' cases
    | 'contrast' var 'for' cases
    | 'versus' var 'for' cases
    | 'compare' var 'split by' subgroup 'for' cases
    | 'compare' var 'grouped by' subgroup 'for' cases
    | 'differences within' subgroup 'for' cases
    | 'show' var 'stacked by' subgroup 'for' cases
    | 'show' var 'subgroups' subgroup 'for' cases
    | 'show correlation between' continuousVar 'and' continuousVar
    | 'log' trendKeyword continuousVar 'from' range
    | 'show proportion of' var 'by' cases
    | 'show share of' var 'by' cases
    | 'show percentage of' var 'by' cases
    | 'show frequency of' var 'by' range
    | 'show distribution of' var 'by' range
    | 'show frequency in' range 'buckets'
    | 'accumulation of' continuousVar 'for' cases 'from' range
    | 'stacked trend of' continuousVar 'for' cases
    | 'scatter plot of' var 'and' var
    | 'pattern of' var 'and' var
    | 'bubble of' var ',' var ',' var 'for' cases
    ;

table: IDENTIFIER;
var: IDENTIFIER;
subgroup: IDENTIFIER;
cases: IDENTIFIER;

continuousVar: IDENTIFIER (',' IDENTIFIER)*;
range: IDENTIFIER 'to' IDENTIFIER;

trendKeyword: 'progression of' | 'trend of' | 'growth of';

loop: 'while' '(' condition ')' ':';

conditionalStatement: 'if' '(' condition ')';

condition: logicalOperation
           | '!' condition
           | condition ('and' | 'or') condition
           | '(' condition ')';

logicalOperation: operationBody logicalOperationSign operationBody;

operationBody: operation
                  | '(' operation ')'
                  | operationBody operationSign operationBody;

operation:  IDENTIFIER | IDENTIFIER operationSign IDENTIFIER;

operationSign:  '+' | '-' | '*' | '/';

logicalOperationSign: '<' | '<=' | '>' | '>=' | '==' | '!=';

IDENTIFIER: LETTER (LETTER | DIGIT)*;

fragment LETTER: [a-zA-Z];
fragment DIGIT: [0-9];

WS: [ \t\r\n]+ -> skip; // Ignore whitespace


