
```
<command> ::= "with data from" <table> "chart:" <chartFunction> 
<chartFunction> ::= "compare" <var> "for" <cases> #HERE STARTS BAR CHART
                 | "differences" <var> "for" <cases> 
                 | "contrast" <var> "for" <cases> 
                 | "versus" <var> "for" <cases>
                
                 | "compare" <var> "split by" <subgroup> "for" <cases> #BAR CHART (GROUPED)
                 | "compare" <var> "grouped by" <subgroup> "for" <cases>
                 | "differences within" <subgroup> "for" <cases>
               
                 | "show" <var> "stacked by" <subgroup> "for" <cases> #BAR CHART (STACKED)
                 | "show" <var> "subgroups" <subgroup> "for" <cases>
               
                 | "show correlation between" <continuousVar> "and" <continuousVar>  # Line Graph (2 variables)
                 | "log" <trendKeyword> <continuousVar> "from" <range>  # Line Graph (Trend)
                 
                 | "show proportion of" <var> by <cases> #PIE CHART
                 | "show share of" <var> by <cases> 
                 | "show percentage of" <var> by <cases> 
                 
                 | "show frequency of" <var> "by" <range>  # HISTOGRAM
                 | "show distribution of" <var> "by" <range> 
                 | "show frequency in" <range> "buckets" 
                 
                 | "accumulation of" <continuousVar> "for" <cases> "from" <range>  # AREA CHART (Accumulation)
                 | "stacked trend of" <continuousVar> "for" <cases>  # AREA CHART (Stacked Trend)
                 
                 | "scatter plot of" <var> "and" <var>  #SCATTER PLOT
                 | "pattern of" <var> "and" <var> 
                 
                 | "bubble of" <var> "," <var> "," <var> "for" <cases>  # BUBBLE CHART

<table> ::= <identifier>
<var> ::= <identifier>
<continuousVar> ::= <identifier> | <identifier> "," <continuousVar>
<continuousCases ::= <identifier> | <identifier> "," <continuousVar>

<range> ::= <identifier> "to" <identifier>

<subgroup> ::= <identifier>
<cases> ::= <identifier>
<identifier> ::=  <letter> | <letter> <identifier> | <identifier> <digit>

<trendKeyword> ::= "progression of" | "trend of" | "growth of"

<letter> ::= a|b|...|z|A|B|...|Z
<digit> ::= 0|1|...|9
```
