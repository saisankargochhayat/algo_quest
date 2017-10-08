if __name__ == '__main__' : 
    arr1=[1,2,3,4,7,8,9]
    arr2=[1,2,5,6,7,8]
    uncommon_ele = len(set(arr1)-set(arr2))+len(set(arr2)-set(arr1))
    print(uncommon_ele)