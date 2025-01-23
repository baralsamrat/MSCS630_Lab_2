
import argparse
import random
import math

class PagingSimulator:
    def __init__(self, page_size, address_space, physical_memory, allocated_pages=100, random_seed=None):
        self.page_size = page_size
        self.address_space = address_space
        self.physical_memory = physical_memory
        self.allocated_pages = allocated_pages
        self.random_seed = random_seed

        # Derived parameters
        self.num_pages = self.address_space // self.page_size
        self.num_frames = self.physical_memory // self.page_size
        self.page_table = [None] * self.num_pages  # Simulates the page table

        # Set random seed for reproducibility
        if random_seed is not None:
            random.seed(random_seed)

    def allocate_pages(self):
        """Allocate a percentage of pages."""
        num_allocated = int((self.allocated_pages / 100) * self.num_pages)
        allocated_indices = random.sample(range(self.num_pages), num_allocated)

        for page in allocated_indices:
            self.page_table[page] = random.randint(0, self.num_frames - 1)  # Assign a frame to the page

    def translate_address(self, virtual_address):
        """Translate a virtual address to a physical address."""
        page_number = virtual_address // self.page_size
        page_offset = virtual_address % self.page_size

        if page_number >= len(self.page_table) or self.page_table[page_number] is None:
            return "Page fault"  # Simulates a page fault

        frame_number = self.page_table[page_number]
        physical_address = (frame_number * self.page_size) + page_offset
        return physical_address

    def run_simulation(self):
        """Run the paging simulation."""
        self.allocate_pages()
        print(f"Page Table: {self.page_table}")

        print("\nSimulating Address Translations:")
        for _ in range(10):
            virtual_address = random.randint(0, self.address_space - 1)
            result = self.translate_address(virtual_address)
            print(f"Virtual Address: {virtual_address}, Result: {result}")

    def calculate_page_table_size(self):
        """Calculate the size of the page table."""
        entry_size = 4  # Assume 4 bytes per entry
        total_size = len(self.page_table) * entry_size
        return total_size


def main():
    parser = argparse.ArgumentParser(description="Paging Simulator")
    parser.add_argument("-p", "--page_size", type=int, required=True, help="Size of a page in bytes")
    parser.add_argument("-a", "--address_space", type=int, required=True, help="Address space size in bytes")
    parser.add_argument("-P", "--physical_memory", type=int, required=True, help="Physical memory size in bytes")
    parser.add_argument("-u", "--allocated_pages", type=int, default=100, help="Percentage of pages to allocate (default: 100)")
    parser.add_argument("-s", "--seed", type=int, default=None, help="Random seed for deterministic behavior")

    args = parser.parse_args()

    simulator = PagingSimulator(
        page_size=args.page_size,
        address_space=args.address_space,
        physical_memory=args.physical_memory,
        allocated_pages=args.allocated_pages,
        random_seed=args.seed
    )

    print("\nStarting Paging Simulation...")
    simulator.run_simulation()
    print("\nPage Table Size:", simulator.calculate_page_table_size(), "bytes")


if __name__ == "__main__":
    main()
