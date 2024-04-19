def solution(arr):
    if len(arr) == len(arr[0]) :
        return arr
    elif len(arr) > len(arr[0]) :
        for j in range((len(arr)-len(arr[0]))) :
            for i in arr :
                i.append(0)
    else :
        for i in range((len(arr[0])-len(arr))) :
            arr.append([0 for i in range(len(arr[0]))])
    return arr