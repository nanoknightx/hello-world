def main():
    """Calculates the average of an array, rounded to the nearest integer."""

    arr = [2, 4, 8]
    sum = 0

    for i in range(len(arr)):
        sum += arr[i]

    sum /= len(arr)
    
    if sum > 0:
        result = int(sum + 0.5)
    else:
        result = int(sum - 0.5)

    print(result)

if __name__ == "__main__":
    main()