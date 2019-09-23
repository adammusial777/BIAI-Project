from Tile import Tile


class BoardReader:

    tileWidth = 40
    tileHeight = 40
    black = (0, 0, 0)
    green = (158, 242, 156)
    white = (249, 244, 255)
    grey = (224, 218, 254)
    red = (255, 118, 118)

    def ReadFile(self, filepath):

        colorsArray = [BoardReader.black, BoardReader.green,
                       BoardReader.white, BoardReader.grey, BoardReader.red]
        tagsArray = ["Wall", "StartArea",
                     "Floor", "Floor", "FinishArea"]
        tilesArray = []
        currentRow = 0
        currentColumn = 0
        with open(filepath) as f:
            for i in f:
                for j in i:
                    if j != '\n':
                        tilesArray.append(Tile(colorsArray[int(j)], currentColumn * BoardReader.tileWidth, currentRow *
                                               BoardReader.tileHeight, BoardReader.tileWidth, BoardReader.tileHeight, tagsArray[int(j)]))
                        currentColumn += 1
                currentColumn = 0
                currentRow += 1
        return tilesArray
