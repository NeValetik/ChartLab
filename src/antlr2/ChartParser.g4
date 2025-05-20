parser grammar ChartParser;

options {
    tokenVocab=ChartLexer;
}

program
    : statement+ EOF
    ;

statement
    : loop
    | command
    ;

loop
    : WHILE LPAREN condition RPAREN LBRACE statement+ RBRACE
    ;

command
    : WITH data FROM table CHART chartFunction (LBRACE statement+ RBRACE)?
    ;

// Optional block rule (if needed)
block
    : LBRACE statement+ RBRACE
    ;

chartFunction
    : COMPARE var FOR cases
    | DIFFERENCES var FOR cases
    | CONTRAST var FOR cases
    | VERSUS var FOR cases
    | COMPARE var SPLIT_BY subgroup FOR cases
    | COMPARE var GROUPED_BY subgroup FOR cases
    | DIFFERENCES WITHIN subgroup FOR cases
    | SHOW var STACKED_BY subgroup FOR cases
    | SHOW var SUBGROUPS subgroup FOR cases
    | CORRELATION continuousVar AND continuousVar
    | LOG trendKeyword continuousVar FROM range
    | SHOW_PROPORTION var BY cases
    | SHOW_SHARE var BY cases
    | SHOW_PERCENTAGE var BY cases
    | SHOW_FREQUENCY var (STEP value)?
    | SHOW_DISTRIBUTION var (STEP value)?
    | SHOW_FREQUENCY_BUCKETS var BUCKETS
    | ACCUMULATION continuousVar FOR cases FROM range
    | STACKED_TREND continuousVar FOR cases
    | SCATTER_PLOT var AND var
    | PATTERN var AND var
    | BUBBLE var COMMA var COMMA var FOR cases
    ;

data       : var | continuousVar | var AT var ;
table      : IDENTIFIER ;
var        : IDENTIFIER ;
continuousVar : IDENTIFIER (COMMA IDENTIFIER)* ;
range      : IDENTIFIER TO IDENTIFIER ;
subgroup   : IDENTIFIER ;
cases      : IDENTIFIER ;
trendKeyword : PROGRESSION_OF | TREND_OF | GROWTH_OF ;
value       : IDENTIFIER | NUMBER ;

condition
    : NOT? LPAREN? NOT* logicalOperation ((AND | OR) NOT? logicalOperation)* NOT?
    ;

logicalOperation
    : LPAREN? operationBody RPAREN? logicalOperationSign LPAREN? operationBody RPAREN?
    ;

operationBody
    : LPAREN? operation RPAREN? (operationSign LPAREN? operation RPAREN?)*
    ;

operation
    : IDENTIFIER (operationSign IDENTIFIER)?
    ;

operationSign        : PLUS | MINUS | MULTIPLY | DIVIDE ;
logicalOperationSign : LT | LTE | GT | GTE | EQ | NEQ ;
