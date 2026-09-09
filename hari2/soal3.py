class Thing:

    pass

class Agent(Thing):

    def __init__(self, program=None):
        self.location = 1
        if program:
            self.program = program

class People(Thing):

    pass


class BlindAlley(Thing):

    pass

class CarAgent(Agent):

    def __init__(self, program=None):
        super().__init__(program)
        self.location = 0

    def brake(self, thing):
        if isinstance(thing, People):
            print(f"Car Braked at location {self.location}")
            self.location += 0
            return True
        return False

    def reverse(self, thing):
        if isinstance(thing, BlindAlley):
            print(f"Car Reversed at location {self.location}")
            self.location -= 1 
            return True
        return False

    def accelerate(self):
        self.location += 1
        print(f"Car Accelerated to location {self.location}")


def program(percepts):
    for p in percepts:
        if isinstance(p, People):
            return "brake"
        elif isinstance(p, BlindAlley):
            return "reverse"
    return "accelerate"


def main():
    car = CarAgent(program)

    percepts = [
        [], 
        [], 
        [People()],  
        [BlindAlley()],  
        [],  
        [People()],
        [BlindAlley()],
        [],
        [],
        [],
        [],
        [People()],
    ]

    for step, percept in enumerate(percepts, 1):
        action = car.program(percept)

        print(f"Step {step}:")
        if action == "brake":
            car.brake(percept[0])
        elif action == "reverse":
            car.reverse(percept[0])
        elif action == "accelerate":
            car.accelerate()
        print("-" * 30)

main()