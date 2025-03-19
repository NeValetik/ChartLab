```
<command> ::= <startProgram> "with" <data> "from" <table> "chart:" <chartFunction> <endProgram>
<startProgram> ::= "BEGIN"
<endProgram> ::= "END"
<chartFunction> ::= "compare" <var> "for" <cases>  
                 | "differences" <var> "for" <cases>  
                 | "contrast" <var> "for" <cases>  
                 | "versus" <var> "for" <cases>  
                 | "compare" <var> "split by" <subgroup> "for" <cases>  
                 | "compare" <var> "grouped by" <subgroup> "for" <cases>  
                 | "differences within" <subgroup> "for" <cases>  
                 | "show" <var> "stacked by" <subgroup> "for" <cases>  
                 | "show" <var> "subgroups" <subgroup> "for" <cases>  
                 | "show correlation between" <continuousVar> "and" <continuousVar>  
                 | "log" <trendKeyword> <continuousVar> "from" <range>  
                 | "show proportion of" <var> "by" <cases>  
                 | "show share of" <var> "by" <cases>  
                 | "show percentage of" <var> "by" <cases>  
                 | "show frequency of" <var> "by" <range>  
                 | "show distribution of" <var> "by" <range>  
                 | "show frequency in" <range> "buckets"  
                 | "accumulation of" <continuousVar> "for" <cases> "from" <range>  
                 | "stacked trend of" <continuousVar> "for" <cases>  
                 | "scatter plot of" <var> "and" <var>  
                 | "pattern of" <var> "and" <var>  
                 | "bubble of" <var> "," <var> "," <var> "for" <cases>

<table> ::= <identifier>

<data> ::= <var> | <continuousVar> | <var> "at" <var>

<var> ::= <identifier>

<continuousVar> ::= <identifier> | <identifier> "," <continuousVar>

<range> ::= <identifier> "to" <identifier>

<loop> ::= "while" "(" <condition> ")" ":"

<conditionalStatement> ::= "if" "(" <condition> ")" ":"

<condition> ::= <logicalOperation>
              | "!" <condition>
              | <condition> ("and" | "or") <condition>
              | "(" <condition> ")"

<logicalOperation> ::= <operationBody> <logicalOperationSign> <operationBody>

<operationBody> ::= <operation>
                  | "(" <operation> ")"
                  | <operationBody> <operationSign> <operationBody>

<operation> ::= <identifier> | <identifier> <operationSign> <identifier>

<operationSign> ::= "+" | "-" | "*" | "/"

<logicalOperationSign> ::= "<" | "<=" | ">" | ">=" | "==" | "!="

<subgroup> ::= <identifier>

<cases> ::= <identifier>

<identifier> ::= <letter> | <letter> <identifier> | <identifier> <digit>

<trendKeyword> ::= "progression of" | "trend of" | "growth of"

<letter> ::= "a"|"b"|...|"z"|"A"|"B"|...|"Z"

<digit> ::= "0" | "1" |...| "9"
```
