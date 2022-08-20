"""
Day 14 - Aug 19

Given two strings representing sentences, return the words that are not common to both strings (i.e. the words that only appear in one of the sentences). You may assume that each sentence is a sequence of words (without punctuation) correctly separated using space characters. 

Ex: given the following strings...

sentence1 = "the quick", sentence2 = "brown fox", return ["the", "quick", "brown", "fox"]
sentence1 = "the tortoise beat the haire", sentence2 = "the tortoise lost to the haire", return ["beat", "to", "lost"]
sentence1 = "copper coffee pot", sentence2 = "hot coffee pot", return ["copper", "hot"]
"""

sentence1 = input()
sentence2 = input()

def uniqueWords(sentence1, sentence2):
  hash1 = {}
  hash2 = {}
  results = []
  sentence1 = sentence1.split(' ')
  sentence2 = sentence2.split(' ')
  for word in sentence2:
    if word not in hash1:
      hash1[word] = True

  for word in sentence1:
    if word not in hash1:
      results.append(word)
    if word not in hash2:
      hash2[word] = True

  for word in sentence2:
    if word not in hash2:
      results.append(word)

  return results

"""
Time Complexity: O(n) where n = max(len(sentence1.split(' ')), len(sentence2.split(' ')))
"""

print(uniqueWords(sentence1, sentence2))