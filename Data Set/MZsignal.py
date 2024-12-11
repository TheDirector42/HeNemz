import matplotlib.pyplot as plt
filepath= "2024-11-12-Test2-PDout.txt"
results=[]
with open(filepath, encoding='latin_1') as f:
	for line in f:
		results.append(line)

r= results[1:]
data=[]
for d in r:
	t = d.split('\t')[:-1];data.append(t)
	
plt.plot(results)
plt.show()