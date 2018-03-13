# Phonebook Dictionary
phonebook_dict = {
  'Alice': '703-493-1834',
  'Bob': '857-384-1234',
  'Elizabeth': '484-584-2923'
}

print(phonebook_dict.get("Elizabeth"))
phonebook_dict["Kareem"] = "938-489-1234"
print(phonebook_dict)
del phonebook_dict["Alice"]
print(phonebook_dict)
phonebook_dict["Bob"] = "968-345-2345"
print(phonebook_dict)


#Nested Dictionary
ramit = {
  'name': 'Ramit',
  'email': 'ramit@gmail.com',
  'interests': ['movies', 'tennis'],
  'friends': [
    {
      'name': 'Jasmine',
      'email': 'jasmine@yahoo.com',
      'interests': ['photography', 'tennis']
    },
    {
      'name': 'Jan',
      'email': 'jan@hotmail.com',
      'interests': ['movies', 'tv']
    }
  ]
}

print(ramit.get("email"))
print(ramit.get("interests")[0])
print(ramit.get("friends")[0].get("email"))
print(ramit.get("friends")[1].get("interests")[1])


#Letter Summary
def letter_histogram(word):
        return {i: word.count(i) for i in word}
        
print(letter_histogram("nelson"))

#Word Summary
def word_histogram(string):
    words = string.lower().split()
    return {w:words.count(w) for w in words}
    
print(word_histogram("To be or not to be"))


#Bonus Challenge
i
def word_histogram_max(string):
    words
    result = {w:words.count(w) for w in words}
    d = Counter(result)
    d.most_common()
    for k, v in d.most_common(3):
      return '%s: %i' % (k, v)
    
print(word_histogram_max("To be or not to be"))
    