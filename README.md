# Loose-Change-Problem

## Introduction
Repo for implementation of the loose change problem.

Given an input of coin change required, return the minimal amount coins required to meet that amount.

E.g. £0.93 would return 50p, 20p (x2), 2p, 1p

## Pseudo code and thoughts
### Initial thoughts
- Use of ordered list containing all the coin denominations
- Loop from highest to lowest, and compare if value is higher than remaining change
- Use a dictionary to store the combination of values

### Pseudo Code
```
coins = [2,1,0.5,0.2,0.1,0.05,0.02,0.01]
denomination = ["£2","£1","50p","20p","10p","5p","2p","1p"]
finalDict = {}
change = 0.93

for i in len(coins):
    temp = change div coins(i)
    if temp > 0:
        add denomination and amount to dictionary
        remove amount of money from the change amount
    if change == 0
        print finalDict

```