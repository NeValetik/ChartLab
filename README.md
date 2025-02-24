
SQL like syntax
```sql
Vn = {
	<table>, <query>, <chart>, <var>, <function>, <dataType>, <string>, <char>,
	<operationType>, <declaration>, <logicalOperand>, <chartType>, <row>,
	<column>, <int>, <float>,
	// expandable  
}
Vt = {
	A..Z, a..z, 0..9, /, ", `, ', _, +, -, ;, {, }, [, ], !, %, (, ), #, =, ?, :,  
}
```


Example of syntax that might be:
```dsl
var chart1 = get *.csv{
	cols [0..9] | none ; // or colls by names
	rows 100 | [20..100] | max | none ;
};
var options = {
	lenX: alot;
	lenY: 100.1;
};
chart1("pie",{...options}).out("html");
```

%% COMMENTED OUT
```dsl
get *.csv{
	(cols [0..9]) | epsilon // or colls names
	(rows 100 | [20..100] | max) | epsilon
} 
```
%%