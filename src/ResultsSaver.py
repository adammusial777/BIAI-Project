import csv


class ResultsSaver:

    bestResults = []
    filename = "Results/Results.csv"

    def __init__(self, startTime):
        self.startTime = startTime

    def AppendResult(self, best):
        self.bestResults.append(best)

    def SaveResults(self):
        with open(ResultsSaver.filename, mode='w') as results:
            resultsWriter = csv.writer(
                results, delimiter=',', quotechar='"', quoting=csv.QUOTE_MINIMAL)

            resultsWriter.writerow(['Fitness', 'Distance', 'Time'])

            for result in self.bestResults:
                resultsWriter.writerow(
                    [result.fitness, result.distance, result.time - self.startTime])
