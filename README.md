# Data Structures and Algorithms

This repository is my working collection of solutions to data-structure and
algorithm problems. I use it to practise problem solving, compare approaches,
and keep a record of the patterns that come up in technical interviews.

The solutions are written in Java and Python. Each solution is intended to be
small enough to read easily, but complete enough to explain why the approach
works and where it may be useful.

## Repository layout

```text
data-structures-and-algorithms/
├── README.md
├── LICENSE
├── .gitignore
├── .github/
│   └── workflows/
│       └── ci.yml
├── java/
│   ├── build.gradle
│   ├── settings.gradle
│   └── src/
│       ├── main/java/com/leetcode/algorithms/
│       │   ├── arrays/
│       │   ├── dynamicprogramming/
│       │   ├── graphs/
│       │   ├── linkedlist/
│       │   ├── queue/
│       │   ├── sorting/
│       │   ├── stack/
│       │   ├── strings/
│       │   └── trees/
│       └── test/java/com/leetcode/algorithms/
└── python/
    ├── src/leetcode/algorithms/
    │   ├── arrays/
    │   ├── dynamic_programming/
    │   ├── graphs/
    │   ├── linkedlist/
    │   ├── queue/
    │   ├── sorting/
    │   ├── stack/
    │   ├── strings/
    │   └── trees/
    └── tests/
```

Problems are grouped by topic, including arrays, strings, linked lists, stacks,
queues, trees, graphs, sorting, and dynamic programming. The Java and Python
implementations use separate source roots. The Java project uses Gradle, and
its tests run in GitHub Actions on every push to `main` and every pull request.

## Current solution layout

The current Java solution is grouped under the `strings` topic:

```text
java/src/main/java/com/leetcode/algorithms/strings/
└── Palindrome.java

java/src/test/java/com/leetcode/algorithms/strings/
└── PalindromeTest.java
```

The `leetcode` directories and the Python source directories are present for
future solutions but do not contain implementations yet. New Java solutions
should be placed under the topic package that best describes the problem, with
corresponding tests under the matching test package.

The root `.gitignore` excludes editor settings, operating-system metadata,
build output, caches, virtual environments, and other generated files from
version control.

## Test coverage

`PalindromeTest` currently covers:

- palindromes containing spaces, punctuation, and mixed letter case;
- non-palindrome input;
- empty strings and input containing only non-alphanumeric characters;
- `null` input.

Run the Java test suite from the repository root with:

```bash
gradle -p java test
```

## What each solution includes

Where appropriate, a problem includes:

- a link to the original problem statement;
- a short explanation of the approach;
- time and space complexity;
- tests for normal cases and important edge cases.

The code is written for clarity first. When two approaches are both useful, I
prefer to keep the straightforward version visible and explain the trade-off
of a more optimized version.

## Running the Java tests

From the repository root, run:

```bash
gradle -p java test
```

The CI workflow runs the same command using Java 17 and Gradle 8.10. A Gradle
wrapper can be added later so contributors do not need a system Gradle
installation.

## Code quality

I aim to keep the implementations consistent and maintainable by using:

- descriptive names and small, focused methods;
- standard Java and Python formatting conventions;
- explicit complexity analysis;
- automated tests for behaviour that matters;
- continuous integration checks for Java changes;
- incremental commits that describe one meaningful change.

## Attribution

The solutions in this repository are my own implementations unless a file or
directory says otherwise. If I use an idea, implementation, or explanation
from another source, I will identify the source and retain its applicable
license and attribution.

## License

This project is licensed under the terms in [LICENSE](LICENSE).
