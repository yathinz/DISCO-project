# imports
import networkx as nx
from networkx.algorithms import bipartite
# Initialise graph
B = nx.Graph()

cdc = []
ele =[]
c = cdc+ele
p = []
x = []
pref = []
sol = []
links = {}



with open(r"C:\Users\yathi\Documents\disco\disco IP_1_just enough preferences.txt") as f:
    C = f.readline().split()
    E = f.readline().split()
    N = 2 * len(C + E)
    L = 0
    for i in C:
        cdc.append(i + '1')
        cdc.append(i + '2')
    for i in E:
        ele.append(i + '1')
        ele.append(i + '2')
    f.readline()
    while 1:
        Professor = f.readline().split()
        if Professor:
            Name, Type = Professor[0], float(Professor[1])
            pref.append(Professor[2:])
            X = int(Type // 0.5)
            L += X
            x.append(X)
            for i in range(X):
                p.append(float(Name+"."+str(i+1)))
        else:
            for i in range(N - L):
                p.append(float('100.'+str(i+1)))
            break
f.close()
#print(cdc)
#print(ele)
#print(x)
#print(p)
#print(pref)


f = open(r"C:\Users\yathi\Documents\disco\disco OP_1_all slots filled.txt","w")

#creating bipartite graph
B.add_nodes_from(p,bipartite=0)
B.add_nodes_from(c,bipartite=1)


for i in p :
    t = int(i)
    if t<100 :
        preflist = pref[t]
        #print (preflist)
        for j in preflist:
         B.add_edge(i, str(j[0]+"1"), weight = preflist.index(j))
         links[(i,str(j[0]+"1"))] = preflist.index(j)
         B.add_edge(i, j[0]+"2", weight = preflist.index(j))
         links[(i,str(j[0]+"2"))] = preflist.index(j)
    else :
         for j in ele :
          B.add_edge(i, j[0]+"1", weight = 50)
          B.add_edge(i, j[0]+"2", weight = 50)
          links[(i,str(j[0]+"1"))] = 50          
          links[(i,str(j[0]+"2"))] = 50
          
linklist = list(links.keys())
# (linklist)

         
try :
    my_matching = bipartite.matching.minimum_weight_full_matching(B,p)
    sol.append(my_matching)
except ValueError:
    print("no allocation for CDC's possible for given constraints")
    f.write("no allocation for CDC's possible for given constraints")
    
for i in linklist:
     B.remove_edge(i[0], i[1])
     try :
         my_matching = bipartite.matching.minimum_weight_full_matching(B,p)
         sol.append(my_matching)
     except ValueError:
         pass
     B.add_edge(i[0], i[1], weight = links[i])
     
for i in p :
    t = int(i)
    if t<100 :
        preflist = pref[t]
        #print (preflist)
        for j in preflist:
         B.add_edge(i, str(j[0]+"1"), weight = (preflist.index(j))^2)
         links[(i,str(j[0]+"1"))] = (preflist.index(j))^2
         B.add_edge(i, j[0]+"2", weight = (preflist.index(j))^2)
         links[(i,str(j[0]+"2"))] = (preflist.index(j))^2
    else :
         for j in ele :
          B.add_edge(i, j[0]+"1", weight = 50)
          B.add_edge(i, j[0]+"2", weight = 50)
          links[(i,str(j[0]+"1"))] = 50          
          links[(i,str(j[0]+"2"))] = 50
          
linklist = list(links.keys())

try :
    my_matching = bipartite.matching.minimum_weight_full_matching(B,p)
    sol.append(my_matching)
except ValueError:
    print("no allocation for CDC's possible for given constraints")
    f.write("no allocation for CDC's possible for given constraints")
    
for i in linklist:
     B.remove_edge(i[0], i[1])
     try :
         my_matching = bipartite.matching.minimum_weight_full_matching(B,p)
         sol.append(my_matching)
     except ValueError:
         pass
     B.add_edge(i[0], i[1], weight = links[i])


     
print("****************  ALLOTMENTS  ******************")
f.write("**********************        ALLOTMENTS          ****************************")

solu = []
solul = ""
solulu = set()

for i in sol:
  for j in i:
      if (type(j)==type("string")):
          p1 = int(i[j[0]+"1"])
          p2 = int(i[j[0]+"2"])
          #print(p1,p2)
          
          #print(p1,p2)
          if p1 == p2 :
              p2 = 100
              solu.append(str("course " + str(j[0]) + " -> prof" +  str(p1)[0]))
          if (p1<50 and int(p2)<50) :
              #print(str(j[0]) + " " +  str(p1)+ " " + str(p2))
              y1 = min(p1,p2)
              y2 = max(p1,p2)
              p1 = y1
              p2 = y2
              solu.append(str("course " + str(j[0]) + " -> prof" +  str(p1)[0] + " and prof" + str(p2)[0]))
  #print("*******************************")
  #solu = sorted(solu)
  solululu = set(solu)
  solululu = sorted(solululu)
  for k in solululu :
      solul = solul + str(k) + "\n"
  solulu.add(solul)
  solul = ""
  solu.clear()
              
for i in solulu:
    print(i)
    print("*********************")
print("           ")



for i in solulu:
    f.write("\n")
    f.write(i)
    f.write("********************************")
f.close()