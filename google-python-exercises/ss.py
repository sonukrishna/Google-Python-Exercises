def print_dict(filename):
  d={}
  for lines in open(filename):
    lines=lines.split()
    for words in lines:
      words.lower()
      if words not in d:
        d[words]=1
      else:
        d[words] += 1
  return d
def print_words(filename):
  words=print_dict(filename)
  srted_words=sorted(words.keys())
  for i in srted_words:
    print i,words[i]
def print_top(filename):
  words=print_dict(filename)
  srted_words=sorted(words.items(),key=lambda x:x[1],reverse=True)
  for i,j in srted_words[:20]:
    print i,j


print_top('small.txt')
