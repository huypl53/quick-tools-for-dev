# My Helpful Tools

This repository contains a collection of helpful tools, each organized in its own directory. These tools are designed to solve specific tasks and can be installed and run as command-line scripts.

## Tools

- [SQL Tool](packages/sql/README.md): A tool for processing large SQL files efficiently.

## Getting Started

### Prerequisites

- Python 3.12 or higher
- `pip` (Python package installer)

### Installation

1. Clone the repository:

   ```bash
   git clone https://github.com/your-username/my-helpful-tools.git
   cd my-helpful-tools
   ```

2. Navigate to the tool's directory (e.g., `packages/sql`) and install it:

   ```bash
   cd packages/sql
   pip install .
   ```

### Usage

#### SQL Tool

The SQL tool provides a command-line interface (CLI) for processing large SQL files.

1. Run the `sql-cli` command:

   ```bash
   sql-cli trim --record-num 3 input.sql output.sql
   ```

   - `--record-num`: Number of records to keep from each line (default: 3).
   - `input.sql`: Path to the input SQL file.
   - `output.sql`: Path to the output SQL file.

2. For more help, use:

   ```bash
   sql-cli --help
   ```

## Contributing

Contributions are welcome! Feel free to open issues or submit pull requests to improve the tools.

## License

This project is licensed under the MIT License. See the [LICENSE](LICENSE) file for details.
