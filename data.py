import pandas as pd

import matplotlib.pyplot as plt

print("Opening database... (~20s)")

xl_file = pd.ExcelFile("db.xlsx")
data = xl_file.parse("kepessegvizsga_2019_kuld")

l = data.values.tolist()

l = [x for x in l if x[7] == 'Limba maghiară'] #7 = limba
l = [x for x in l if x[9] != '#NULL!'] #9 = media

judets = set([x[3] for x in l]) #3 = judet

shown = [0,1,2,3]

def hideUnhide(num):
	global shown
	if num in shown:
		shown.remove(num)
	else:
		shown += [num]
		shown.sort()


def viz(juds):
	print(juds)
	ml = [x for x in l if x[3] in juds]
	print(len(ml))
	
	grads = []
	
	g1 = [] #5
	g2 = [] #6
	g3 = [] #8
	
	for jud in juds:
		grads += [getAvg(ml, 9, jud)]
		g1 += [getAvg(ml, 5, jud)]
		g2 += [getAvg(ml, 6, jud)]
		g3 += [getAvg(ml, 8, jud)]
	
	
	if len(juds) > 1:
		juds = ["AVG"]+juds
		grads = [getAvg(ml, 9, "")]+grads
		
		g1 = [getAvg(ml, 5, "")]+g1
		g2 = [getAvg(ml, 6, "")]+g2
		g3 = [getAvg(ml, 8, "")]+g3
	
	
	drawPlot(grads, g1, g2, g3, juds)

def clearName(x):

	x = x.split('"')[1] if '"' in x else x
	x = x.split("'")[1] if "'" in x else x
	bads = ["?coala","?COALA","?coala","GIMNAZIALĂ","Liceul","Teoretic","SCOALA","GIMNAZIALA","ŞCOALA", "LICEUL","Gimnazială","Teologic", "COLEGIUL", "TEHNIC", "TEHNOLOGIC"]
	for bad in bads:
		x = x.replace(bad, "")
	
	
	return x

def judViz(jud):
	print(jud)
	ml = [x for x in l if x[3] == jud]
	print(len(ml))
	
	schools = set([x[4] for x in ml])
	print(schools)
	
	grads = []
	
	g1 = [] #5
	g2 = [] #6
	g3 = [] #8
	
	
	for schl in schools:
		grads += [getJudAvg(ml, 9, schl)]
		g1 += [getJudAvg(ml, 5, schl)]
		g2 += [getJudAvg(ml, 6, schl)]
		g3 += [getJudAvg(ml, 8, schl)]
	
	
	schools = [clearName(x) for x in schools]
	
	if len(schools) > 1:
		schools = ["AVG"]+schools
		grads = [getJudAvg(ml, 9, "")]+grads
		
		g1 = [getJudAvg(ml, 5, "")]+g1
		g2 = [getJudAvg(ml, 6, "")]+g2
		g3 = [getJudAvg(ml, 8, "")]+g3
	
	drawPlot(grads, g1, g2, g3, schools)
	

def getAvg(ml, col, jud):
	cl = []
	if jud == "":
		cl = [x[col] for x in ml]
	else:
		cl = [x[col] for x in ml if x[3] == jud]
	return sum(cl)/len(cl)

def getJudAvg(ml, col, schl):
	cl = []
	if schl == "":
		cl = [x[col] for x in ml]
	else:
		cl = [x[col] for x in ml if x[4] == schl]
	return sum(cl)/len(cl)


def drawPlot(grads, g1, g2, g3, names):
	fig, ax = plt.subplots()
	
	grads, g3, g2, g1, names = (list(t) for t in zip(*sorted(zip(grads, g3, g2, g1, names), key=lambda el:el[shown[0]], reverse=True)))
	
	
	if 0 in shown:
		ax.bar([i*2 for i in range(len(names))], grads, 1.5, label = "Media", color = (1,0,1,1))
	
	if 1 in shown:
		ax.bar([i*2-0.5 for i in range(len(names))], g3, 0.5, label = "Magyar", color = (0.2,0.8,0,1))
	
	if 2 in shown:
		ax.bar([i*2 for i in range(len(names))], g2, 0.5, label = "Matek", color = (0.1,0.5,1,1))
	
	if 3 in shown:
		ax.bar([i*2+0.5 for i in range(len(names))], g1, 0.5, label = "Román", color = (0.9,0,0,1))
	
	

	
	ax.legend()
	plt.xticks([i*2 for i in range(len(names))], names, rotation = "vertical")
	
	plt.tight_layout()

	plt.show()