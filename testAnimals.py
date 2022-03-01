import animals

myMammals = animals.Mammals()
myMammals.printMembers()

myBird = animals.Birds()
myBird.printMembers()

harmless_birds = animals.harmless.Birds()
harmless_birds.printMembers()

dangerous_fish = animals.dangerous.Fish()
dangerous_fish.printMembers()
