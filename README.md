# Pit Analyzer

This program processes terrain depth measurements along a straight channel, identifying pits (depressions) and calculating their characteristics.

## Functionality

1. **Function 1** – Loads data from the `depth.txt` file and stores the depth values per meter.
2. **Function 2** – Accepts a user-specified distance and prints the depth at that location.
3. **Function 3** – Calculates and prints the percentage of the terrain that remained untouched (depth = 0).
4. **Function 4** – Writes all identified pits into the `pits.txt` file, each on a separate line.
5. **Function 5** – Prints the number of pits found in the terrain.
6. **Function 6** – For the pit at the user-specified location:
   - a) Prints the start and end position.
   - b) Checks whether the pit deepens continuously from both directions.
   - c) Prints the maximum depth.
   - d) Calculates and prints the volume (cross section = 10 m).
   - e) Calculates and prints the water-holding capacity (if at least 1 meter deeper than the edge).

## Input

- `depth.txt`: A text file with one integer per line indicating the depth (in meters) at each meter along the channel.

## Output

- Console output for each function result.
- `pits.txt`: Contains each identified pit as a line of space-separated depth values.

## Output files

After running the program, it generates a `pits.txt` file containing pit depth values.
This file is not included in the repository. It is automatically created during execution.

---
Developed by Áron Domonkos, 2023.
