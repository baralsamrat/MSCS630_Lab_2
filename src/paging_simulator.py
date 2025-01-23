
import argparse
import random
import math

class PagingSimulator:
    def __init__(self, page_size, address_space, physical_memory, allocated_pages=100, random_seed=None, verbose=False):
        self.page_size = page_size
        self.address_space = address_space
        self.physical_memory = physical_memory
        self.allocated_pages = allocated_pages
        self.random_seed = random_seed
        self.verbose = verbose

        # Derived parameters
        self.num_pages = self.address_space // self.page_size
        self.num_frames = self.physical_memory // self.page_size
        self.page_table = [None] * self.num_pages

        # Set random seed for reproducibility
        if random_seed is not None:
            random.seed(random_seed)

    def allocate_pages(self):
        """Allocate a percentage of pages."""
        num_allocated = int((self.allocated_pages / 100) * self.num_pages)
        allocated_indices = random.sample(range(self.num_pages), num_allocated)

        for page in allocated_indices:
            self.page_table[page] = random.randint(0, self.num_frames - 1)

    def translate_address(self, virtual_address):
        """Translate a virtual address to a physical address."""
        page_number = virtual_address // self.page_size
        page_offset = virtual_address % self.page_size

        if page_number >= len(self.page_table) or self.page_table[page_number] is None:
            return "Page fault"

        frame_number = self.page_table[page_number]
        physical_address = (frame_number * self.page_size) + page_offset
        return physical_address

    def run_simulation(self):
        """Run the paging simulation."""
        self.allocate_pages()
        if self.verbose:
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

    def analyze_page_table_size(self):
        """Analyze and print the page table size."""
        size = self.calculate_page_table_size()
        print(f"Page Table Size: {size} bytes")

    def explore_page_allocation(self):
        """Explore and print behavior based on page allocation."""
        self.allocate_pages()
        allocated = sum(1 for entry in self.page_table if entry is not None)
        print(f"Allocated Pages: {allocated}/{len(self.page_table)}")
        self.analyze_page_table_size()


def run_predefined_tasks():
    tasks = [
        {"description": "Task 1: Page Table Size Analysis", "configs": [
            {"page_size": 1024, "address_space": 1048576, "physical_memory": 536870912, "allocated_pages": 100},
            {"page_size": 1024, "address_space": 2097152, "physical_memory": 536870912, "allocated_pages": 100},
            {"page_size": 1024, "address_space": 4194304, "physical_memory": 536870912, "allocated_pages": 100},
        ]},
        {"description": "Task 2: Page Allocation Experiment", "configs": [
            {"page_size": 1024, "address_space": 16384, "physical_memory": 32768, "allocated_pages": 0},
            {"page_size": 1024, "address_space": 16384, "physical_memory": 32768, "allocated_pages": 25},
            {"page_size": 1024, "address_space": 16384, "physical_memory": 32768, "allocated_pages": 50},
            {"page_size": 1024, "address_space": 16384, "physical_memory": 32768, "allocated_pages": 100},
        ]},
        {"description": "Task 3: Random Seed Experiment", "configs": [
            {"page_size": 8, "address_space": 32, "physical_memory": 1024, "allocated_pages": 100, "random_seed": 1},
            {"page_size": 8192, "address_space": 32768, "physical_memory": 1048576, "allocated_pages": 100, "random_seed": 2},
            {"page_size": 1048576, "address_space": 268435456, "physical_memory": 536870912, "allocated_pages": 100, "random_seed": 3},
        ]},
    ]

    for task in tasks:
        print(f"\n=== {task['description']} ===")
        for config in task["configs"]:
            print(f"\nConfiguration: {config}")
            simulator = PagingSimulator(
                page_size=config.get("page_size"),
                address_space=config.get("address_space"),
                physical_memory=config.get("physical_memory"),
                allocated_pages=config.get("allocated_pages", 100),
                random_seed=config.get("random_seed"),
                verbose=True
            )
            simulator.analyze_page_table_size()
            simulator.explore_page_allocation()


def main():
    parser = argparse.ArgumentParser(description="Paging Simulator")
    parser.add_argument("-p", "--page_size", type=int, help="Size of a page in bytes")
    parser.add_argument("-a", "--address_space", type=int, help="Address space size in bytes")
    parser.add_argument("-P", "--physical_memory", type=int, help="Physical memory size in bytes")
    parser.add_argument("-u", "--allocated_pages", type=int, default=100, help="Percentage of pages to allocate")
    parser.add_argument("-s", "--seed", type=int, default=None, help="Random seed for deterministic behavior")
    parser.add_argument("-v", "--verbose", action="store_true", help="Enable verbose output")
    parser.add_argument("--run-predefined", action="store_true", help="Run predefined tasks for lab analysis")

    args = parser.parse_args()

    if args.run_predefined:
        run_predefined_tasks()
    else:
        if args.page_size and args.address_space and args.physical_memory:
            simulator = PagingSimulator(
                page_size=args.page_size,
                address_space=args.address_space,
                physical_memory=args.physical_memory,
                allocated_pages=args.allocated_pages,
                random_seed=args.seed,
                verbose=args.verbose
            )

            print("\nRunning Analysis...")

            simulator.analyze_page_table_size()
            simulator.explore_page_allocation()
            simulator.run_simulation()
        else:
            print("Error: Missing required arguments. Use -p, -a, -P to specify page size, address space, and physical memory.")

if __name__ == "__main__":
    main()
