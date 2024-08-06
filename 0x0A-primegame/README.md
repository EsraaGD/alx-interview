Maria and Ben are playing a game. Given a set of consecutive integers starting from 1 up to and including n, they take turns choosing a prime number from the set and removing that number and its multiples from the set. The player that cannot make a move loses the game.

They play <code>x</code> rounds of the game, where n may be different for each round. Assuming Maria always goes first and both players play optimally, determine who the winner of each game is.

 - Prototype: <code>def isWinner(x, nums)</code>
 - where <code>x</code> is the number of rounds and <code>nums</code> is an array of <code>n</code>
 - Return: name of the player that won the most rounds
 - If the winner cannot be determined, return <code>None</code>
 - You can assume <code>n</code> and <code>x</code> will not be larger than 10000
 - You cannot import any packages in this task

Example:

 - <code>x = 3, nums = [4, 5, 1]</code>

First round: <code>4</code>

 - Maria picks 2 and removes 2, 4, leaving 1, 3
 - Ben picks 3 and removes 3, leaving 1
 - Ben wins because there are no prime numbers left for Maria to choose

Second round: <code>5</code>

 - Maria picks 2 and removes 2, 4, leaving 1, 3, 5
 - Ben picks 3 and removes 3, leaving 1, 5
 - Maria picks 5 and removes 5, leaving 1
 - Maria wins because there are no prime numbers left for Ben to choose

Third round: <code>1</code>

 - Ben wins because there are no prime numbers for Maria to choose

Result: Ben has the most wins