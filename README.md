
SQL like syntax
```sql
Vn = {
	<table>, <query>, <chart>, <var>, <function>, <dataType<>>, <string>, <char>,
	<operationType<>>, <declaration>, <logicalOperand<>>, <chartType>, <row>,
	<column>, <int>, <float>, <assignment>, <list<>>, <value>, <global>, <with>, <keyword<>>, <and>
	// expandable  
}
Vt = {
	A..Z, a..z, 0..9, /, ", `, ', _, +, -, ;, {, }, [, ], !, %, (, ), #, =, ?, :, |, \, &, *,   
}
```


Example of syntax that might be:
```dsl
data = smth1, smth2, smth3 // where smth# is a column name

with data from table.extension chart:

	compare smth1 and smth2 //and ...

	log progression and total
```

Token Decomposition
```dsl 
<global>
<var> <operationType> <value<list<dataType>>> <chart> <endLine>
<with><var><from><table><begin>
	<keyword><value><and><value>
	<keyword><and><keyword>
<end>
<globalEnd>
```

%% COMMENTED OUT
```dsl
```
%%