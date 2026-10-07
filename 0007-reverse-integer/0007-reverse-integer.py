class Solution:
    def reverse(self, x: int) -> int:

        # Store the sign of the number
        sign = -1 if x < 0 else 1

        # Work with the positive value
        x = abs(x)

        # Variable to store the reversed number
        rev = 0

        while x > 0:

            # Get the last digit
            digit = x % 10

            # Add the digit to the reversed number
            rev = rev * 10 + digit

            # Remove the last digit from x
            x = x // 10

        # Put the original sign back
        rev = rev * sign

        # 32-bit signed integer range:
        # -2147483648 to 2147483647
        if rev < -2**31 or rev > 2**31 - 1:
            return 0

        return rev