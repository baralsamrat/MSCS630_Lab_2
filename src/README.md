
# Paging Simulator

## Overview

The Paging Simulator is a Python-based tool designed to simulate virtual memory management using paging mechanisms. It allows users to explore the behavior of page tables under various configurations of address space size, page size, physical memory size, and percentage of page allocation. This tool is perfect for educational purposes and experiments in operating systems concepts.

---

## Features

- Simulates page table allocation and address translation.
- Handles varying parameters for address space, page size, and physical memory.
- Provides detailed outputs for analysis of paging behavior.
- Simulates page faults for unallocated or invalid pages.

---

## Requirements

- Python 3.6 or higher

To install Python, visit [Python's official website](https://www.python.org/).

---

## Usage

### 1. Run the Simulator
To run the simulator, execute the following command in your terminal:

```bash
python paging_simulator.py -p <PAGE_SIZE> -a <ADDRESS_SPACE> -P <PHYSICAL_MEMORY> [-u <ALLOCATED_PAGES>] [-s <RANDOM_SEED>]
```

### 2. Command-Line Arguments

| Argument             | Description                                      |
|----------------------|--------------------------------------------------|
| `-p`, `--page_size`  | Size of a page in bytes (required).              |
| `-a`, `--address_space` | Address space size in bytes (required).         |
| `-P`, `--physical_memory` | Physical memory size in bytes (required).      |
| `-u`, `--allocated_pages` | Percentage of pages to allocate (default: 100). |
| `-s`, `--seed`       | Random seed for deterministic behavior (optional). |

---

## Example Usage

### Example 1: Basic Simulation
```bash
python paging_simulator.py -p 1024 -a 1048576 -P 524288
```
**Output**:
```
Starting Paging Simulation...
Page Table: [23, None, 17, None, 9, ...]
Simulating Address Translations:
Virtual Address: 12345, Result: Page fault
Virtual Address: 67890, Result: 45218
...
Page Table Size: 4096 bytes
```

### Example 2: Partial Page Allocation
```bash
python paging_simulator.py -p 1024 -a 1048576 -P 524288 -u 50
```
**Output**:
```
Starting Paging Simulation...
Page Table: [None, 141, None, None, 126, 332, None, None, None, None, None, None, None, 260, None, 60, 322, None, 65, None, None, 410, 161, 469, 248, None, 447, 457, None, None, 149, 131, None, 135, None, None, 480, 318, None, None, 41, None, 486, None, None, None, None, 80, None, 197, None, None, 316, 239, None, 374, 126, 237, None, 112, 300, 73, None, 370, 191, None, None, 504, None, 346, 117, None, None, 19, None, None, None, 102, 302, None, 3, 353, None, 296, 123, None, 10, 130, None, 280, None, None, None, None, None, None, 467, 430, 397, 55, 149, 195, None, 90, 149, None, None, 36, 285, 451, 477, None, None, None, 346, None, None, 396, 469, None, None, 343, None, 484, 327, None, 195, None, 367, 151, None, None, 41, 83, 436, None, 505, None, None, 117, None, 506, None, 134, None, 345, None, 510, 226, 49, None, None, 359, 221, 225, 58, 54, 0, None, None, None, None, None, 81, 376, None, 58, None, None, None, None, 339, None, None, None, None, 196, None, None, 145, 236, 229, None, 269, 502, 502, 100, 424, 456, 347, 365, 253, None, None, 422, 225, None, 466, 503, None, 301, 450, None, None, 425, None, None, None, None, None, 492, None, 362, None, 416, None, 3, None, 216, 263, None, 241, None, None, 147, None, None, None, None, None, 436, None, None, None, None, 413, None, 11, 249, None, 175, None, 140, 212, None, None, 389, None, 23, None, None, 271, 364, 158, 147, None, 338, None, 299, 370, None, 435, None, None, 401, 416, None, None, None, 293, None, 224, None, None, None, 357, 282, None, None, None, None, None, 386, None, 475, 180, None, None, None, 159, 362, None, None, None, 93, 477, 168, None, 235, 179, None, 40, None, None, 490, None, 145, 459, None, None, 494, None, 506, None, 113, 240, 205, None, 141, None, None, 367, None, None, None, 162, None, 105, 289, 450, 266, None, None, None, 431, 358, None, 175, 492, 107, None, 18, 425, 498, 179, None, 81, None, None, None, None, None, 275, None, None, None, 46, None, None, 453, 285, 351, 19, 376, None, 122, None, None, 297, None, None, None, None, None, 232, None, 444, 47, 213, 407, None, 43, 384, None, 9, None, None, None, None, 213, None, None, 508, 148, None, 102, None, 20, None, 126, None, None, 62, None, 250, None, 242, None, 455, 426, None, None, None, None, 119, 36, 493, 177, None, 258, 281, None, None, 210, 426, 2, None, None, None, None, 491, None, 293, 328, None, None, 40, 341, None, 311, None, 58, 498, 200, None, 170, 358, None, None, 475, 409, None, None, 475, None, 52, None, 474, 131, None, 137, 56, None, 296, 168, 225, 477, 54, 260, 129, 367, 326, 31, None, None, None, None, 456, None, None, None, None, 232, 442, 9, None, 278, 281, None, 42, None, 288, 132, 384, None, 141, 460, None, 237, 362, None, None, None, None, 74, 465, 298, None, None, 82, None, 388, 178, None, None, None, None, None, None, None, None, None, None, None, 408, 153, None, None, None, None, 29, 395, 295, None, None, 181, None, 371, None, 226, 304, 312, 364, None, None, None, None, 348, None, 16, None, None, None, 69, 33, 215, 133, 257, 343, None, None, 370, 352, None, None, None, 157, None, 117, 465, None, 507, None, 155, None, None, None, None, None, None, 142, 4, None, 215, None, None, None, 88, 407, None, 380, None, None, None, 366, 190, None, None, 272, 69, None, None, 144, None, None, 454, None, 20, 176, 29, 41, 292, 232, None, None, None, None, None, 353, None, None, None, 359, 456, None, 187, None, None, 215, 23, 441, 392, 119, None, 64, None, 180, None, 339, 205, None, None, 121, None, None, None, 267, None, 425, None, 28, 127, 237, 29, 169, None, None, 336, None, 177, None, None, None, None, 332, None, None, 11, None, None, None, None, None, None, 361, None, None, 155, 345, None, 149, None, None, 316, 419, 111, 343, None, None, None, 158, 179, None, None, 404, None, None, None, 96, 392, None, None, 179, 197, None, 463, 300, None, None, 7, 458, 348, 129, None, 185, 431, 487, None, 231, 259, None, None, None, 26, 333, None, None, 493, 304, 396, None, 209, None, 497, 171, 360, None, None, None, None, 316, None, 209, 199, None, 24, None, 121, None, 352, 283, 71, 367, None, None, None, 129, 325, 302, None, None, 244, None, 363, None, None, 135, 31, None, 368, None, 383, 394, 344, None, None, 154, None, 172, None, 232, None, None, 230, 451, None, None, None, 384, None, 432, None, None, 377, 406, None, None, None, 439, None, None, 88, None, None, None, 117, 166, 180, 365, 245, 217, 38, 21, None, 132, None, 447, None, None, None, None, None, None, None, 505, None, None, None, 471, None, None, 30, 397, 364, None, 396, 225, 196, None, 32, 14, None, 379, None, 470, None, None, 433, 418, None, 393, 111, None, 175, None, None, 393, 43, 502, 467, 21, 189, 382, 301, None, 69, 267, None, 121, None, 168, 24, None, 431, 393, None, 190, None, None, None, None, 443, None, None, None, None, 153, None, None, 415, 418, 116, None, 438, 371, 33, 76, 196, None, 243, 172, None, 236, 183, None, 449, None, None, 474, None, 266, None, None, None, 476, 87, None, 496, None, 136, 387, None, None, None, 292, 34, 33, 434, None, None, 209, None, 478, 40, 386, 419, None, None, None, 509, None, None, None, 234, 503, None, 94, None, 294, None, 159, 508, None, 149, None, 277, None, None, 467, 295, None, None, 348, 227, 328, 376, 323, 161, 306, None, None, 28, None, None, None, None, 422, None, 78, 17, None, 463, 448, None, None, None, 229, 415, None, None, None, None, 207, None, None, 193, 363, 214, 207, 18, None, 276, 375, None, None, 122, 180, None, None, 124, None, None, 344, None, 96, None, 331, None, None, None, 396, 351, 179, None]

Simulating Address Translations:
Virtual Address: 991631, Result: 313743
Virtual Address: 283275, Result: 289419
Virtual Address: 638165, Result: 467157
Virtual Address: 402758, Result: 151878
Virtual Address: 156308, Result: 368276
Virtual Address: 25578, Result: 254954
Virtual Address: 262793, Result: 346761
Virtual Address: 856245, Result: 230581
Virtual Address: 990153, Result: 331721
Virtual Address: 191404, Result: 103340

Page Table Size: 4096 bytes
```

### Example 3: Using a Random Seed
```bash
python paging_simulator.py -p 4096 -a 16777216 -P 8388608 -s 42
```
**Output**:
```

Starting Paging Simulation...
Page Table: [None, 141, None, None, 126, 332, None, None, None, None, None, None, None, 260, None, 60, 322, None, 65, None, None, 410, 161, 469, 248, None, 447, 457, None, None, 149, 131, None, 135, None, None, 480, 318, None, None, 41, None, 486, None, None, None, None, 80, None, 197, None, None, 316, 239, None, 374, 126, 237, None, 112, 300, 73, None, 370, 191, None, None, 504, None, 346, 117, None, None, 19, None, None, None, 102, 302, None, 3, 353, None, 296, 123, None, 10, 130, None, 280, None, None, None, None, None, None, 467, 430, 397, 55, 149, 195, None, 90, 149, None, None, 36, 285, 451, 477, None, None, None, 346, None, None, 396, 469, None, None, 343, None, 484, 327, None, 195, None, 367, 151, None, None, 41, 83, 436, None, 505, None, None, 117, None, 506, None, 134, None, 345, None, 510, 226, 49, None, None, 359, 221, 225, 58, 54, 0, None, None, None, None, None, 81, 376, None, 58, None, None, None, None, 339, None, None, None, None, 196, None, None, 145, 236, 229, None, 269, 502, 502, 100, 424, 456, 347, 365, 253, None, None, 422, 225, None, 466, 503, None, 301, 450, None, None, 425, None, None, None, None, None, 492, None, 362, None, 416, None, 3, None, 216, 263, None, 241, None, None, 147, None, None, None, None, None, 436, None, None, None, None, 413, None, 11, 249, None, 175, None, 140, 212, None, None, 389, None, 23, None, None, 271, 364, 158, 147, None, 338, None, 299, 370, None, 435, None, None, 401, 416, None, None, None, 293, None, 224, None, None, None, 357, 282, None, None, None, None, None, 386, None, 475, 180, None, None, None, 159, 362, None, None, None, 93, 477, 168, None, 235, 179, None, 40, None, None, 490, None, 145, 459, None, None, 494, None, 506, None, 113, 240, 205, None, 141, None, None, 367, None, None, None, 162, None, 105, 289, 450, 266, None, None, None, 431, 358, None, 175, 492, 107, None, 18, 425, 498, 179, None, 81, None, None, None, None, None, 275, None, None, None, 46, None, None, 453, 285, 351, 19, 376, None, 122, None, None, 297, None, None, None, None, None, 232, None, 444, 47, 213, 407, None, 43, 384, None, 9, None, None, None, None, 213, None, None, 508, 148, None, 102, None, 20, None, 126, None, None, 62, None, 250, None, 242, None, 455, 426, None, None, None, None, 119, 36, 493, 177, None, 258, 281, None, None, 210, 426, 2, None, None, None, None, 491, None, 293, 328, None, None, 40, 341, None, 311, None, 58, 498, 200, None, 170, 358, None, None, 475, 409, None, None, 475, None, 52, None, 474, 131, None, 137, 56, None, 296, 168, 225, 477, 54, 260, 129, 367, 326, 31, None, None, None, None, 456, None, None, None, None, 232, 442, 9, None, 278, 281, None, 42, None, 288, 132, 384, None, 141, 460, None, 237, 362, None, None, None, None, 74, 465, 298, None, None, 82, None, 388, 178, None, None, None, None, None, None, None, None, None, None, None, 408, 153, None, None, None, None, 29, 395, 295, None, None, 181, None, 371, None, 226, 304, 312, 364, None, None, None, None, 348, None, 16, None, None, None, 69, 33, 215, 133, 257, 343, None, None, 370, 352, None, None, None, 157, None, 117, 465, None, 507, None, 155, None, None, None, None, None, None, 142, 4, None, 215, None, None, None, 88, 407, None, 380, None, None, None, 366, 190, None, None, 272, 69, None, None, 144, None, None, 454, None, 20, 176, 29, 41, 292, 232, None, None, None, None, None, 353, None, None, None, 359, 456, None, 187, None, None, 215, 23, 441, 392, 119, None, 64, None, 180, None, 339, 205, None, None, 121, None, None, None, 267, None, 425, None, 28, 127, 237, 29, 169, None, None, 336, None, 177, None, None, None, None, 332, None, None, 11, None, None, None, None, None, None, 361, None, None, 155, 345, None, 149, None, None, 316, 419, 111, 343, None, None, None, 158, 179, None, None, 404, None, None, None, 96, 392, None, None, 179, 197, None, 463, 300, None, None, 7, 458, 348, 129, None, 185, 431, 487, None, 231, 259, None, None, None, 26, 333, None, None, 493, 304, 396, None, 209, None, 497, 171, 360, None, None, None, None, 316, None, 209, 199, None, 24, None, 121, None, 352, 283, 71, 367, None, None, None, 129, 325, 302, None, None, 244, None, 363, None, None, 135, 31, None, 368, None, 383, 394, 344, None, None, 154, None, 172, None, 232, None, None, 230, 451, None, None, None, 384, None, 432, None, None, 377, 406, None, None, None, 439, None, None, 88, None, None, None, 117, 166, 180, 365, 245, 217, 38, 21, None, 132, None, 447, None, None, None, None, None, None, None, 505, None, None, None, 471, None, None, 30, 397, 364, None, 396, 225, 196, None, 32, 14, None, 379, None, 470, None, None, 433, 418, None, 393, 111, None, 175, None, None, 393, 43, 502, 467, 21, 189, 382, 301, None, 69, 267, None, 121, None, 168, 24, None, 431, 393, None, 190, None, None, None, None, 443, None, None, None, None, 153, None, None, 415, 418, 116, None, 438, 371, 33, 76, 196, None, 243, 172, None, 236, 183, None, 449, None, None, 474, None, 266, None, None, None, 476, 87, None, 496, None, 136, 387, None, None, None, 292, 34, 33, 434, None, None, 209, None, 478, 40, 386, 419, None, None, None, 509, None, None, None, 234, 503, None, 94, None, 294, None, 159, 508, None, 149, None, 277, None, None, 467, 295, None, None, 348, 227, 328, 376, 323, 161, 306, None, None, 28, None, None, None, None, 422, None, 78, 17, None, 463, 448, None, None, None, 229, 415, None, None, None, None, 207, None, None, 193, 363, 214, 207, 18, None, 276, 375, None, None, 122, 180, None, None, 124, None, None, 344, None, 96, None, 331, None, None, None, 396, 351, 179, None]

Simulating Address Translations:
Virtual Address: 991631, Result: 313743
Virtual Address: 283275, Result: 289419
Virtual Address: 638165, Result: 467157
Virtual Address: 402758, Result: 151878
Virtual Address: 156308, Result: 368276
Virtual Address: 25578, Result: 254954
Virtual Address: 262793, Result: 346761
Virtual Address: 856245, Result: 230581
Virtual Address: 990153, Result: 331721
Virtual Address: 191404, Result: 103340

Page Table Size: 4096 bytes
```

---

## Notes

- Ensure that the page size evenly divides the address space and physical memory.
- Use the `-s` flag to test deterministic scenarios with a specific random seed.
- Adjust `-u` to simulate scenarios with varying levels of page allocation.

---

## Outputs

- **Page Table**: Displays the allocated frames for pages.
- **Page Table Size**: Total size of the page table in bytes.
- **Address Translations**: Simulates random virtual address translations and outputs results (physical address or page fault).

---

## License

This project is licensed under the MIT License.

---

Happy simulating! 🎉
