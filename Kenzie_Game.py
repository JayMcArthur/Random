import copy

conversion = {
    "1": "Lime Green",
    "2": "Purple",
    "3": "Gray",
    "4": "Orange",
    "5": "Pink",
    "6": "Red",
    "7": "Blue",
    "8": "Light Blue",
    "9": "Dark Green"
}

class Rack:
    def __init__(self, rack):
        self.rackList = [[rack, []]]
        self.workingRack = []
        self.changeRack = []
        self.win = False
        self.completed = 0

    def getMoves(self, location, color, amount, c):
        moves = []
        empty = False
        for l in range(len(self.workingRack[0])):
            if l == location: continue
            if self.workingRack[0][l][0] == 0:
                if self.workingRack[0][l][1] == 0:
                    if self.workingRack[0][l][2] == 0:
                        if self.workingRack[0][l][3] == 0 and not c and not empty and amount <= 3:
                            moves.append(l)
                            empty = True
                            continue
                        elif self.workingRack[0][l][3] == color and amount <= 3:
                            moves.append(l)
                            continue
                    elif self.workingRack[0][l][2] == color and amount <= 2:
                        moves.append(l)
                        continue
                elif self.workingRack[0][l][1] == color and amount == 1:
                    moves.append(l)
                    continue
        return moves

    def performTurn(self):
        self.workingRack = self.rackList.pop(len(self.rackList)-1)
        for i in range(len(self.workingRack[0])):
            com = False
            if self.workingRack[0][i][0] == 0:
                if self.workingRack[0][i][1] == 0:
                    if self.workingRack[0][i][2] == 0:
                        if self.workingRack[0][i][3] == 0:
                            continue
                        else:
                            color = self.workingRack[0][i][3]
                            amount = 1
                            index = 3
                            com = True
                    elif self.workingRack[0][i][2] == self.workingRack[0][i][3]:
                        color = self.workingRack[0][i][2]
                        amount = 2
                        index = 2
                        com = True
                    else:
                        color = self.workingRack[0][i][2]
                        amount = 1
                        index = 2
                elif self.workingRack[0][i][1] == self.workingRack[0][i][2]:
                    if self.workingRack[0][i][1] == self.workingRack[0][i][3]:
                        color = self.workingRack[0][i][1]
                        amount = 3
                        index = 1
                        com = True
                    else:
                        color = self.workingRack[0][i][1]
                        amount = 2
                        index = 1
                else:
                    color = self.workingRack[0][i][1]
                    amount = 1
                    index = 1
            elif self.workingRack[0][i][0] == self.workingRack[0][i][1]:
                if self.workingRack[0][i][0] == self.workingRack[0][i][2]:
                    if self.workingRack[0][i][0] == self.workingRack[0][i][3]:
                        continue
                    else:
                        color = self.workingRack[0][i][0]
                        amount = 3
                        index = 0
                else:
                    color = self.workingRack[0][i][0]
                    amount = 2
                    index = 0
            else:
                color = self.workingRack[0][i][0]
                amount = 1
                index = 0
            moves = self.getMoves(i, color, amount, com)

            for j in range(len(moves)):
                self.changeRack = copy.deepcopy(self.workingRack[0])
                Tlist = copy.deepcopy(self.workingRack[1])
                Tlist.append(f'{i}>{moves[j]}')
                for k in range(amount):
                    self.changeRack[i][index+k] = 0
                toMove = amount
                for k in range(4):
                    if toMove > 0 and self.changeRack[moves[j]][3-k] == 0:
                        self.changeRack[moves[j]][3 - k] = color
                        toMove -= 1
                self.rackList.append([self.changeRack, Tlist])
                self.win = self.checkForWin()

        self.completed += 1
        print(f'completed: {self.completed} Left: {len(self.rackList)}')

    def checkForWin(self):
        pos = len(self.rackList) - 1
        for k in range(len(self.rackList[pos][0])):
            if self.rackList[pos][0][k][0] == self.rackList[pos][0][k][1] and \
                    self.rackList[pos][0][k][0] == self.rackList[pos][0][k][1] and \
                    self.rackList[pos][0][k][0] == self.rackList[pos][0][k][2] and \
                    self.rackList[pos][0][k][0] == self.rackList[pos][0][k][3]:
                continue
            else:
                return False
        print(self.rackList[pos][0])
        print(self.rackList[pos][1])
        return True

    def run(self):
        while not self.win:
            self.performTurn()

test = Rack([[9, 2, 8, 6],
             [9, 5, 6, 8],
             [4, 2, 2, 4],
             [7, 7, 4, 6],
             [6, 3, 5, 2],
             [7, 3, 5, 3],
             [5, 8, 9, 1],
             [7, 3, 1, 1],
             [8, 1, 9, 4],
             [0, 0, 0, 0],
             [0, 0, 0, 0]])
#test.run()