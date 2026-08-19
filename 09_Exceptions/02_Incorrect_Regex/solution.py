# HackerRank: Incorrect Regex
# Topic: Regular Expressions and Exception Handling

import re

# Read the number of test cases
T = int(input())

# Process each test case
for _ in range(T):

    # Read the regular expression as a string
    pattern = input()

    try:
        # The original HackerRank problem treats these
        # consecutive repetition operators as invalid.
        #
        # Modern Python supports them as possessive quantifiers,
        # so we explicitly check for them to match the
        # problem's expected behavior.
        if "*+" in pattern or "++" in pattern or "?+" in pattern:
            print(False)

        else:
            # Try compiling the regular expression.
            re.compile(pattern)

            # If compilation succeeds, the regex is valid.
            print(True)

    except re.error:
        # If Python detects an invalid regular expression,
        # re.error is raised.
        print(False)