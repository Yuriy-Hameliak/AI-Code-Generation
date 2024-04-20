def validate_board(board: list) -> bool:
    """
    Перевіряє, чи готове ігрове поле логічної головоломки до початку гри.

    Args:
        board (list): Список рядків ігрового поля.

    Returns:
        bool: True, якщо ігрове поле готове, False - якщо ні.
    """

    def check_line(line: str) -> bool:
        """
        Перевіряє, чи немає однакових цифр у рядку.

        Args:
            line (str): Рядок ігрового поля.

        Returns:
            bool: True, якщо немає однакових цифр, False - якщо є.
        """
        numbers = set()
        for char in line:
            if char.isdigit() and char in numbers:
                return False
            numbers.add(char)
        return True

    def check_column(board: list) -> bool:
        """
        Перевіряє, чи немає однакових цифр у стовпчику.

        Args:
            board (list): Список рядків ігрового поля.

        Returns:
            bool: True, якщо немає однакових цифр, False - якщо є.
        """
        for col in range(9):
            numbers = set()
            for row in board:
                char = row[col]
                if char.isdigit() and char in numbers:
                    return False
                numbers.add(char)
        return True

    def check_square(board: list) -> bool:
        """
        Перевіряє, чи немає однакових цифр у квадраті.

        Args:
            board (list): Список рядків ігрового поля.

        Returns:
            bool: True, якщо немає однакових цифр, False - якщо є.
        """
        for row_start in range(0, 9, 3):
            for col_start in range(0, 9, 3):
                numbers = set()
                for row in range(row_start, row_start + 3):
                    for col in range(col_start, col_start + 3):
                        char = board[row][col]
                        if char.isdigit() and char in numbers:
                            return False
                        numbers.add(char)
        return True

    # Перевірка рядків, стовпчиків та квадратів
    return all(check_line(row) for row in board) and check_column(board) and check_square(board)

