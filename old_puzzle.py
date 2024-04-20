"""https://github.com/IvanShynkarenko/puzzle.py"""
def validate_board(board: list)->bool:
    '''Connect all funcion and return bool
    >>> validate_board([\
"**** ****",\
"***1 ****",\
"**  3****",\
"* 4 1****",\
"     9 5 ",\
" 6  83  *",\
"3   1  **",\
"  8  2***",\
"  2  ****"\
])
    False
    '''
    final = []
    def check_line(board):
        '''Check if in line are same numbers and return bool
        >>> check_line([\
"**** ****",\
"***1 ****",\
"**  3****",\
"* 4 1****",\
"     9 5 ",\
" 6  83  *",\
"3   1  **",\
"  8  2***",\
"  2  ****"\
])
        True
        '''
        res = []
        numbers = ['1','2','3','4','5','6','7','8','9','0']
        for line in board:
            checker = []
            for el in line:
                if el in numbers:
                    checker+=[el]
                else:
                    continue
            res.append(len(checker) == len(set(checker)))
        return all(res)

    def check_column(board):
        '''Check if in column are same numbers and return bool
        >>> check_column([\
"**** ****",\
"***1 ****",\
"**  3****",\
"* 4 1****",\
"     9 5 ",\
" 6  83  *",\
"3   1  **",\
"  8  2***",\
"  2  ****"\
])
        False
        '''
        res = []
        numbers = ['1','2','3','4','5','6','7','8','9','0']
        for i in range(9):
            checker = []
            for line in board:
                lst = []
                for el in line:
                    lst+=[el]
                if lst[i] in numbers:
                    checker+=lst[i]
            res.append(len(checker) == len(set(checker)))
        return all(res)
    def check_color(board):
        '''Check if in colors are same numbers and return bool
        >>> check_color([\
"**** ****",\
"***1 ****",\
"**  3****",\
"* 4 1****",\
"     9 5 ",\
" 6  83  *",\
"3   1  **",\
"  8  2***",\
"  2  ****"\
])
        True
        '''
        result = []
        for i in range(-1,-6,-1):
            lst = []
            lst+=[board[i][(-1)*i-1]]

            for j in range(1,5):
                lst+=[board[i][(-1)*i-1+j]]
            for j in range(1,5):
                lst+=[board[i-j][(-1)*i-1]]
            result+=[lst]
        res = check_line(result)
        return res
    final.extend([check_column(board),check_line(board),check_color(board)])
    return all(final)
