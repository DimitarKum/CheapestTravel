def distance(i, j, distances):
	i, j = min(i, j), max(i, j)
	return sum(distances[i:j])

def getReachableStationsForwards(i, distances, curCapacity):
	stations = []
	curStation = i + 1
	while curStation < len(distances) + 1:
		if distance(curStation, i, distances) < curCapacity:
			stations.append(curStation)
			curStation += 1
		else:
			break
	return stations


def findMinCost(gasPrices, distances, capacity):
	minCost = [(999999999999, i - 1) for i in range(len(gasPrices))]
	minCost[0] = (gasPrices[0] * capacity, 0)
	for i in range(len(gasPrices)):
		for stationIndex in getReachableStationsForwards(i, distances, capacity):
			if minCost[i][0] + (distance(i, stationIndex, distances)) * gasPrices[stationIndex] < minCost[stationIndex][0]:
				minCost[stationIndex] = (minCost[i][0] + (distance(i, stationIndex, distances)) * gasPrices[stationIndex], i)
	return minCost

def backTrackSolution(minCost):
	stations = list()
	curStation = len(minCost) - 1
	stations.append(curStation)
	while(curStation > 0):
		curStation = minCost[curStation][1]
		stations.append(curStation)
	return sorted(stations)

def main():
	gasPrices = [12, 14, 21, 14, 17, 22, 11, 16, 17, 12, 30, 25, 27, 24, 22, 15, 24, 23, 15, 21]
	distances = [31, 42, 31, 33, 12, 34, 55, 25, 34, 64, 24, 13, 52, 33, 23, 64, 43, 25, 15]
	capacity = 170

	l0 = "Index:    "
	l1 = "GasPrices:"
	l2 = "Distances:   "
	for i in range(len(gasPrices)):
		l0 += '{:>6}'.format(i)
	for i in range(len(gasPrices)):
		l1 += '{:>6}'.format(gasPrices[i])
	for i in range(len(distances)):
		l2 += '{:>6}'.format(distances[i])
	print(l0)
	print(l1)
	print(l2)
	print("Capacity:", capacity)
	print()

	print("Minimum costs\nStation : Total Min Cost")
	m = findMinCost(gasPrices, distances, capacity)
	for i in range(len(gasPrices)):
		print(i, ":", m[i])

	print("\nStations:")
	print(backTrackSolution(m))

main()