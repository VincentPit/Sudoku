class SudokuSolver:
    def __init__(self, puzzle):
        self.puzzle = puzzle

    def is_valid(self, row, col, num):
        # Check if the number is already in the row
        if num in self.puzzle[row]:
            return False

        # Check if the number is already in the column
        for i in range(9):
            if self.puzzle[i][col] == num:
                return False

        # Check if the number is already in the 3x3 box
        start_row, start_col = 3 * (row // 3), 3 * (col // 3)
        for i in range(3):
            for j in range(3):
                if self.puzzle[i + start_row][j + start_col] == num:
                    return False

        # Check if the number is already in the 45 diagonal
        if row == col:
            for i in range(9):
                if self.puzzle[i][i] == num:
                    return False
        # Check if the number is already in the 135 diagonal
       
        if row + col == 8:
            for i in range(9):
                if self.puzzle[i][8 - i] == num:
                    return False

        return True

    def solve(self):
        empty_cell = self.find_empty()
        if not empty_cell:
            return True  # Puzzle solved successfully
        else:
            row, col = empty_cell

        for num in range(1, 10):
            if self.is_valid(row, col, num):
                self.puzzle[row][col] = num
                if self.solve():
                    return True
                self.puzzle[row][col] = 0  # Reset if solution failed
        return False  # No solution found

    def find_empty(self):
        for i in range(9):
            for j in range(9):
                if self.puzzle[i][j] == 0:
                    return i, j
        return None

    def print_solution(self):
        for row in self.puzzle:
            print(" ".join(map(str, row)))


#checked
def read_sudoku_from_file(file_path):
    puzzle = []
    with open(file_path, 'r') as file:
        for line in file:
            puzzle.append(list(map(int, line.strip().split())))
    return puzzle


if __name__ == "__main__":
    puzzle = read_sudoku_from_file("Sample_Input.txt")
    solver = SudokuSolver(puzzle)
    if solver.solve():
        solver.print_solution()
    else:
        print("No solution exists.")
