Python 3.14.4 (tags/v3.14.4:23116f9, Apr  7 2026, 14:10:54) [MSC v.1944 64 bit (AMD64)] on win32
Enter "help" below or click "Help" above for more information.
a = 190
float(a)
190.0
dict(a)
Traceback (most recent call last):
  File "<pyshell#2>", line 1, in <module>
    dict(a)
TypeError: 'int' object is not iterable
complex(a)
(190+0j)
tuple(a)
Traceback (most recent call last):
  File "<pyshell#5>", line 1, in <module>
    tuple(a)
TypeError: 'int' object is not iterable
set(a)
Traceback (most recent call last):
  File "<pyshell#6>", line 1, in <module>
    set(a)
TypeError: 'int' object is not iterable
list(a)
Traceback (most recent call last):
  File "<pyshell#7>", line 1, in <module>
    list(a)
TypeError: 'int' object is not iterable
b = 3+1j
int(b)
Traceback (most recent call last):
  File "<pyshell#9>", line 1, in <module>
    int(b)
TypeError: int() argument must be a string, a bytes-like object or a real number, not 'complex'
str(b)
'(3+1j)'
str(a)
'190'
set(b)
Traceback (most recent call last):
  File "<pyshell#12>", line 1, in <module>
    set(b)
TypeError: 'complex' object is not iterable
tuple(b)
Traceback (most recent call last):
  File "<pyshell#13>", line 1, in <module>
    tuple(b)
TypeError: 'complex' object is not iterable
dict(b)
Traceback (most recent call last):
  File "<pyshell#14>", line 1, in <module>
    dict(b)
TypeError: 'complex' object is not iterable
bool(a)
True
bool(b)
True
c = 'python'
int(c)
Traceback (most recent call last):
  File "<pyshell#18>", line 1, in <module>
    int(c)
ValueError: invalid literal for int() with base 10: 'python'
bool(c)
True
set(c)
{'n', 'o', 'p', 't', 'h', 'y'}
tuple(c)
('p', 'y', 't', 'h', 'o', 'n')
dict(c)
Traceback (most recent call last):
  File "<pyshell#22>", line 1, in <module>
    dict(c)
ValueError: dictionary update sequence element #0 has length 1; 2 is required

d = "10"
int(d)
10
float(d)
10.0
list()
[]
list(c)
['p', 'y', 't', 'h', 'o', 'n']
list(d)
['1', '0']
set(d)
{'0', '1'}
complex(c)
Traceback (most recent call last):
  File "<pyshell#30>", line 1, in <module>
    complex(c)
ValueError: complex() arg is a malformed string
complex(d)
(10+0j)
l = (1, 2, 3)
str(l)
'(1, 2, 3)'
tuple(l)
(1, 2, 3)
set(l)
{1, 2, 3}
bool(l)
True
int(l)
Traceback (most recent call last):
  File "<pyshell#37>", line 1, in <module>
    int(l)
TypeError: int() argument must be a string, a bytes-like object or a real number, not 'tuple'

t = [1, 2, 3]
type(t)
<class 'list'>
type(l)
<class 'tuple'>
bool(t)
True
set(t)
{1, 2, 3}
dict(t)
Traceback (most recent call last):
  File "<pyshell#44>", line 1, in <module>
    dict(t)
TypeError: object is not iterable
Cannot convert dictionary update sequence element #0 to a sequence
s = {6, 7, 8, 9}
float(s)
Traceback (most recent call last):
  File "<pyshell#46>", line 1, in <module>
    float(s)
TypeError: float() argument must be a string or a real number, not 'set'
list(s)
[8, 9, 6, 7]
set(s)
{8, 9, 6, 7}
tuple(s)
(8, 9, 6, 7)
dict(s)
Traceback (most recent call last):
  File "<pyshell#50>", line 1, in <module>
    dict(s)
TypeError: object is not iterable
Cannot convert dictionary update sequence element #0 to a sequence
d = {1:1, 2:3, 4:5}
int(d)
Traceback (most recent call last):
  File "<pyshell#52>", line 1, in <module>
    int(d)
TypeError: int() argument must be a string, a bytes-like object or a real number, not 'dict'
tuple(d)
(1, 2, 4)
list(d)
[1, 2, 4]
set(d)
{1, 2, 4}
str(d)
'{1: 1, 2: 3, 4: 5}'
bool(s)
True
str(s)
'{8, 9, 6, 7}'
complex(s)
Traceback (most recent call last):
  File "<pyshell#59>", line 1, in <module>
    complex(s)
TypeError: complex() argument must be a string or a number, not set
m = True
int(m)
1
float(m)
1.0
complex(m)
(1+0j)
str(m)
'True'
set(m)
Traceback (most recent call last):
  File "<pyshell#65>", line 1, in <module>
    set(m)
TypeError: 'bool' object is not iterable
tuple(s)
(8, 9, 6, 7)
tuple(m)
Traceback (most recent call last):
  File "<pyshell#67>", line 1, in <module>
    tuple(m)
TypeError: 'bool' object is not iterable
bool(m)
True
bool(s)
True




a = 10
b = 10.2
c = 'python'
print(a, b, c)
10 10.2 python
print('a =',a , 'b =',b , 'c=',c)
a = 10 b = 10.2 c= python
print('a =',a , 'b =',b , 'c=',c, ' ')
a = 10 b = 10.2 c= python  
print('a =',a , 'b =',b , 'c=',c, sep =' ')
a = 10 b = 10.2 c= python
print('a =',a , 'b =',b , 'c=',c, sep ='\n')
a =
10
b =
10.2
c=
python
>>> print('a =',a , 'b =',b , 'c=',c, sep = ' ')
a = 10 b = 10.2 c= python
>>> print('a=',a , 'b=',b , 'c=',c, sep = ' ')
a= 10 b= 10.2 c= python
>>> KeyboardInterrupt
>>> print('a=',a , 'b=',b , 'c=',c, sep=' ')
a= 10 b= 10.2 c= python
>>> print('a=',a,'b=',b,'c=',c,sep=' ')
a= 10 b= 10.2 c= python
>>> print('a=',a , 'b=',b , 'c=',c , sep='\t', end = '\n\n')
a=	10	b=	10.2	c=	python

>>> print('a=',a , 'b=',b , 'c=',c , sep='\t', end = '\n')
a=	10	b=	10.2	c=	python
>>> print('a=',a , 'b=',b , 'c=',c , sep='\t', end = '\n')
a=	10	b=	10.2	c=	python
>>> print(f'a: {a}, b: {b}, c: {c}')
a: 10, b: 10.2, c: python
>>> print('a = %a b = %f c = %s' % (a, b, c))
a = 10 b = 10.200000 c = python
>>> print('a = %a b = %.2f c = %s' % (a, b, c))
... 
a = 10 b = 10.20 c = python
>>> print('a = {} b ={} c = {}'.(a, b, c))
SyntaxError: invalid syntax
>>> print('a = {} b ={} c = {}'.format(a, b, c))
a = 10 b =10.2 c = python
>>> print('a = {1} b ={0} c = {2}'.format(a, b, c))
a = 10.2 b =10 c = python
