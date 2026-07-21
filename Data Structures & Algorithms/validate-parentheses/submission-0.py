class Solution:
    def isValid(self, s: str) -> bool:

        stack = []

        mapping = {
            ')' : '(',
            '}' : '{',
            ']' : '['
        }

        for ch in s:

            # Opening bracket
            if ch in "({[":
                stack.append(ch)

            # Closing bracket
            else:
                # No matching opening bracket
                if not stack:
                    return False

                # Top doesn't match
                if stack[-1] != mapping[ch]:
                    return False

                stack.pop()

        return len(stack) == 0     