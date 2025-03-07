
## In our DSL:
* Keywords - special reserved words with fixed meanings in the language
  * "data" (declares variables)
  * "with data from" (declares the table)
  * "chart" (signals chart creation)
  * "compare", "log", etc. (specific keywords for each chart type)

Example:
```
data = sales, revenue;   // "data" is a keyword
with data from finance chart:  // "with data from" is a keyword
    compare sales and revenue; // "compare" is a keyword
```

* Operators - symbols that perform operations on values.
Includes arithmetic (+, -), logical (and, or), assignment (=), and possibly others.

  * "=" (assignment operator)
  * "," (comma for lists)
  * "and" (logical operator for multiple comparisons)
  * "*,/"

Example:
```
data = sales, revenue; // "=" assigns values
compare sales and revenue; // "and" connects values

```

* Identifiers - user-defined names for variables, tables, etc.
Must start with a letter and can contain letters, numbers, underscores.
  * sales, revenue, finance (column & table names)

```
data = sales, revenue;  // "sales" and "revenue" are identifiers
with data from finance chart:  // "finance" is an identifier
```

# Example Chart Definitions
## Bar Chart
Use case: Compares a single variable across multiple cases.
* Keywords: "compare", "differences", "contrast", "versus"

```
with data from employees chart:
    compare salary for employee1 and employee2 and employee3;
```
Also, 
``` 
"compare X for A and B", "differences in X", "contrast A vs B"
```



## Bar Chart (Grouped/Split)
Use case: Compares a variable split into subsets, across various cases (for
example salary for both men and women in x companies). It contrasts subsets within and across individual cases, not useful
for comparing total values for cases.
* Keywords: "compare" in combination with "split by", "grouped by"; "differences within X"

```
with data from industry chart:
    compare salary split by gender for technology, finance, and healthcare
```

## Bar Chart (Stacked)
Use case: Compares the value of one variable split into 2 or more subsets, across various cases.
Best for comparing TOTALS across cases and subsets within cases.
* Keywords: "stacked by", "split by", "subgroups", "composition of"

```
with data from complaints chart:
    show harassment complaints stacked by region for healthcare, finance, and retail

```

## Line Graph
Use case: Compares continuous variables for one or more cases.
Keywords: "log", "trend of", "progression of", "growth of", "show correlation between X and Y", "relationship between X and Y for A, B"
```
with data from sales chart:
    log progression of revenue from 2019 to 2024;
```
```
with data from experiment chart:
    show correlation between temperature and viscosity for oil and water
```

## Pie Chart
Use case: Shows the proportion of a single variable for multiple cases (when you compare one segment to a whole)
* Keywords: "proportion of", "share of", "percentage of"
```
with data from market chart:
    show proportion of market share by company
```


## Histogram
Use case: Compares two variables, with one segmented into ranges that function like the cases in a bar graph(service 
workers - continuous variable - whose salary is 0-5000, 5001-10000, etc.). Best for comparing segments within continuous data sets.
* Keywords: "frequency", "range", "buckets", "distribution"
```
with data from salary chart:
    show frequency of employees by salary range
```

## Area Chart
Use Case: Compares 2 continuous variables for one or more cases
* Keywords: "accumulation", "stacked trend", "growth contribution of"
```
with data from market chart:
    accumulation of revenue for productA and productB from 2010 to 2024
```
```
with data from research chart:
    stacked trend of population growth in Europe, Asia, and Africa;
```


## Scatterplot
Use Case: Compares 2 variables at multiple data points for a single case. Best for showing distribution of data, when there is no clear trends, or when focus is on outlying data points.
* Keywords: "relationship", "correlation", "pattern", "scatter"
```
with data from research chart:
    find relationship between hours studied and exam score
```

## Bubble Chart
Use Case: Compares 3 variables at multiple data points for a single case. It emphasizes
the relationship between the third variable(the bubbles) and the first two
* Keywords: "impact of", "size represents", "3D relationship", "relationship of three variables", "bubble of"
```
with data from economy chart:
    bubble of GDP, life expectancy, and population for all countries;
```

Token Decomposition
```dsl 
<global>
<var> <operationType> <value<list<dataType>>> <endLine>
with<var>from<table> <chart> <begin>
	<keyword><value> and <value>
	<keyword>and<keyword>
<end>
<globalEnd>
```
```
<query> ::= "with data from" <table> ":" <chartFunction>;

<chartFunction> ::= "compare" <var> ("and" <var>)+ | <expression>

<var> ::= [a-zA-Z_][a-zA-Z0-9_]*

<table> ::= [a-zA-Z_][a-zA-Z0-9_]*

<expression> ::= <var> ("+" | "-" | "*" | "/") <var>
```