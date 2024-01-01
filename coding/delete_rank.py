list = []

for x in range (0,5):
  item = input('Enter a number:  ')
  list.append(item)
  
rank = input('Enter a rank:  ')
rank = int(rank)

def delete_rank(list, rank):
  #list.remove(rank)
  list1 = list[:]
  for y in range(0,4):
    if y >= rank:
      list1[y] = list1[y+1]
  del list1[y+1]
  return (list1)

final_list = delete_rank(list, rank)

print (final_list)
