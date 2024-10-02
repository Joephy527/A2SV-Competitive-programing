class Solution:
  def maxProduct(self, words: List[str]) -> int:
    maxLen = 0

    def helper(word):
      b = 0

      for c in word:
        b |= 1 << ord(c) - ord("a")
      
      return b

    masks = [helper(word) for word in words]

    for i in range(len(words)):
      for j in range(i):
        if not (masks[i] & masks[j]):
          maxLen = max(maxLen, len(words[i]) * len(words[j]))

    return maxLen
