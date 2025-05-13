class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        if len(s) == 0:
            return 0
        if len(s) == 1:
            return 1

        # We store character indices in char_index_map so that we know where the last occurrence of a character was.
        # This is essential for efficiently updating the left boundary of the sliding window when a duplicate character
        # is found.
        sliding_window_map: dict[str, int] = {}
        max_length: int = 0

        for index, character in enumerate(s):
            if character in sliding_window_map:
                sliding_window_map = {}
                max_length = 0
                max_length += 1
            else:
                sliding_window_map[character] = index
                max_length += 1
        return max_length
