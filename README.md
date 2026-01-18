# Coffee Shop Simulator

This is a simple coffee shop simulator written in Python. It allows you to run a coffee shop, manage resources, take orders, and handle customer payments.

## Features

*   **Order Management:**  Choose from a selection of coffee flavors.
*   **Resource Management:**  Refill resources, track inventory.
*   **Payment Processing:**  Handle customer payments with coins.
*   **Reporting:** Generate a resource report.

## Getting Started

### Prerequisites

*   Python 3.6 or higher

### Installation

1.  Clone the repository: `git clone https://github.com/mandalorian-0/coffe_machine.git`
2.  Navigate to the project directory: `cd coffe_machine`

### Running the Simulator

1.  Run the main script: `python main.py`  (Assuming the main script is named `main.py`)
2.  Follow the on-screen prompts to operate the coffee shop.

## Usage

The program simulates a coffee shop with the following actions:

*   `report`:  Generates a report of current resources.
*   `off`:  Shuts down the coffee shop.
*   `refill`: Refills the coffee resources.
*   [Coffee Flavor Choices]:  Select a coffee flavor to prepare (e.g., "latte", "espresso").  The available flavors are 
defined in the `coffee_flavors` data.

##  Controls

*   The program will display a menu with available options.
*   Press the corresponding key to make your choice.
*   `Press enter` to advance to the next step when prompted.

## Notes

*   This is a simplified simulation and does not include features like customer interactions or complex inventory management.
*   The program relies on functions such as `get_resources_without_money`, `get_specific_flavor`, 
`check_resources`, `refill_machine`, `update_resources`, `process_coins`, and more (these are assumed to be defined elsewhere within the project).

## Contributing

Contributions are welcome! Please submit any bug fixes or enhancements as GitHub issues or pull requests.
