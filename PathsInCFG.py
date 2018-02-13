def bitArrayToString(bitArray):
	finalStr = ""
	for bit in bitArray:
		if bit == "0":
			finalStr = finalStr + "F"
		elif bit == "1":
			finalStr = finalStr + "T"
		else:
			print "ERROR"
	return finalStr

def nodePathToString(nodePath):
	finalStr = ""
	for node in nodePath:
		if node == "18":
			finalStr = finalStr + node
		else:
			finalStr = finalStr + node + ", "
	return finalStr

# Find all paths in a CFG

condStmts = ["3", "6", "7", "11", "15"] # Nodes with conditions

exitPath = {"3": "3F", "6": "6F", "7": "7T", "11": "11F", "15": "15F"} # At conditions, which way will get you out of the loop

paths = {"1": "2", "2": "3", "3F": "13", "3T": "4", "4": "5", "5": "6", "6F": "10", "6T": "7",
"7F": "8", "7T": "9", "8": "5", "9": "10", "10": "11", "11F": "2", "11T": "12", "12": "2",
"13": "14", "14": "15", "15F": "18", "15T": "16", "16": "17", "17": "14", "18": "-1"} # Connections between nodes. Must end in -1

finalPaths = {}

binaryCnt = 0b00000 # 5 bits because len(condStmts) = 5
while binaryCnt != 0b100000:
	myBitArray = list(bin(binaryCnt))
	myBitArray = myBitArray[2:]
	while len(myBitArray) != len(condStmts):
		myBitArray.insert(0,'0')
	displayConditions = bitArrayToString(myBitArray)


	currNode = "1"
	condStmtsVisited = []
	nodePath = []
	while(currNode != "-1"):
		nodePath.append(currNode)
		if currNode in condStmts:
			if currNode in condStmtsVisited:
				currNode = exitPath[currNode]
			else:
				condStmtsVisited.append(currNode)
				bitArrayIndex = condStmts.index(currNode)
				if myBitArray[bitArrayIndex] == "0":
					currNode = currNode + "F"
				elif myBitArray[bitArrayIndex] == "1":
					currNode = currNode + "T"
				else:
					print "ERROR"
		currNode = paths[currNode]

	if nodePathToString(nodePath) in finalPaths.values():
		finalPaths[displayConditions] = (nodePathToString(nodePath) + " [DUPL]")
	else:
		finalPaths[displayConditions] = nodePathToString(nodePath)
	binaryCnt += 1

print finalPaths
