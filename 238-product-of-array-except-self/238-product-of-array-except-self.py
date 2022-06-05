def print_array(arr):
    print("printing array")
    for i in arr:
        print("{} ".format(i), end="", flush=True)
        
class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        # copy nums for reference
        products = list(nums)
        # for readability, assign the length of nums to a variable
        n = len(nums)
        
        # calculate the products of all numbers to the left of index i
        for i in range(1,n-1):
            products[i] *= products[i-1]
        
        # Now, from right to left, calculate the right products and update products array
        right_product = 1
        
        for i in range(n-1,-1,-1):
            if i==n:
                products[i] = products[i-1]
            elif i==0:
                products[i] = right_product
            else:
                products[i] = products[i-1] * right_product
            print("i: {}, products[i]: {}, right_product: {}".format(
                i,
                products[i],
                right_product
            ))
            right_product *= nums[i]
        print_array(products)
        
        return products