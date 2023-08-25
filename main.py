
from Graph import *
from shortestPath import *
from getPlot import *
from pbft import *
import warnings
warnings.filterwarnings("ignore", category=FutureWarning)

print("Graph: ")
fileName = "graph.txt"

# Generate the Graph
G = Graph(fileName)
G.generate()
print("Generated\n")

source, destination = 1,6
print("USER-REQUEST:\nFROM: {}, TO: {}\n".format(source,destination))

# run PBFT Consensus
pbft(source,destination,G,6)


source, destination = 2,19
print("USER-REQUEST:\nFROM: {}, TO: {}\n".format(source,destination))

# run PBFT Consensus
pbft(source,destination,G,10) #Since the number of nodes is 20, so 10(faulty nodes) wouldnot reach consensus 



