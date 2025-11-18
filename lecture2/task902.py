class Elevator:
    def __init__(self, bottom_floor, top_floor):
        self.bottom_floor = bottom_floor
        self.top_floor = top_floor
        self.current_floor = bottom_floor  # start at bottom

    def floor_up(self):
        if self.current_floor < self.top_floor:
            self.current_floor += 1
            print(f"Elevator is now on floor {self.current_floor}")

    def floor_down(self):
        if self.current_floor > self.bottom_floor:
            self.current_floor -= 1
            print(f"Elevator is now on floor {self.current_floor}")

    def go_to_floor(self, target_floor):
        print(f"\nMoving elevator to floor {target_floor}...")

        if target_floor > self.current_floor:
            while self.current_floor < target_floor:
                self.floor_up()

        elif target_floor < self.current_floor:
            while self.current_floor > target_floor:
                self.floor_down()

        else:
            print("Already on that floor.")

        print(f"Elevator arrived at floor {self.current_floor}\n")


class Building:
    def __init__(self, bottom_floor, top_floor, num_elevators):
        self.elevators = []

        for i in range(num_elevators):
            self.elevators.append(Elevator(bottom_floor, top_floor))

    def run_elevator(self, elevator_number, destination_floor):
        print(f"\nRunning elevator {elevator_number}...")
        chosen_elevator = self.elevators[elevator_number - 1]   # 1-based index
        chosen_elevator.go_to_floor(destination_floor)
def main():
    # Create a building with floors 1 to 10 and 3 elevators
    b = Building(1, 10, 3)

    # Run elevator 1 to floor 7
    b.run_elevator(1, 7)

    # Run elevator 2 to floor 4
    b.run_elevator(2, 4)

    # Run elevator 1 back to floor 1
    b.run_elevator(1, 1)

main()
