class Solution:
    def findKthLargest(self, nums, k):
        k_index = len(nums) - k

        def partition(nums, left, right):
            pivot = nums[right]
            i = left
            for j in range(left, right):
                if nums[j] <= pivot:
                    nums[i], nums[j] = nums[j], nums[i]
                    i += 1
            nums[i], nums[right] = nums[right], nums[i]
            return i

        def quickselect(nums, left, right, k_index):
            if left == right:
                return nums[left]

            pivot_index = partition(nums, left, right)

            if pivot_index == k_index:
                return nums[pivot_index]
            elif pivot_index < k_index:
                return quickselect(nums, pivot_index + 1, right, k_index)
            else:
                return quickselect(nums, left, pivot_index - 1, k_index)

        return quickselect(nums, 0, len(nums) - 1, k_index)