import difflib
import pprint


class Solution(object):
    def reverseString(self, s):
        """
        :type s: List[str]
        :rtype: None
        """
        i = 0
        j = len(s) - 1
        while i <= j:
            s[i], s[j] = s[j], s[i]
            i += 1
            j -= 1


def build_diff(actual, expected):
    actual_lines = pprint.pformat(actual).splitlines()
    expected_lines = pprint.pformat(expected).splitlines()
    return "\n".join(
        difflib.unified_diff(
            expected_lines,
            actual_lines,
            fromfile="expected",
            tofile="actual",
            lineterm="",
        )
    )


if __name__ == "__main__":
    sol = Solution()
    samples = [
        (["h", "e", "l", "l", "o"], ["o", "l", "l", "e", "h"]),
        (["H", "a", "n", "n", "a", "h"], ["h", "a", "n", "n", "a", "H"]),
    ]

    for sample_input, expected in samples:
        chars = sample_input[:]
        sol.reverseString(chars)
        matches_expected = chars == expected
        print("Input:", sample_input)
        print("Actual:", chars)
        print("Expected:", expected)
        print("Matches expected:", matches_expected)
        if not matches_expected:
            print("Diff:")
            print(build_diff(chars, expected))
        print()
