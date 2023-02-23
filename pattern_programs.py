# Pattern_01_Line
'''
    *  *  *  *  *
'''

# simple Line program
n = 5
for ele in range(n):
    print('* ', end = ' ')


# Pattern_02_Square
'''
    * * * * 
    * * * * 
    * * * * 
    * * * *
'''

n = 4
for ele in range(1, n+1):
    print('* '*n)

# Pattern_03_Half_Pyramid
'''
    * 
    * * 
    * * * 
    * * * * 
    * * * * *
'''

n = 5
for ele in range(1,n+1):
    print(ele*'* ')

# Pattern_04_Invert_Half_Pyramid
'''
    * * * * * 
    * * * * 
    * * * 
    * * 
    *
'''

n = 5
for ele in range(n, 0, -1):
    print(ele*'* ')


    
# Pattern_05
'''
        *
       **
      ***
     ****
'''

n = 5
for ele in range(1,n):
    print((n-ele)*' '+ele*'*')


# Pattern_06_Pyramid
'''
        * 
       * * 
      * * * 
     * * * * 
    * * * * * 
'''

n = 5
for ele in range(1,n):
    print((n-ele)*' '+ele*'* ')


# Pattern_07_Invert_Pyramid
'''
    * * * * * 
     * * * * 
      * * * 
       * * 
        *
'''
n = 5
for ele in range(n, 0, -1):
    print((n-ele)*' '+ele*'* ')
    
# Pattern_08_Daimond
'''
        * 
       * * 
      * * * 
     * * * * 
    * * * * * 
     * * * * 
      * * * 
       * * 
        *
'''
n = 5
for ele in range(1,n):
    print((n-ele)*' '+ele*'* ')
for ele in range(n, 0, -1):
    print((n-ele)*' '+ele*'* ')
    
# Pattern_09_Number_Half_Pyramid
'''
    1
    1 2
    1 2 3
    1 2 3 4
'''
n = 4
for ele in range(1,n+1):
    print(*[i for i in range(1, ele+1)])
# Pattern_10_Number_Half_Invert_Pyramid
'''
    1 2 3 4
    1 2 3
    1 2
    1
'''
n = 4
for ele in range(n, 0, -1):
    print(*[i for i in range(1, ele+1)])


# Pattern_11_
'''
        1
       22
      333
     4444
'''
n = 5
for ele in range(n):
    print(' '*(n-ele)+ele*str(ele))
    
    
 
# Pattern_12_
'''
    1 0 0 0 0 
    0 1 0 0 0 
    0 0 1 0 0 
    0 0 0 1 0 
    0 0 0 0 1
'''
n = 5
for row in range(0,n):
    for col in range(0,n):
        if row == col:
            print('1', end= ' ' )
        else:
            print('0', end = ' ')
    print()

# Pattern_13_
'''
    * * * * * * * * * * 
    * * * *     * * * * 
    * * *         * * * 
    * *             * * 
    *                 * 
    *                 * 
    * *             * * 
    * * *         * * * 
    * * * *     * * * * 
    * * * * * * * * * *
'''
n = 5
for ele in range(n,0, -1):
    for itm in range(ele, 0, -1):
        print('*', end =  ' ')
    for itm in range(2*(n-ele)):
        print(' ', end = ' ')
    for itm in range(ele, 0, -1):
        print('*', end =' ')
    print()
for ele in range(n):
    for itm in range(ele+1):
        print('*', end =  ' ')
    for itm in range(2*(n-ele-1)):
        print(' ', end = ' ')
    for itm in range(ele+1):
        print('*', end =' ')
    print()



# Pattern_14_
# Pattern_15_
