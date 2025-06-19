class MissingAndRepeatingNumber:
    '''
    Here Use a count array initilially storing all zeros and update it while iterating over the array
    '''
    def missing_repeating_number(self,arr):
        missing=-1
        repeating = -1
        count_array = [0] * (len(arr) +1)
        for i in range(len(arr)):
            count_array[arr[i]] +=1
        # print(count_array)
        for j,v in enumerate(count_array,1):
            if v==2:
                repeating=j-1
            if v==0:
                missing=j-1
        print(missing,repeating)
        '''
        Time Complexity :O(N+N)
        Space Complexity : O(N)
        '''


        '''
        Here we are using the formulas of sum of N natural numbers and sum of squares of first n natural numbers 
        x - y = S - SN
        x^2 - y^2 = Sq - Sqn
        x + y = (Sq - Sqn) / (x-y)
        x = {((Sq - Sqn) / (x-y)) + (S - SN)} / 2
        y = ((Sq - Sqn) / (x-y)) - x
        '''

    def missing_repeating_numbers_optimal(self,arr):
        n =len(arr)
        S=0
        Sn = (n*(n+1))/2
        Squ=0
        Squn = (n*(n+1)*(2*n+1))/6
        for i,v in enumerate(arr):
            S+=v
            Squ+= v*v
        x_y = S-Sn
        xplusy = (Squ-Squn)/x_y
        x = ((x_y)+(xplusy))/2
        y = xplusy - x
        print(x,y)

        '''
        Time Complexity : O(N)
        Space Complexity : O(1)
        '''
        


if __name__ == "__main__":
    lst = [4,3,6,2,1,1]
    sol = MissingAndRepeatingNumber()
    # print(sol.missing_repeating_number(lst))
    sol.missing_repeating_numbers_optimal(lst)