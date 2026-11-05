class Solution:
    def buildArray(self, target: list[int], n: int) -> list[str]:
        # we simulate the whole push and pop operations by checking wether each element becomes equal to target[i] or not 
        
        target.sort()
        stream = [x for x in range(1,n + 1)]
        stack_operations = []
        for i in range(len(target)):
            top_element = stream[0]
            while target[i] != top_element:
                stream.pop(0)
                top_element = stream[0]
                stack_operations.append("Push")
                stack_operations.append("Pop")
            stream.pop(0)
            stack_operations.append("Push")

        return stack_operations

