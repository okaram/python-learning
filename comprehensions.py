_1_to_10=list(range(1,11))
_10_to_20=list(range(10,21))

def is_odd(n:int)->int:
   return n%2==1

def is_even(n:int)->int:
   return n%2==0

[ i for i in _1_to_10]
[ 2*i for i in _1_to_10]
[ 2*i for i in _1_to_10 if is_even(i)]

[ 2*i+j for i in _1_to_10 if is_even(i) for j in _10_to_20 if is_odd(j)]

#dict
{i: 2*i for i in _10_to_20}

#set
{ i+j for i in _10_to_20 for j in _10_to_20}

# generator
(i+j for i in _10_to_20 for j in _10_to_20)

from dataclasses import dataclass
@dataclass

