class product:
    def product_array(self,array):
        n=len(array)
        a=[1] * n
        for i in range(n):
            for j in range(n):
                if i!=j:
                    a[i]*=array[j]
        return a
lists=[2,3,4]
product=product()
res=product.product_array(lists)
print(res)

                    
