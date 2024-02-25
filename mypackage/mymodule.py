#!/Users/Aaron/.pyenv/shims/python
def top_n(items,n):
  """
  The function `top_n` takes a list of items and an integer n, sorts the items in ascending order, and
  returns the top n items in descending order.
  
  :param items: It looks like the code snippet you provided is a sorting algorithm to find the top n
  items in a list. However, there seems to be a syntax error in the code. The range function should
  not have a minus sign before 'i' in the inner loop
  :param n: The parameter `n` in the `top_n` function represents the number of top items that you want
  to retrieve from the input list `items`. It specifies how many of the largest items you want to
  return from the sorted list
  :return: The function `top_n` is returning the top `n` items from the input list `items`, after
  sorting the list in ascending order.
  """
  for j in range(n):
    for i  in range(len(items)-1-j):
      if items[i]> items[i+1]:
        items[i],items[i+1] = items[i+1], items[i]

  top_n = items[-n::]
  return top_n[::-1]

    


print(top_n([90,9,89,7,5,6,78],2))