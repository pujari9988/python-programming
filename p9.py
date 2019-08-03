Python 3.7.3 (v3.7.3:ef4ec6ed12, Mar 25 2019, 21:26:53) [MSC v.1916 32 bit (Intel)] on win32
Type "help", "copyright", "credits" or "license()" for more information.
>>> l=[1,2,3,4,5,6]
>>> 1
1
>>> l
[1, 2, 3, 4, 5, 6]
>>> for i in l:
	if(i%2)==0:
		print i,"is even"
		
SyntaxError: Missing parentheses in call to 'print'. Did you mean print(i,"is even")?
>>> else
SyntaxError: invalid syntax
>>> for i in l:
	if(i%2)==0:
		print i,"is even."
		
SyntaxError: Missing parentheses in call to 'print'. Did you mean print(i,"is even.")?
>>> for i in l:
	if(i%2)==0:
		print(i,"is Even")
		else
		
SyntaxError: invalid syntax
>>> 
