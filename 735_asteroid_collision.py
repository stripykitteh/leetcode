from typing import List

class Solution:
    
    def asteroidCollision(self, asteroids: List[int]) -> List[int]:

        stack = []
        for i in asteroids:
            if i > 0:
                stack.append(i)
            else:
                if stack:
                    do_append = True
                    while stack and stack[-1] > 0:
                        if abs(i) > stack[-1]:
                            stack.pop()
                        elif abs(i) == stack[-1]:
                            stack.pop()
                            do_append = False
                            break
                        else:
                            do_append = False
                            break
                    if do_append:
                        stack.append(i)
                    print(stack)
                else:
                    stack.append(i)
            
        return stack

    
if __name__ == '__main__':

    asteroids = [5,10,-5]
    print(Solution().asteroidCollision(asteroids))
    asteroids = [8,-8]
    print(Solution().asteroidCollision(asteroids))
    asteroids = [10,2,-5]
    print(Solution().asteroidCollision(asteroids))
    asteroids = [-2.1,1,-1]
    print(Solution().asteroidCollision(asteroids))

