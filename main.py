#Y1t1 coursework main.py

#test change for git commit command

class Party():
    def __init__(self, MP, constit):
        self.MP=MP
        self.constit=constit
    
    def MPsearch(MP):
        pass
    def constitSearch(constit):
        pass

class Constituancy():
    def __init__(self, MP, constit):
        super().__init__(MP, constit)

while True:
    mmInp=input("""Select one of the following
    1. Candidate party 
    2. Candidate name
    3. Parliamentary Seat (name) 
    4. Total registered voters in the seat 
    5. Total of votes cast 
    6. Votes cast for the candidate 
    7. Votes for a given party received as a percentage of total votes cast
Enter selection: """)
    if mmInp=='1' or mmInp=='2':
        print("candidate query")
    elif mmInp=='3':
        print("parlimentary seat")
    elif mmInp=="4" or mmInp=="5" or mmInp=="6" or mmInp=="7":
        print("Votes query")
    else:
        print("\nPlease enter the number of the selection you wish to make\n")