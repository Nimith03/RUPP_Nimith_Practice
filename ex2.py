arr = [1, 3, 5, 7, 10]

def solution(arr, targeted_number):
    new_arr = []
    for i in range(len(arr)):  # Use len(arr) to get the correct range
        for j in range(len(arr)):
            if i != j and arr[i] + arr[j] == targeted_number:  # Avoid using the same index
                new_arr.append((arr[i], arr[j]))  # Append as a tuple
    return new_arr

print(solution(arr, 10))
