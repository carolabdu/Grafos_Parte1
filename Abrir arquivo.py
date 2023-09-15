
with open('textoteste.txt', 'r') as archive:
        text = [int(node) for node in archive.read().split() if node.isdigit()]
        nodes = text[0]
        edges = []
        for i in range(len(text[1:])//2):
            edges += [text[2*i+1:2*i+3]]
print (edges)
