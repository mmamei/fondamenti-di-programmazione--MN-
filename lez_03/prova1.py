import csv
from collections import defaultdict

filename = "lez_2/nfl_offensive_stats.csv"

# Dictionary to store total passing yards per QB
yards_per_qb = defaultdict(int)

with open(filename, mode='r', newline='', encoding='utf-8') as file:
    reader = csv.reader(file)
    
    # Skip header row
    header = next(reader)
    
    for row in reader:
        position = row[2].strip()   # Column 3: Position
        player_name = row[3].strip() # Column 4: Player name
        passing_yards = row[7].strip() # Column 8: Passing yards
        
        # Consider only QBs and valid yard values
        if position == "QB" and passing_yards.isdigit():
            yards_per_qb[player_name] += int(passing_yards)

# Sort by total passing yards (descending order)
sorted_qbs = sorted(yards_per_qb.items(), key=lambda x: x[1], reverse=True)

# Print the result
print("Total passing yards per QB (sorted):")
for player, total_yards in sorted_qbs:
    print(f"{player}: {total_yards}")
