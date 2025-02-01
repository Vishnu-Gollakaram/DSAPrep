class Solution:
    def isArraySpecial(self, nums: List[int]) -> bool:
        # Variables to be used later
        size_of_nums = len(nums)
        previous_element_parity = nums[0] & 1

        # Idea is to check for parity equality across array
        # Parity is just seeing if element is even or odd
        # Dividing into 2 element running stream
        # Compare Element 0 with element 1, then 1 with 2 and so on
        # If any 2 elements have same parity (previous_element_parity == current_element_parity) return False
        # If no matching parity found, nums is special array. So, return True
        for index in range(1, size_of_nums):
            current_element_parity = nums[index] & 1 # Famous syntax is n % 2 to check even or odd, but this is more time efficient as single bit comparision.

            if previous_element_parity == current_element_parity:
                return False
            previous_element_parity = current_element_parity

        return True