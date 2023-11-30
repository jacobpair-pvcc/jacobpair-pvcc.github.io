# Name: Jacob Pair
# Prog Purpose: This program demonstartes how to manipulate a list, including:
#   finding number of items in the list, sorting the list, adding/removing items,
#   copying a list of items into another list, and changing the data in the list.

dogs = ["Sadie", "Molly", "Ella", "Milo", "Buddy", "Rocky", "Annebelle",
        "Gonzo", "Sweetie-Pie", "Diego"]
dogs2 = []

def main():
    how_many = len(dogs)
    print("\nNumber of dogs in the list: " + str(how_many))
    print("\nOriginal list of dog names:")
    print(dogs)
    
    dogs.reverse()
    print("\nList from last to first:")
    print(dogs)
    
    dogs.sort()
    print("\nAlphabetized list:")
    print(dogs)
    
    dogs.sort(reverse = True)
    print("\nList in reverse alphabetized order:")
    print(dogs)
    
