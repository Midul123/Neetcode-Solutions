#Leetcode238
def productExceptSelf(nums):
        product= 1
        zero_count=0
        for num in nums:
            if num != 0:
                product *= num
            else:
                zero_count += 1

        output = []
        for num in nums:
            if zero_count > 1:
                # If more than one zero, all products are zero
                output.append(0)
            elif zero_count == 1:
                # If exactly one zero, only the zero element gets the product of non-zero elements
                if num == 0:
                    output.append(product)
                else:
                    output.append(0)
            else:
                # No zeroes, calculate the product normally (product divided by the current element)
                output.append(product // num)
                
        return(output)
print(productExceptSelf([1,2,3,4]))