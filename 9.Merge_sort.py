def merge_sort(unsorted_list):
   if len(unsorted_list) <= 1:
      return unsorted_list

   mid = len(unsorted_list) // 2
   leftlist = unsorted_list[:mid]
   rightlist = unsorted_list[mid:]

   leftlist = merge_sort(leftlist)
   rightlist = merge_sort(rightlist)
   return list(merge(leftlist, rightlist))


def merge(lefthalf,righthalf):
   res = []
   while len(lefthalf) != 0 and len(righthalf) != 0:
      if lefthalf[0] < righthalf[0]:
         res.append(lefthalf[0])
         lefthalf.remove(lefthalf[0])
      else:
         res.append(righthalf[0])
         righthalf.remove(righthalf[0])
   if len(lefthalf) == 0:
      res = res + righthalf
   else:
      res = res + lefthalf
   return res
unsorted_list = [89, 43, 67, 13, 32, 10, 97]
print(merge_sort(unsorted_list))