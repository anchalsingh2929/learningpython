class Solution(object):
    def heightChecker(self, heights):
        count = 0
        new_list = heights.copy()
        new_list.sort()
        print(heights,new_list)
        for x,y in enumerate(new_list):
            print(x,y)
            if y != heights[x]:
                count += 1
        print(new_list)
        return count
height=Solution()
     
print(height.heightChecker([1,7,2,3,4,9,5,6]))
#expected = [1,2,3,4,5,6,7,9]