"""Python serial number generator."""

class SerialGenerator:
    """Machine to create unique incrementing serial numbers.
    
    >>> serial = SerialGenerator(start=100)

    >>> serial.generate()
    100

    >>> serial.generate()
    101

    >>> serial.generate()
    102

    >>> serial.reset()

    >>> serial.generate()
    100
    """

    def __init__(self, start = 0):
        """Make a sequencial number generator, starting from start."""

        self.start = self.next = start

    def __repr__(self):
        """Shows representation."""

        return f"SerialGenerator(start={self.start}, next={self.next})"

    def generate(self):
        """Generates next number in sequence."""

        self.next += 1
        return self.next - 1

    def reset(self):
        """Resets generated number to starting position."""

        self.next = self.start
