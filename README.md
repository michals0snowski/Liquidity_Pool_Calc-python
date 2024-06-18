# Liquidity_Pool_Calc-python
Simple calc for adding pair of assets to liquidity pool (crypto)

# Token Pool Calculator

This is a simple Python application with a GUI interface to calculate the number of seats in the Polish parliament based on election results using the D'Hondt method. The program is implemented using the `tkinter` module to provide an easy-to-use interface for input and displaying results.

## Features

- Input names of tokens in a pool.
- Input current quantity of tokens and their price ratio.
- Input the current value of the pool and amounts of tokens to add.
- Calculate new quantities, prices, and values of tokens after adding the specified amounts.
- Display the results in a separate window.

## Requirements

- Python 3.x
- `tkinter` module (included with standard Python installations)
- `selenium` module (for web automation tasks)

## Installation

1. Clone the repository or download the script file.

    ```sh
    git clone https://github.com/michals0snowski/Liquidity_Pool_Calc-python.git
    cd Liquidity_Pool_Calc-python
    ```

2. Ensure you have Python 3.x installed. You can download it from [python.org](https://www.python.org/).

3. Install the required `selenium` module using pip:

    ```sh
    pip install selenium
    ```

## Usage

1. Run the script using Python.

    ```sh
    python LiquidityPoolCalcUI.py
    ```

2. The main window will appear, allowing you to input the necessary data:

    - Token A Name
    - Token B Name
    - Current quantity of Token A
    - Current quantity of Token B
    - Price Ratio
    - Current Pool Value (in dollars)
    - Amount of Token A to add
    - Amount of Token B to add
    - Share of Pool Before (%)

3. Click the "Calculate" button to perform the calculations.

4. A new window will display the results, including new quantities, prices, values, and price impacts for both tokens.

### Input Fields

- **Token A Name**: The name of the first currency in the pair.
- **Token B Name**: The name of the second currency in the pair.
- **Current quantity of Token A**: The current quantity of Token A in the pool.
- **Current quantity of Token B**: The current quantity of Token B in the pool.
- **Price Ratio**: The ratio of the value of both tokens.
- **Current Pool Value (in dollars)**: The current value of the pool.
- **Amount of Token A to add**: The amount of Token A being added to the pool.
- **Amount of Token B to add**: The amount of Token B being added to the pool.
- **Share of Pool Before (%)**: The user's share in the pool before adding new tokens.

### Results

- New quantities of Token A and Token B in the pool.
- Contribution values for both tokens.
- Total contribution value and pool value after adding assets.
- New prices and values for both tokens in the pool.
- Price impacts for both tokens.

## Contributing

Feel free to submit issues or pull requests if you have suggestions or improvements.

## License

This project is licensed under the MIT License.
