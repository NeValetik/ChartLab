parser grammar ChartParser;

options {
    tokenVocab=ChartLexer;  // Use the lexer rules defined above
}

// Top-level command that starts with 'with' and ends with the chart function
command            : WITH data FROM table CHART chartFunction ;

// Rules for the chart functions, each representing different types of charts
chartFunction      : COMPARE var FOR cases
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
                  | SHOW_FREQUENCY var BY range
                  | SHOW_DISTRIBUTION var BY range
                  | SHOW_FREQUENCY_BUCKETS range BUCKETS
                  | ACCUMULATION continuousVar FOR cases FROM range
                  | STACKED_TREND continuousVar FOR cases
                  | SCATTER_PLOT var AND var
                  | PATTERN var AND var
                  | BUBBLE var COMMA var COMMA var FOR cases ;

// Define the data, variables, and continuous variables
data               : var | continuousVar | var AT var ;
table              : IDENTIFIER ;
var                : IDENTIFIER ;
continuousVar      : IDENTIFIER (COMMA IDENTIFIER)* ;

loop               : WHILE LPAREN condition RPAREN COLON;

// Define ranges for continuous variables
range              : IDENTIFIER TO IDENTIFIER ;

// Rules for subgroups and cases (both are identifiers)
subgroup           : IDENTIFIER ;
cases              : IDENTIFIER ;


// Trend keyword for log graphs
trendKeyword       : PROGRESSION_OF | TREND_OF | GROWTH_OF ;

// Define conditions for logical operations
condition          : NOT? LPAREN? NOT* logicalOperation ((AND | OR) NOT? logicalOperation)* NOT? ;
logicalOperation  : LPAREN? operationBody RPAREN? logicalOperationSign LPAREN? operationBody RPAREN?;
operationBody      : LPAREN? operation RPAREN? (operationSign LPAREN? operation RPAREN?)* ;
operation          : IDENTIFIER (operationSign IDENTIFIER)? ;
operationSign      : PLUS | MINUS | MULTIPLY | DIVIDE ;
logicalOperationSign : LT | LTE | GT | GTE | EQ | NEQ ;
