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

        for i in range(rows):
            if target==matrix[i][columns-1]:
                print(matrix[i][0])
                return True
            elif target<matrix[i][columns-1]:
                answer = search(matrix[i], target)
                return answer
            elif target>matrix[i][columns-1]:
                continue
            
        return False

            
            
