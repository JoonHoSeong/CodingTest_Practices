def solution(arr):
    try :
        start = arr.index(2)
        arr.reverse()
        end = arr.index(2)
        arr.reverse()
        return arr[start:len(arr)-end]
    except :
        return [-1]