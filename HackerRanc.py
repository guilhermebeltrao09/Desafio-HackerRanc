#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'repeatedString' function below.
#
# The function is expected to return a LONG_INTEGER.
# The function accepts following parameters:
#  1. STRING s
#  2. LONG_INTEGER n
#

def repeatedString(s, n):
    
    quantidade = s.count("a")
    
    repeticoes = int(n/len(s))
    
    quantidade = quantidade*repeticoes
    
    analisado = repeticoes*len(s)
    
    nao_analisado = n-analisado
    
    if (nao_analisado != 0):
        sobra = 0
        contador = 0
        
        while contador < nao_analisado:
            if s[contador] == "a":
                sobra += 1
                contador += 1
            else:
                contador += 1
                pass
        
        quantidade = quantidade+sobra
    
    return quantidade

if _name_ == '_main_':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    s = input()

    n = int(input().strip())

    result = repeatedString(s, n)

    fptr.write(str(result) + '\n')

    fptr.close()
