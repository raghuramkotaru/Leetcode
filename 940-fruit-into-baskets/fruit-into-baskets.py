class Solution:
    def totalFruit(self, fruit: List[int]) -> int:
        l, total, ans = 0,0,0
        count = defaultdict(int)

        for i in range(len(fruit)):
            count[fruit[i]] += 1
            total +=1

            while len(count) >2:
                count[fruit[l]] -= 1
                
                total -= 1
                if not count[fruit[l]]:
                    count.pop(fruit[l])
                l +=1 
            ans = max(ans,total)
            
        return ans

                
            
