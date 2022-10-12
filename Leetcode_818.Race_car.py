class Solution:
    def racecar(self, target: int) -> int:
        queue = collections.deque([(0, 0, 1)])
        visited = set()                 
        
        while queue:
            moves, position, speed = queue.popleft()
            
            if position == target:
                return moves
            
            if (position, speed) in visited:
                continue
            else:
                visited.add((position, speed))
                
                queue.append((moves + 1, position + speed, speed * 2))
                
                if (position + speed > target and speed > 0) or (position + speed < target and speed < 0):
                    speed = -1 if speed > 0 else 1
                    
                    queue.append((moves + 1, position, speed))
                    
                    
        """
        T = O(log Target)
        S = O(log Target)
        """
        
