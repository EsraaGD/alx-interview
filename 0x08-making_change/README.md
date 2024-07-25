Given a pile of coins of different values, determine the fewest number of coins needed to meet a given amount total.

- Prototype: <code>def makeChange(coins, total)</code>
- Return: fewest number of coins needed to meet <code>total</code>
  - If <code>total</code> is <code>0</code> or less, return <code>0</code>
  - If <code>total</code> cannot be met by any number of coins you have, return <code>-1</code>
- <code>coins</code> is a list of the values of the coins in your possession
- The value of a coin will always be an integer greater than <code>0</code>
- You can assume you have an infinite number of each denomination of coin in the list
- Your solution’s runtime will be evaluated in this task