
"""Calculate daily pay for bicycle and motorbike delivery riders."""


class Rider:
    """Represent a delivery rider."""

    def __init__(self, name, deliveries):
        """Initialize the rider's name and delivery count."""
        self.name = name
        self.deliveries = deliveries

    def pay(self):
        """Return the rider's daily pay."""
        raise NotImplementedError("Subclasses must implement pay()")


class BicycleRider(Rider):
    """Represent a bicycle delivery rider."""

    def pay(self):
        """Calculate pay at 100 yen per delivery."""
        return self.deliveries * 100


class MotorbikeRider(Rider):
    """Represent a motorbike delivery rider."""

    def pay(self):
        """Calculate pay after deducting fuel costs."""
        return (self.deliveries * 150) - (self.deliveries * 30)


def main():
    """Collect rider details and display their daily pay."""
    riders = []

    while True:
        rider_type = input(
            "\nEnter rider type (bicycle/motorbike) or 'done' to finish: "
        ).strip().lower()

        if rider_type == "done":
            break

        if rider_type not in ("bicycle", "motorbike"):
            print("Invalid rider type. Please try again.")
            continue

        name = input("Enter rider name: ").strip()

        try:
            deliveries = int(input("Enter number of deliveries: "))

            if deliveries < 0:
                print("Deliveries cannot be negative.")
                continue

        except ValueError:
            print("Please enter a valid whole number.")
            continue

        if rider_type == "bicycle":
            rider = BicycleRider(name, deliveries)
        else:
            rider = MotorbikeRider(name, deliveries)

        riders.append(rider)

        print(f"Rider: {rider.name}")
        print(f"Daily pay: ¥{rider.pay()}")

    print("\n--- Daily Payment Summary ---")

    if not riders:
        print("No riders were entered.")
    else:
        for rider in riders:
            print(f"{rider.name}: ¥{rider.pay()}")

    print("Program finished.")


if __name__ == "__main__":
    main()
