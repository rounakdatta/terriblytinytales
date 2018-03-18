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

def give_count(n):
	
	url = "http://terriblytinytales.com/test.txt"
	data = requests.get(url).text.split()
	data = [elem.lower() for elem in data]
	
	final_list = []
	
	root = TrieNode('__ttt__')
	for item in data:
	
		if(find_word(root, item)[0] == True):
	
			target = list(filter(lambda x: item in x, final_list))
			if(target != []):
				target = target[0]
				final_list[final_list.index(target)][1] += 1
	
			else:
				final_list.append([item, 1])	
		
		else:
			add(root, item)
			final_list.append([item, 1])
	
	print(len(final_list))
	final_list = sorted(final_list, key=lambda x : x[1], reverse=True)

	return final_list