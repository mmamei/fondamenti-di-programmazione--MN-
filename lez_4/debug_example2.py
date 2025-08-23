# nested_loops_buggy.py

"""
Goal: Compute row averages and column sums of a 5x5 grid.
"""

def make_grid():
    # Simple 5x5 grid with distinct values per row for easier inspection
    return [
        [1,  2,  3,  4,  5],
        [6,  7,  8,  9, 10],
        [11, 12, 13, 14, 15],
        [16, 17, 18, 19, 20],
        [21, 22, 23, 24, 25],
    ]

def row_averages(grid):
    avgs = []
    for r in range(len(grid)):
        total = 0
        for c in range(len(grid[0])):
            total += grid[r][c]
        avgs.append(total / len(grid[0]))
    return avgs

def col_sums(grid):
    n_rows = len(grid)
    n_cols = len(grid[0])
    sums = [0] * n_cols
    for c in range(n_cols):
        total = 0
        for c in range(n_rows):          
            total += grid[c][c]          
        sums[c] = total                  
    return sums

def main():
    grid = make_grid()

    print("Grid:")
    for row in grid:
        print(row)

    avgs = row_averages(grid)
    sums = col_sums(grid)

    print("\nRow averages:")
    for i, a in enumerate(avgs):
        print(f"Row {i}: {a:.2f}")

    print("\nColumn sums:")
    for j, s in enumerate(sums):
        print(f"Col {j}: {s}")

if __name__ == "__main__":
    main()
