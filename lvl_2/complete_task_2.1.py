
data = input()
s = data.split()
A = [int(x) for x in s]

def maximum(arr):
  max = arr[0]
  for ele in arr:
    if ele > max:
      max = ele
  return max


def minimum(arr):
  min = arr[0]
  for ele in arr:
    if ele < min:
      min = ele
  return min

print("max =", maximum(A),", min =", minimum(A))