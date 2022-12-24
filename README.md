# VoloPay

## Airplane Seating Algorithm

### Write a program that helps seat audiences in a flight based on the following input and rules.

### Rules for seating
1. Always seat passengers starting from the front row to back, starting from the left to
the right
2. Fill aisle seats first followed by window seats followed by center seats (any order in
center seats)

### Input to the program will be
1. A 2D array that represents the columns and rows - Ex. `[[3,4], [4,5], [2,3], [3,4]]`
2. Number of passengers waiting in the queue.

### Example
- Given - A 2D array that represents the columns and rows - `[[3,2], [4,3], [2,3], [3,4]]`

### Test cases:
1. Number of passengers are less than number of seats available
    - Passengers: 15
    - Columns and Rows: [[2,1], [3,2]]
 
2. Number of passengers are more than number of seats available
    - Passengers: 20
    - Columns and Rows: [[3,3], [3,3], [3,3]]
    
### Output screenshots:

1. <p align="center"><img align="center" height="250em" src="https://user-images.githubusercontent.com/60578902/209428067-425f3563-d87b-4216-b041-37f17d593c5c.jpg" /></p>
2. <p align="center"><img align="center" height="250em" src="https://user-images.githubusercontent.com/60578902/209428069-dfc86149-d2f2-41e5-9680-fa3768d6ab9a.jpg" /></p>
3. <p align="center"><img align="center" height="250em" src="https://user-images.githubusercontent.com/60578902/209428071-8f2ec7ee-191c-4d57-a8ef-33641f989fb1.jpg" /></p>
