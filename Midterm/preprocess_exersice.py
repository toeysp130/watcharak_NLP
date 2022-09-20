article = []
for i in range(5):
    f = open(f"ex{i+1}.txt","r")
    article.append(f.read())

print(article[0])