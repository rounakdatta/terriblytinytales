import requests

class TrieNode(object):

	def __init__(self, char: str):
		self.char = char
		self.children = []
		self.branch_end = False
		self.count = 0

def add(root, word: str):
	node = root
	for char in word:
		iffound = False

		for child in node.children:
			if(child.char == char):

				child.count += 1	

				node = child
				iffound = True
				break

		if not iffound:
			new_node = TrieNode(char)
			node.children.append(new_node)

			node = new_node

	# end of the branch is reached
	node.branch_end = True

def find_word(root, prefix: str):
	node = root

	if not root.children:
		return False, 0

	for char in prefix:
		found = False

		for child in node.children:
			if(child.char == char):

				found = True
				node = child
				break

		if not found:
			return False, 0

	return True, node.count

url = "http://terriblytinytales.com/test.txt"

data = requests.get(url).text.split()

root = TrieNode('__ttt__')
for item in data:
	add(root, item)

query = input()
foo, bar = find_word(root, query)

print("bar=" + str(bar))