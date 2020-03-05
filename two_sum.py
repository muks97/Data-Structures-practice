def permute(nums):
  if nums == []:
    return [[]]
  permutations = []
  for idx,num in enumerate(nums):
    other_permutations = permute(nums[:idx] + nums[idx + 1:])
    #print(nums[:idx]+nums[idx+1:])
    permutations += map(lambda permutation: [num] + permutation, other_permutations)
  return permutations

print(permute([1, 2, 3]))