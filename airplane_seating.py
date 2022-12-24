# number of persons to be seated inside in the plane
passengers = int(input("Number of passengers waiting in the queue: "))
airplane = []

# maximum number of columns that the plane have (each column has its own rows and columns)
total_columns=int(input("\nEnter the number of columns in airplane: "))
for i in range(total_columns):
   column = []
   for j in range(2):
      if j == 0:
        dimension = int(input("\nEnter the number of columns in %x: " %i))
      else: 
        dimension = int(input("Enter the number of rows in %x: " %i))

      # add matrix dimension to column
      column.append(dimension)

   # add the column to airplane seating matrix
   airplane.append(column)

print("\nResultant airplane seating:\n")
print(airplane)
airplaneSeatGrid = airplane

row = 0
seated = 0
fill_temporary = -1

# construct airplane seats grid
def buildPlane(airplaneSeatGrid):
    seats = []
    for seat in airplaneSeatGrid:
        cols = seat[0]
        rows = seat[1]
        addToSeat = []
        for seat in range(rows):
            addToSeat.append([-1]*cols)
        seats.append(addToSeat)
    return seats

# first seat aisle filling start 
def seating_aisle():
    global seated
    fill_temporary = -1
    row = 0
    while seated < passengers and seated != fill_temporary:
        fill_temporary = seated
        for i in range(length):
            if airplaneSeatGrid[i][1] > row:
                if i == 0 and airplaneSeatGrid[i][0] > 1:
                    seated += 1
                    aCol = airplaneSeatGrid[i][0] - 1
                    seats[i][row][aCol] = seated
                    if seated >= passengers:
                        break
                elif i == length - 1 and airplaneSeatGrid[i][0] > 1:
                    seated += 1
                    aCol = 0
                    seats[i][row][aCol] = seated
                    if seated >= passengers:
                        break
                else:
                    seated += 1
                    aCol = 0
                    seats[i][row][aCol] = seated
                    if seated >= passengers:
                        break
                    if airplaneSeatGrid[i][0] > 1:
                        seated += 1
                        aCol = airplaneSeatGrid[i][0] - 1
                        seats[i][row][aCol] = seated
                        if seated >= passengers:
                            break
        row += 1

# second seat window filling start 
def seating_window():
    row = 0
    global seated
    global passengers
    fill_temporary = 0
    while seated < passengers and seated != fill_temporary:
        fill_temporary = seated
        if airplaneSeatGrid[0][1] > row:
            seated += 1
            wind = 0
            seats[0][row][wind] = seated
            if seated >= passengers:
                break
        if airplaneSeatGrid[length-1][1] > row:
            seated += 1
            wind = airplaneSeatGrid[length-1][0] - 1
            seats[length-1][row][wind] = seated
            if seated >= passengers:
                break
        row += 1

# third and last seat middle filling start 
def seating_middle():
    row = 0
    fill_temporary = 0
    global seated
    while seated < passengers and seated != fill_temporary:
        fill_temporary = seated
        for i in range(length):
            if airplaneSeatGrid[i][1] > row:
                if airplaneSeatGrid[i][0] > 2:
                    for col in range(1, airplaneSeatGrid[i][0] - 1):
                        seated += 1
                        seats[i][row][col] = seated
                        if seated >= passengers:
                            break
        row += 1

# printing of airplane seats grid
def printAirplaneSeating(seats):
    bulks = len(str(passengers))
    cols = [x[0] for x in airplaneSeatGrid]
    rows = [x[1] for x in airplaneSeatGrid]

    maxi = max(rows)
    above = True
    for i in range(maxi):
        columnlist = []
        columnlist_1 = []
        for j in range(length):
            row = ' '
            rowl = ' '
            if len(seats[j]) <= i:
                for k in range(cols[j]):
                    row += ' '*bulks
                    rowl += ' '*bulks
                    row += ' '
                    rowl += ' '
            else:
                row = '|'
                rowl = '+'
                for k in seats[j][i]:
                    if k == -1:
                        row += ' '*bulks
                        rowl += '-'*bulks
                        row += '|'
                        rowl += '+'
                    else:
                        row += str(k)+(' '*(bulks - len(str(k))))
                        rowl += '-'*bulks
                        row += '|'
                        rowl += '+'
            
            columnlist.append(row)
            columnlist_1.append(rowl)

        if above:
            print('    '.join(columnlist_1))
            above = False
        print('    '.join(columnlist))
        print('    '.join(columnlist_1))

# Build Airplane
seats = buildPlane(airplaneSeatGrid)

length = len(airplaneSeatGrid)
# Aisle seating
seating_aisle()
# Window seating
seating_window()
# Middle seating
row = 0
fill_temporary = 0
seating_middle()
# Print seats
printAirplaneSeating(seats)