class Solution:
    def is_palindrome(self, x: int) -> bool:
        """
        Determine whether an integer is a palindrome.

        :param x: The integer to check for palindrome property.
        :type x: int
        :return: True if `x` is a palindrome, False otherwise.
        :rtype: bool
        """
        return str(x) == str(x)[::-1]
