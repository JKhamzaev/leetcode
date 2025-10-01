class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        rows = len(matrix)
        columns = len(matrix[0])
        answer = False

        def search(arr: List[int], target: int) -> int:
            left = 0
            right = len(arr) - 1
    
            while left<=right:
                i = (left + right)//2
                if target == arr[i]:
                    return True
                elif target < arr[i]:
                    right = i - 1
                elif target > arr[i]:
                    left = i + 1
            
            return False

        l = 0
        r = rows-1

        while l<=r:
            i = (l + r)//2
            if matrix[i][0]<=target<=matrix[i][columns-1]:
                answer = search(matrix[i], target)
                return answer
            elif target < matrix[i][0]:
                r = i - 1
            elif target > matrix[i][columns-1]:
                l = i + 1
        
        return False

            
            
