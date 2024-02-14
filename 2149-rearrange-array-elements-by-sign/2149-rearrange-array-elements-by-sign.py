class Solution:
    def rearrangeArray(self, nums: List[int]) -> List[int]:
        posQueue = []
        negQueue = []
        ans = []
        for i in nums:
            if i < 0:
                if ans == [] or ans[-1] < 0:
                    negQueue.append(i)
                else:
                    if negQueue == []:
                        ans.append(i)
                    else:
                        ans.append(negQueue.pop(0))
                        negQueue.append(i)
            else:
                if ans == [] or ans[-1] < 0:
                    if posQueue == []:
                        ans.append(i)
                    else:
                        ans.append(posQueue.pop(0))
                        posQueue.append(i)
                else:
                    posQueue.append(i)
        if nums == []:
            return []
        elif ans == [] or ans[-1] < 0:
            for k in range(len(negQueue)):
                ans.append(posQueue.pop(0))
                ans.append(negQueue.pop(0))
        else:
            for k in range(min(len(negQueue), len(posQueue))):
                ans.append(negQueue.pop(0))
                ans.append(posQueue.pop(0))
            ans.append(negQueue.pop(0))
        return ans