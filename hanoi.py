class Hanoi:
    def __init__(self, n):
        self.total = n
        self.a = [ n - i for i in range(n) ]
        self.b = []
        self.c = []

    def play(self):
        alg = self._rec(self.total).split()
        print('\nSteps to finish: ' + str(len(alg)))
        print('Note, that steps number is 2^' + str(self.total) + ' - 1')
        print('\nTo make a step, click Enter')
        case = {
            'ab': (self.a, self.b),
            'bc': (self.b, self.c),
            'ca': (self.c, self.a),
            'ac': (self.a, self.c),
            'cb': (self.c, self.b),
            'ba': (self.b, self.a)
        }
        for i in alg:
            self.move(case[i][0], case[i][1])

    def move(self, f, t):
        input()
        t.append(f.pop(-1))
        self.show()

    def show(self):
        print('.' + '_' * 26 + '.\n|' + ' ' * 26 + '|')
        self._rows()
        print("""|                          |
| ------------------------ |
|                          |
|    ##     ####    ####   |
|   #  #    #  #    #      |
|   ####    ###     #      |
|   #  #    #  #    #      |
|   #  #    ####    ####   |
|__________________________|""")


    def _rec(self, n):
        if n == 1:
            return 'ac'
        return self._rec(n-1).replace('c', 'B').replace('b', 'C').lower() + ' ac ' + self._rec(n-1).replace('a', 'B').replace('b', 'A').lower()

    def _rows(self):
        max_length = max([len(self.a), len(self.b), len(self.c)])
        for i in range(max_length):
            row = ''
            if len(self.a) >= max_length - i:
                block = str(self.a[-1 + (max_length - i - len(self.a))])
                row += ' # ' + '0' * (len(block)<=1) + block + ' # '
            else:
                row += ' '*8
            if len(self.b) >= max_length - i:
                block = str(self.b[-1 + (max_length - i - len(self.b))])
                row += ' # ' + '0' * (len(block)<=1) + block + ' # '
            else:
                row += ' '*8
            if len(self.c) >= max_length - i:
                block = str(self.c[-1 + (max_length - i - len(self.c))])
                row += ' # ' + '0' * (len(block)<=1) + block + ' # '
            else:
                row += ' '*8

            row += ' ' * (24 - len(row))

            print('| ' + row + ' |')


n = int(input('- How many blocks?\n- '))

hanoi = Hanoi(n)

hanoi.show()

hanoi.play()
