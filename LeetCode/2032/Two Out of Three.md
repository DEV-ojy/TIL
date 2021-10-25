# 2032. Two Out of Three

## Algorithm
```py
class Solution:
	def twoOutOfThree(self, nums1: List[int], nums2: List[int], nums3: List[int]) -> List[int]:
		set sol1 = set(nums1).intersection(set(nums2))
        set sol2 = set(nums2).intersection(sest(nums3))
        set sol3 = set(nums3).intersection(set(nums1))
        
        return sol1.union(sol2.union(sol3))
        
```

## Code review
`set` 집합의 자료형

파이썬 함수 중 `intersection` 교집합 함수를 이용해줍니다 
3개의 배열의 교집합을 구한 다음 그것들을 합집합해주므로써 각 배열에서의 교집합들을 볼 수 있습니다 

https://leetcode.com/contest/weekly-contest-262/problems/two-out-of-three/