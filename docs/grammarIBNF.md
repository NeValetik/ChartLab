
```
<program> ::= <statement>+ EOF

<statement> ::= <loop> | <command>

<loop> ::= "while" "(" <condition> ")" ":"

<command> ::= "with" <data> "from" <table> "chart:" <chartFunction> [ <block> ]

<block> ::= "{" <statement>+ "}"

<chartFunction> ::=
    "compare" <var> "for" <cases> |
    "differences" <var> "for" <cases> |
    "contrast" <var> "for" <cases> |
    "versus" <var> "for" <cases> |

    "compare" <var> "split by" <subgroup> "for" <cases> |
    "compare" <var> "grouped by" <subgroup> "for" <cases> |
    "differences within" <subgroup> "for" <cases> |

    "show" <var> "stacked by" <subgroup> "for" <cases> |
    "show" <var> "subgroups" <subgroup> "for" <cases> |

    "show correlation between" <continuousVar> "and" <continuousVar> |
    "log" <trendKeyword> <continuousVar> "from" <range> |

    "show proportion of" <var> "by" <cases> |
    "show share of" <var> "by" <cases> |
    "show percentage of" <var> "by" <cases> |

    "show frequency of" <var> [ "step" <value> ] |
    "show distribution of" <var> [ "step" <value> ] |
    "show frequency in" <var> "buckets" |

    "accumulation of" <continuousVar> "for" <cases> "from" <var> |
    "stacked trend of" <continuousVar> "for" <cases> "from" <var> |

    "scatter plot of" <var> "and" <var> |
    "pattern of" <var> "and" <var> |

    "bubble of" <var> "," <var> "," <var> "for" <cases>

<data> ::= <var> | <continuousVar> | <var> "at" <var>

<table> ::= <identifier>
<var> ::= <identifier>
<continuousVar> ::= <identifier> | <identifier> "," <continuousVar>
<range> ::= <identifier> "to" <identifier>
<subgroup> ::= <identifier>
<cases> ::= <identifier>
<value> ::= <identifier> | <number>

<trendKeyword> ::= "progression of" | "trend of" | "growth of"

<condition> ::= [ "!" ] [ "(" ] { "!" } <logicalOperation> { ("and" | "or") [ "!" ] <logicalOperation> } [ ")" ]

<logicalOperation> ::= [ "(" ] <operationBody> [ ")" ] <logicalOperationSign> [ "(" ] <operationBody> [ ")" ]

<operationBody> ::= [ "(" ] <operation> [ ")" ] { <operationSign> [ "(" ] <operation> [ ")" ] }

<operation> ::= <identifier> [ <operationSign> <identifier> ]

<operationSign> ::= "+" | "-" | "*" | "/"
<logicalOperationSign> ::= "<" | "<=" | ">" | ">=" | "==" | "!="

<identifier> ::= <letter> { <letter> | <digit> }
<number> ::= { <digit> } [ "." { <digit> } ]
<letter> ::= "a" | "b" | ... | "z" | "A" | "B" | ... | "Z"
<digit> ::= "0" | "1" | ... | "9"
```
