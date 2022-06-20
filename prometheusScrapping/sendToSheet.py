import gspread
from oauth2client.service_account import ServiceAccountCredentials
import numpy as np


def updateSheetPerMethod(sheet, metrics, startLine, endLine):
    columnsLabels = ["J", "K", "L"]

    for i in range(len(columnsLabels)):
        cellList = sheet.range(f'{columnsLabels[i]}{startLine}:{columnsLabels[i]}{endLine}')

        for j in range(len(cellList)):
            cellList[j].value = metrics[i][j]

        sheet.update_cells(cellList)


if __name__ == '__main__':
    with open("outputs.txt", "r") as f:
        lines = [str((float(i.strip()) * 1000)).replace(".", ",") for i in f.readlines()]

    toolsAvgs = np.array_split(lines, 4)
    toolsAvgsMethods = []

    getMethod = [[], [], []]
    streamMethod = [[], [], []]
    dripMethod = [[], [], []]

    for i in toolsAvgs:
        toolsAvgsMethods.append([i.tolist() for i in np.array_split(i, 3)])

    for tool in toolsAvgsMethods:
        for j in range(len(tool)):
            getMethod[j].append(tool[0][j])
            streamMethod[j].append(tool[1][j])
            dripMethod[j].append(tool[2][j])

    # define the scope
    scope = ['https://spreadsheets.google.com/feeds', 'https://www.googleapis.com/auth/drive']

    # add credentials to the account
    creds = ServiceAccountCredentials.from_json_keyfile_name('eth-vs-ton-b8e005fda44c.json', scope)

    # authorize the clientsheet
    client = gspread.authorize(creds)

    # get the instance of the Spreadsheet
    sheet = client.open_by_key("1_nZLaWe0RleL9vHWVRra3ltOy37VnQJy5SRqrdJNw9c").sheet1

    updateSheetPerMethod(sheet, getMethod, 25, 28)
    updateSheetPerMethod(sheet, streamMethod, 32, 35)
    updateSheetPerMethod(sheet, dripMethod, 39, 42)
