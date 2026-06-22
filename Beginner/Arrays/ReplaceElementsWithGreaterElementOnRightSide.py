class Solution:
    def replaceElements(self, arr: List[int]) -> List[int]:
        length = len(arr)
        max_val = 0
        for i in range(length - 1):
            for j in range(i + 1, length):
                max_val = max(arr[j], max_val)
            arr[i] = max_val
            max_val = 0
        arr[length - 1] = -1

        return arr