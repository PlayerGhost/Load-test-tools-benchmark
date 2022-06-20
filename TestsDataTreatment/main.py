import gspread
from oauth2client.service_account import ServiceAccountCredentials
import json
import numpy as np


def getMetricsResults(durations):
    durations = np.array(durations)

    minValue = np.min(durations)
    maxValue = np.max(durations)
    meanValue = np.mean(durations)
    percentileValue = np.percentile(durations, 95)
    medianValue = np.median(durations)

    return {'min': minValue, 'max': maxValue, 'avg': meanValue, 'med': medianValue, 'p(95)': percentileValue}
    # return [str(minValue).replace(".", ","), str(meanValue).replace(".", ","), str(percentileValue).replace(".", ","), str(medianValue).replace(".", ",")]


def getLatenciesPerMethod(k6, vegeta, wrk, jmeter, metric):
    metrics = [
        np.array_split(k6, 3),
        np.array_split(vegeta, 3),
        np.array_split(wrk, 3),
        np.array_split(jmeter, 3)
    ]

    getMethod = [[], [], []]
    streamMethod = [[], [], []]
    dripMethod = [[], [], []]

    for tool in metrics:
        for j in range(len(tool)):
            getMethod[j].append(float(tool[0][j][metric]))
            streamMethod[j].append(float(tool[1][j][metric]))
            dripMethod[j].append(float(tool[2][j][metric]))

    return [getMethod, streamMethod, dripMethod]


def updateSheet(sheet, metrics, startLine, endLine, isNewMetric=False):
    minValues = []
    maxValues = []
    meanValues = []
    medianValues = []
    percentileValues = []

    for i in metrics:
        minValues.append(i['min'])
        maxValues.append(i['max'])
        meanValues.append(i['avg'])
        medianValues.append(i['med'])
        percentileValues.append(i['p(95)'])

    minValues = np.array_split(minValues, 3)
    maxValues = np.array_split(maxValues, 3)
    meanValues = np.array_split(meanValues, 3)
    medianValues = np.array_split(medianValues, 3)
    percentileValues = np.array_split(percentileValues, 3)

    columnsValues = []

    for i in range(3):
        columnValues = []

        columnValues += minValues[i].tolist()
        columnValues += maxValues[i].tolist()
        columnValues += meanValues[i].tolist()
        columnValues += medianValues[i].tolist()
        columnValues += percentileValues[i].tolist()

        columnsValues.append(columnValues)

    columnsLabels = ["B", "D", "F"]

    if isNewMetric:
        columnsLabels = ["P", "Q", "R"]

    for i in range(len(columnsLabels)):
        cellList = sheet.range(f'{columnsLabels[i]}{startLine}:{columnsLabels[i]}{endLine}')

        for j in range(len(cellList)):
            cellList[j].value = columnsValues[i][j]

        sheet.update_cells(cellList)


def updateSheetPerMethod(sheet, metrics, startLine, endLine):
    columnsLabels = ["J", "K", "L"]

    for i in range(len(columnsLabels)):
        cellList = sheet.range(f'{columnsLabels[i]}{startLine}:{columnsLabels[i]}{endLine}')

        for j in range(len(cellList)):
            cellList[j].value = metrics[i][j]

        sheet.update_cells(cellList)


def getMetricsK6NewMetric():
    metrics = []

    for i in range(1, 4):
        metricsAux = loadJSON("ResultsData/K6/new-metric-" + str(i))
        metrics.append(metricsAux["metrics"]["http_req_duration"])

    return metrics


def getMetricsK6():
    metrics = []

    for i in range(0, 9):
        metricsAux = loadJSON("ResultsData/K6/k6" + str(i + 1))
        metrics.append(metricsAux["metrics"]["http_req_duration"])

    return metrics


def getMetricsVegeta():
    metrics = []

    for i in range(0, 9):
        latencies = loadJSON("ResultsData/Vegeta/vegeta" + str(i + 1))[:-1]
        latenciesPass = []

        for j in latencies:
            j = json.loads(j)

            if j["code"] == 200:
                latenciesPass.append(j["latency"] / 1000000)

        latencies = latenciesPass

        metrics.append(getMetricsResults(latencies))

    return metrics


def getMetricsWrk():
    metrics = []

    for i in range(0, 9):
        latencies = loadCSV("ResultsData/Wrk/wrk" + str(i + 1))
        latencies = [int(latencies) / 1000 for latencies in latencies]

        metrics.append(getMetricsResults(latencies))

    return metrics


def getMetricsJmeter():
    metrics = []

    for i in range(0, 9):
        latencies = loadCSV("ResultsData/Jmeter/jmeter" + str(i + 1))
        latencies = [int(latencies) for latencies in latencies]

        metrics.append(getMetricsResults(latencies))

    return metrics


def loadJSON(fileName):
    JSONName = fileName + ".json"

    with open(JSONName, 'r') as file:
        return json.load(file)


def loadCSV(toolName):
    CSVName = toolName + ".csv"

    with open(CSVName, 'r') as file:
        return file.read().splitlines()


if __name__ == '__main__':
    # define the scope
    scope = ['https://spreadsheets.google.com/feeds', 'https://www.googleapis.com/auth/drive']

    # add credentials to the account
    creds = ServiceAccountCredentials.from_json_keyfile_name('eth-vs-ton-b8e005fda44c.json', scope)

    # authorize the clientsheet
    client = gspread.authorize(creds)

    # get the instance of the Spreadsheet
    sheet = client.open_by_key("1_nZLaWe0RleL9vHWVRra3ltOy37VnQJy5SRqrdJNw9c").sheet1

    print("Metrics: ")
    print("Min", "Max", "Mean", "Median", "Percentile(95)")

    metricsK6 = getMetricsK6()
    metricsVegeta = getMetricsVegeta()
    metricsWrk = getMetricsWrk()
    metricsJmeter = getMetricsJmeter()

    medianas = getLatenciesPerMethod(metricsK6, metricsVegeta, metricsWrk, metricsJmeter, "med")
    medias = getLatenciesPerMethod(metricsK6, metricsVegeta, metricsWrk, metricsJmeter, "avg")

    metricsK6NewMetric = getMetricsK6NewMetric()

    print(metricsK6)
    print(metricsVegeta)
    print(metricsWrk)
    print(metricsJmeter)
    print(medianas)
    print(medias)
    print(metricsK6NewMetric)

    updateSheet(sheet, metricsK6, 3, 17)
    updateSheet(sheet, metricsVegeta, 21, 35)
    updateSheet(sheet, metricsWrk, 39, 53)
    updateSheet(sheet, metricsJmeter, 57, 71)

    updateSheetPerMethod(sheet, medias[0], 3, 6)
    updateSheetPerMethod(sheet, medias[1], 10, 13)
    updateSheetPerMethod(sheet, medias[2], 17, 20)

    updateSheet(sheet, metricsK6NewMetric, 2, 6, isNewMetric=True)
