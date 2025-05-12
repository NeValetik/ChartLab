lexer grammar ChartLexer;

// Keywords and literals
WITH               : 'with' ;
FROM               : 'from' ;
CHART              : 'chart:' ;
COMPARE            : 'compare' ;
DIFFERENCES        : 'differences' ;
CONTRAST           : 'contrast' ;
VERSUS             : 'versus' ;
SPLIT_BY           : 'split by' ;
GROUPED_BY         : 'grouped by' ;
SHOW               : 'show' ;
STACKED_BY         : 'stacked by' ;
SUBGROUPS          : 'subgroups' ;
CORRELATION        : 'show correlation between' ;
LOG                : 'log' ;
PROGRESSION_OF     : 'progression of' ;
TREND_OF           : 'trend of' ;
GROWTH_OF          : 'growth of' ;
WITHIN             : 'within' ;
SHOW_PROPORTION    : 'show proportion of' ;
SHOW_SHARE         : 'show share of' ;
SHOW_PERCENTAGE    : 'show percentage of' ;
SHOW_FREQUENCY     : 'show frequency of' ;
SHOW_DISTRIBUTION  : 'show distribution of' ;
SHOW_FREQUENCY_BUCKETS : 'show frequency in' ;
ACCUMULATION       : 'accumulation of' ;
STACKED_TREND      : 'stacked trend of' ;
SCATTER_PLOT       : 'scatter plot of' ;
PATTERN            : 'pattern of' ;
BUBBLE             : 'bubble of' ;
BUCKETS            : 'buckets' ;

BY                 : 'by' ;
AND                : 'and' ;
OR                 : 'or' ;
AT                 : 'at' ;
TO                 : 'to' ;
FOR                : 'for' ;

// Operators and symbols
NOT     : '!' ;
PLUS    : '+' ;
MINUS   : '-' ;
MULTIPLY: '*' ;
DIVIDE  : '/' ;
LT      : '<' ;
LTE     : '<=' ;
GT      : '>' ;
GTE     : '>=' ;
EQ      : '==' ;
NEQ     : '!=' ;

COMMA   : ',' ;
COLON   : ':' ;
LPAREN  : '(' ;
RPAREN  : ')' ;
LBRACE  : '{' ;
RBRACE  : '}' ;
WHILE   : 'while' ;

IDENTIFIER : LETTER (LETTER | DIGIT)* ;

fragment LETTER : [a-zA-Z] ;
fragment DIGIT  : [0-9] ;

// Whitespace
WS : [ \t\n\r]+ -> skip ;
