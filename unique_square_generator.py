import random


class UniqueSquarePatternGenerator:
    def __init__(self, min_base: int, max_base: int):
        """
        Initialize the generator with a range of base values.
        
        :param min_base: Minimum base value.
        :param max_base: Maximum base value.
        """
        self.min_base = min_base
        self.max_base = max_base
        self.generated_numbers = set()  # To store non-repeating numbers
        self.total_possible = max_base - min_base + 1

    def generate_unique_square(self) -> int:
        """
        Generate a unique random number in the form of base^2.
        
        :return: A unique random number.
        :raises ValueError: If all unique numbers have been generated.
        """
        if len(self.generated_numbers) >= self.total_possible:
            raise ValueError("All unique square numbers in the range have been generated.")

        while True:
            base = random.randint(self.min_base, self.max_base)
            if base not in self.generated_numbers:
                self.generated_numbers.add(base)
                return base ** 2


# Example usage
if __name__ == "__main__":
    min_base = 10  # Minimum base for square generation
    max_base = 50  # Maximum base for square generation
    generator = UniqueSquarePatternGenerator(min_base, max_base)

    print("Generating unique random numbers based on square patterns:")
    try:
        for _ in range(10):  # Generate 10 unique numbers
            print(generator.generate_unique_square())
    except ValueError as e:
        print(f"Error: {e}")
