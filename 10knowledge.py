class KnowledgeBase:
    def __init__(self):
        self.likes = {}
        self.facts = set()

    def add_like(self, person1, person2):
        if person1 not in self.likes:
            self.likes[person1] = set()
        self.likes[person1].add(person2)

    def likes_person(self, person1, person2):
        return person2 in self.likes.get(person1, set())

    def query_likes(self, person):
        results = []
        for liked_person in self.likes.get(person, set()):
            results.append(f'likes({person}, {liked_person})')
        return results

if __name__ == "__main__":
    kb = KnowledgeBase()
    n = int(input("Enter the number of likes to add: "))
    for _ in range(n):
        person1, person2 = input("Enter a like (person1 person2): ").split()
        kb.add_like(person1, person2)

    query_person = input("Enter the person to query likes for: ")
    results = kb.query_likes(query_person)
    for result in results:
        print(result)
