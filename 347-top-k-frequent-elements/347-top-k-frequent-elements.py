class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        
        items = set(nums)
        cnt_dict = {}
        results = []
        
        for i in items:
            cnt_dict[i] = nums.count(i)
        
        sorted_cnt = sorted(cnt_dict.items(), key=(lambda item: item[1]), reverse = True)[:k]
        
        for idx, value in enumerate(sorted_cnt):
            
            results.append(value[0])
        
        return results