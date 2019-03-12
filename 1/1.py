def count_sheeps(arrayOfSheeps):
    return arrayOfSheeps.count(True)
    # sum = 0
    # for sheep in arrayOfSheeps:
    #     if sheep == True:
    #         sum += 1
    # return sum

array1 = [True,  True,  True,  False,
          True,  True,  True,  True ,
          True,  False, True,  False,
          True,  False, False, True ,
          True,  True,  True,  True ,
          False, False, True,  True ];

print(count_sheeps(array1))

