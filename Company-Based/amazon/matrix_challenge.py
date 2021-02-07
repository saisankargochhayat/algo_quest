# https://leetcode.com/discuss/interview-question/1001809/AMAZON-or-OA-or-Matrix-challenge
def matrix_challenge(arr):
  for i, row in enumerate(arr):
    arr[i] = [c for c in row]

  rows = len(arr)
  cols = len(arr[0])
  possible, visited_start = search((0, 0), (rows-1, cols-1), arr)
  if possible:
    return True

  _, visited_end = search((rows-1, cols-1), (0, 0), arr)

  neighbors_start = get_all_neighbors(visited_start, arr)
  neighbors_end = get_all_neighbors(visited_end, arr)

  num_intersect = len(neighbors_start.intersection(neighbors_end))
  if num_intersect == 0:
    return "not possible"
  else:
    return num_intersect

def get_all_neighbors(vertices, arr):
  neighbors = set()
  for v in vertices:
    neighbors = neighbors.union(get_neighbors(v, arr, "0"))
  return neighbors

def search(start, target, arr):
  stack = [start]
  visited = {start}

  while stack:
    v = stack.pop()
    if v == target:
      return True, None

    for n in get_neighbors(v, arr, "1"):
      if n in visited:
        continue
      stack.append(n)
      visited.add(n)

  return False, visited

def get_neighbors(v, arr, val):
  rows = len(arr)
  cols = len(arr[0])
  i, j = v

  neighbors = []
  neighbors.extend(valid(i-1, j, rows, cols, arr, val))
  neighbors.extend(valid(i+1, j, rows, cols, arr, val))
  neighbors.extend(valid(i, j-1, rows, cols, arr, val))
  neighbors.extend(valid(i, j+1, rows, cols, arr, val))
  return neighbors

def valid(i, j, rows, cols, arr, val):
  result = []
  if i >= 0 and j >= 0 and i < rows and j < cols and arr[i][j] == val:
    result = [(i, j)]
  return result


print(matrix_challenge(["11100", "10011", "10101", "10011"]))