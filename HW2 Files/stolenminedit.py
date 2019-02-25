import sys

class MinEditDistanceChart:
    def __init__(self, sourceWord, targetWord, verbose=True):
        self.sourceWord = sourceWord
        self.targetWord = targetWord
        self.nRows = len(self.sourceWord) + 1
        self.nColumns = len(self.targetWord) + 1
        self.chart = []
        for i in range(self.nRows):
            row = []
            for j in range(self.nColumns):
                row.append(-1)
            row[0] = i
            self.chart.append(row)
        for j in range(self.nColumns):
            self.chart[0][j] = j
        # This boolean variable determines whether the chart
        # is printed at each stage of its construction.
        self.verbose = verbose

    def __str__(self):
        s = '\n    '
        for k in range(self.nColumns):
            s += '  %2d' % k
        s += '\n'
        s += '       #'
        for ch in self.targetWord:
            s += '   ' + ch
        s += '\n'
        for row in range(self.nRows):
            if row == 0:
                s += '%2d #' % row
            else:
                s += '%2d %s' % (row, self.sourceWord[row - 1])
            for col in range(self.nColumns):
                s += '  %2d' % self.chart[row][col]
            s += '\n'
        s += '\n'
        return s

    def getDistance(self, i, j):
        if self.chart[i][j] != -1:
            return self.chart[i][j]

        if self.chart[i-1][j] != -1:
            down = self.chart[i-1][j] + 1
        else:
            down = self.getDistance(i - 1, j) + 1

        if self.chart[i][j-1] != -1:
            left = self.chart[i][j-1] + 1
        else:
            left = self.getDistance(i, j - 1) + 1

        if self.chart[i-1][j-1] != -1:
            diag = self.chart[i-1][j-1]
        else:
            diag = self.getDistance(i - 1, j - 1)
        if self.sourceWord[i - 1] != self.targetWord[j - 1]:
            diag += 2

        self.chart[i][j] = min(down, left, diag)
        if self.verbose:
            print self
        return self.chart[i][j]

    def printTransformation(self):
        '''This method prints a sequence of steps required to
        transform self.sourceWord into self.targetWord at the
        minimum cost.  For example, if the words are "dog" and
        "pig", this method will print:

            dog, pog, pig

        or something similar.'''
        pass

    def printChartWithPath(self):
        '''This method prints the chart (see the __str__ method
        for an approach to doing this) with an asterisk next
        to each cell of the chart that lies along a path of minimum
        edit distance, from the upper left corner of the chart
        to the lower right.  For example, if the words are "EMU"
        and "elms", the method could print out this:

                 0   1   2   3   4
                 #   E   L   M   S
           0 #   0*  1   2   3   4
           1 E   1   0*  1*  2   3
           2 M   2   1   2   1*  2*
           3 U   3   2   3   2   3*

        which corresponds to "Leave the E, insert an L, leave the M,
        insert an S, and delete the U."
        '''
        pass


if __name__ == '__main__':
    if len(sys.argv) != 3:
        sys.stderr.write('Usage: %s sourceword targetword\n' % sys.argv[0])
        sys.exit(1)

    sourceWord = sys.argv[1]
    targetWord = sys.argv[2]

    chart = MinEditDistanceChart(sourceWord, targetWord)
    print chart
    
    d = chart.getDistance(len(sourceWord), len(targetWord))
    print 'The minimum edit distance between %s and %s is %d.'\
                % (sourceWord, targetWord, d)