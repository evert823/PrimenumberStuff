# PrimenumberStuff
factorfinder.py tests if a number is prime.

PrintTransPrimeList.py identifies lists of n n-digit primes, in which you can transpose the digits resulting into another list of n n-digit primes [(see here)](https://mathforums.com/threads/list-of-prime-numbers-and-after-transposing-all-digits-its-again-a-list-of-prime-numbers.360593/).

PrintNextPrime helps you find the first next prime number from an entered value.

Example:

```
PS C:\Users\Evert Jan\pythonprojects\primes> ..\pypy3.7-v7.3.5-win64\pypy3 PrintNextPrime.py
From what size do you want found factors to be displayed? --> 200
                                    ----+----0----+----0----+----0----+----0
Type your candidate number here --> 83645635241525364653
18/10/2021 20:50:10
8110087501 is a factor of 83645635241525364661
419 is a factor of 83645635241525364691
24709 is a factor of 83645635241525364697
33168497 is a factor of 83645635241525364701
307 is a factor of 83645635241525364719
409 is a factor of 83645635241525364727
83645635241525364739
18/10/2021 20:54:19
                                    ----+----0----+----0----+----0----+----0
Type your candidate number here -->
```


TransPrimeListBatch follows a faster method, suggested by [billymac00](https://mathforums.com/members/billymac00.1949/), for transposable n-digit prime lists.
Example:
```
PS C:\Users\Evert Jan\pythonprojects\primes> cat TransPrimeListBatchInput.txt
11
PS C:\Users\Evert Jan\pythonprojects\primes> cat TransPrimeListBatch.ps1
..\pypy3.7-v7.3.5-win64\pypy3 TransPrimeListBatch.py
PS C:\Users\Evert Jan\pythonprojects\primes> .\TransPrimeListBatch.ps1
19,51
19,79
19,111
19,139
19,147
Found one !!
36827624653
79523446741
23856965107
81894264047
51759205241
86567550449
29691486431
37639410019
52954900147
96064841179
93377373317
----
```
