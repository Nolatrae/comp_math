file = open('input.txt', 'r')
# with open("input.txt", "r") as f:
peaks = int(file.readline().rstrip())
arr = [0] * peaks
num_island = 1
answ = 0
for line in file.readlines():
    line_arr = [int(i) for i in line.split()]
    if arr[line_arr[0] - 1] == 0 and arr[line_arr[1] - 1] == 0:
          arr[line_arr[0] - 1] = num_island
          arr[line_arr[1] - 1] = num_island
          num_island += 1
          answ += 1

    elif arr[line_arr[0] - 1] != 0 and arr[line_arr[1] - 1] != 0:
      for i in range(peaks):
        if arr[i] == arr[line_arr[1] - 1]:
          arr[i] = arr[line_arr[0] - 1]
          answ -= 1

    elif arr[line_arr[0] - 1] != 0 or arr[line_arr[1] - 1] != 0:
            if arr[line_arr[0] - 1] != 0:
                arr[line_arr[1] - 1] = arr[line_arr[0] - 1]
            elif arr[line_arr[1] - 1] != 0:
                arr[line_arr[0] - 1] = arr[line_arr[1] - 1]
                num_island += 1

for i in range(peaks):
    if arr[i] == 0:
        arr[i] = num_island
        num_island += 1
        answ += 1
print(answ - 1)
