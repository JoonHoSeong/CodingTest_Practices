def solution(arr, idx):
    arr = arr[idx:]
    try : return arr.index(1) + idx
    except : return -1