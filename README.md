# Decode Problem

Problem belonging to the post-classroom Mock Interview Question Repository.

## Problem Statement

We are interested in determining the number of ways we can interpret a secret message provided to us as a numerical code.

Our function will be given a string where each character is a digit.
For example:

code = "12106"

We assume that any message is encoded using the same mapping:
'A': 1
'B': 2
'C': 3
...
'Z': 26

We can see that is possible to translate the above code into 'LJF' where the code is separated into 12 (L), 10 (J), and 6 (F). Alternatively, we could translate the code into 'ABJF' where the code is separated in 1 (A), 2 (B), 10 (J), and 6 (F). Therefore, are function should return 2 as the number of ways we could interpret the given code.

Write a function that takes a code and returns the number of ways it can be decoded.

You are guaranteed that all characters in the code will be numeric.

Inspired by: https://leetcode.com/problems/decode-ways/

## Examples

### Example 1

```py
decode("12106")
```

Produces

```py
2
```

### Example 2

```py
decode("339")
```

Produces

```py
1
```

### Example 3

```py
decode("306")
```

Produces

```py
0
```

## Notes for the Interviewer

### Clarifying Questions

#### Q: Can zeros preceding another digit be interpreted as a single digit, for example 01 as 1?

A: No.

#### Q: What should I do if invalid input is passed in?

A: Assume all input is valid.

#### Q: What should I do if the code can't be decoded?

A: Return 0.

### Hints

- If your candidate struggles with an initial algorithm, encourage them to walk through an example and describe how they would do it using only pen and paper

- Another hint is that this problem can be solved using dynamic programming. Encourage them to look for the overlapping subproblem. To solve this problem, you must consider the solution to each of the substrings, i.e., for `"123"`, consider `"1"`, `"2"`, `"3"`, `"12"`, and `"23"`. Notice that the substrings overlap.

- If your candidate struggles with the edge case where the first two digits make up a number greater than 26, give a hint that their memo can hold an extra space

## Optional Bonus At-Home Challenges

To be attempted after completing the interview.

- What is the time/space complexity of sample solution?

- If you solved this problem recursively, try a dynamic programming approach. If you solved this problem using dynamic programming, try a recursive approach.
