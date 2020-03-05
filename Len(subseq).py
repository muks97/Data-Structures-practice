def longest_substring_without_repeats(string):
  seen = {}
  maximum_length = 0
  start = 0
  for end in range(len(string)):
    if string[end] in seen:
      start = max(start, seen[string[end]] + 1)
    seen[string[end]] = end
    print(seen[string[end]])
    maximum_length = max(maximum_length, end - start + 1)
    #print(seen)
    #print(start)
    #print(end)  
  return maximum_length

print(longest_substring_without_repeats('abcabcbb') == 3)
#print(longest_substring_without_repeats('bbbbb') == 1)
#print(longest_substring_without_repeats('pwwkew') == 3);

