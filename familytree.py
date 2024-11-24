class FamilyTree:
    def __init__(self):
        self.family = {}

    def add_person(self, person):
        if person not in self.family:
            self.family[person] = {'parents': set(), 'children': set()}

    def add_relationship(self, parent, *children):
        self.add_person(parent)
        for child in children:
            self.add_person(child)
            self.family[parent]['children'].add(child)
            self.family[child]['parents'].add(parent)

    def get_parents(self, person):
        return self.family.get(person, {}).get('parents', [])

    def get_children(self, person):
        return self.family.get(person, {}).get('children', [])

    def get_siblings(self, person):
        parents = self.get_parents(person)
        siblings = set()
        for parent in parents:
            siblings.update(self.family[parent]['children'])
        siblings.discard(person)
        return siblings

def main():
    tree = FamilyTree()
    while True:
        choice = input("\n1. Add Relationship\n2. Get Parents\n3. Get Children\n4. Get Siblings\n5. Show Tree\n6. Exit\nChoose: ")
        if choice == '1':
            data = input("Enter parent followed by children (e.g., 'parent1 child1 child2 child3'): ")
            relationship = data.split()
            parent = relationship[0]
            children = relationship[1:]
            tree.add_relationship(parent, *children)
        elif choice == '2':
            person = input("Enter name: ")
            print(f"Parents: {', '.join(tree.get_parents(person)) or 'None'}")
        elif choice == '3':
            person = input("Enter name: ")
            print(f"Children: {', '.join(tree.get_children(person)) or 'None'}")
        elif choice == '4':
            person = input("Enter name: ")
            print(f"Siblings: {', '.join(tree.get_siblings(person)) or 'None'}")
        elif choice == '5':
            print(tree.family)
        elif choice == '6':
            break
        else:
            print("Invalid choice.")

if __name__ == "__main__":
    main()