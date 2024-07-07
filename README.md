### `README.md`
```
# Trix-Framework CLI Tool

The Trix-Framework CLI tool is designed to help you manage and clone various security tools categorized by their functionality. This tool allows users to select categories, view tools within those categories, and clone the desired tools into their home directory. The tool also provides the ability to stop the cloning process without exiting the application.

## Features

- 195+ tools are available 

- Load and parse tools from a `tools.json` file.
- Display available categories and tools.
- Clone selected tools to the home directory.
- Handle directory existence conflicts.
- Stop the cloning process without exiting the tool.
- Support for graceful interruption using Ctrl+C.

## Prerequisites

- Python 3.x
- Git

## Installation

1. **Clone the Repository**

    ```sh
    git clone <repository_url>
    cd <repository_directory>
    ```

2. **Ensure `tools.json` is Present**

    Make sure the `tools.json` file is located in the same directory as `cli3.py`. The `tools.json` should contain the list of tools categorized by their functionality.

## Usage

1. **Run the Script**

    ```sh
    python3 cli3.py
    ```

2. **Select a Category**

    The tool will display a list of categories from which you can select by entering the corresponding number.

3. **Select a Tool**

    After selecting a category, the tool will list the available tools within that category. Select a tool to clone by entering its corresponding number.

4. **Commands**

    - **Back**: Return to the category selection menu.
    - **Stop**: Stop the current cloning process.
    - **Exit**: Exit the application.

## Example

### Running the Script

```sh
┌──(root㉿kali)-[~/Trix-Framework]
└─# python3 cli3.py

Categories Examples:
1. Database SQL Injection Vulnerability or Brute Force
2. Web Vulnerability Scanners
3. Advanced Persistent Threat Detect
Select a category (or type 'exit' to quit): 1

Tools in Database SQL Injection Vulnerability or Brute Force:
1. SQLiScanner - A SQLi vulnerability scanner via SQLMAP and Charles
2. DSSS - A SQLi vulnerability scanner with 99 lines of code
Select a tool to clone (or type 'back' to go back, 'stop' to stop cloning, 'exit' to quit): 1

Cloning SQLiScanner...
```

## Handling Cloning Conflicts

If the directory already exists, you will be prompted to overwrite it:

```
The directory /root/SQLiScanner already exists. Do you want to overwrite it? (yes/no): no
Skipping clone for https://github.com/0xbug/SQLiScanner as the directory already exists.
```

## Stopping the Cloning Process

You can stop the cloning process by typing `stop`:

```
Select a tool to clone (or type 'back' to go back, 'stop' to stop cloning, 'exit' to quit): stop

Cloning process interrupted. Terminating...
Cloning stopped.
```

## Interrupting the Process

You can also interrupt the cloning process using `Ctrl+C`:

```
^C
Cloning process interrupted. Terminating...
```

## Contributing

Feel free to contribute to this project by opening issues, submitting pull requests, or suggesting features.

## License

This project is licensed under the MIT License.

## Acknowledgments

Thanks to the contributors and the open-source community for providing the tools and resources used in this project.
```


This `README.md` provides clear instructions on how to use the CLI tool, making it easier for users to understand its functionality and usage.
