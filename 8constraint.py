r = set()

def sub(i, l, k):
    if sum(l) == k:  
        r.add(tuple(l))
    if i == len(nums):
        return
    sub(i + 1, l, k) 
    l.append(nums[i])  
    sub(i + 1, l, k)
    l.pop()

nums = list(map(int, input("Enter List: ").split()))
k = int(input("Target sum (k): "))

sub(0, [], k)
print(r)