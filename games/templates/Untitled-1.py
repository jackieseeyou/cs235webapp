def fizzBuzz(n):
    for i in range(1, n):
        if i % 3 == 0 and i % 5 == 0:
            print("FizzBuzz")
        elif i % 3 == 0:
            print("Fizz")
        elif i % 5 == 0:
            print("Buzz")
        else:
            print(i)
        

def reverseArray(arr):
    start = 0
    end = len(arr) - 1

    while start < end:
        arr[start], arr[end] = arr[end], arr[start]
        start += 1
        end -= 1

    return arr


def closestNumbers(numbers):
    numbers.sort()
    min_diff = numbers[1] - numbers[0]
    pairs = []

    for i in range(1, len(numbers)):
        diff = numbers[i] - numbers[i-1]
        if diff < min_diff:
            min_diff = diff
            pairs = [(numbers[i-1], numbers[i])]
        elif diff == min_diff:
            pairs.append((numbers[i-1], numbers[i]))

    for pair in pairs:
        print(f"{pair[0]} {pair[1]}")


def compareStrings(s1, s2):
    if s1 == s2:
        return 1
    
    new_s1 = ""
    new_s2 = ""
    for i in range(len(s1)):
        if s1[i] == "#":
            if len(new_s1) > 0:
                new_s1 = new_s1[:-1]
            else:
                continue
        else:
            new_s1 += s1[i]
    for i in range(len(s2)):
        if s2[i] == "#":
            if len(new_s2) > 0:
                new_s2 = new_s2[:-1]
            else:
                continue
        else:
            new_s2 += s2[i]

    if new_s1 == new_s2:
        return 1
    else:
        return 0
    
    
compareStrings("yf#c#", "yy#k#pp##")