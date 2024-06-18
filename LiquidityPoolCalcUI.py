"""
Credit card veryfier (using Luhn's algorithm, and card len check).
M_Sosnowski
"""

import tkinter as tk
from tkinter import messagebox

def calculate_results():
    try:
        # Gathering input values
        tokenA = entry_tokenA.get()
        tokenB = entry_tokenB.get()
        tokenA_currenQntty = float(entry_tokenA_currenQntty.get())
        tokenB_currenQntty = float(entry_tokenB_currenQntty.get())
        priceRatio = float(entry_priceRatio.get())
        poolValueBefore = float(entry_poolValueBefore.get())
        tokenA_added = float(entry_tokenA_added.get())
        tokenB_added = float(entry_tokenB_added.get())
        shareOfPoolBefore = float(entry_shareOfPoolBefore.get())
        
        # Calculations
        tokenA_newQntty = tokenA_currenQntty + tokenA_added
        tokenB_newQntty = tokenB_currenQntty + tokenB_added

        tokenB_price = poolValueBefore / ((tokenB_currenQntty * priceRatio) + tokenA_currenQntty)        
        tokenA_price = (poolValueBefore - (tokenB_price * tokenA_currenQntty)) / tokenB_currenQntty 
        
        tokenA_newValue = tokenA_newQntty * tokenA_price
        tokenB_newValue = tokenB_newQntty * tokenB_price
        
        tokenA_contributionValue = tokenA_added * tokenA_price
        tokenB_contributionValue = tokenB_added * tokenB_price
        contributionValue = tokenA_contributionValue + tokenB_contributionValue
        
        poolValueAfter = poolValueBefore + contributionValue
        
        shareOfPoolContributed = contributionValue / poolValueAfter
        shareOfPoolNew = (shareOfPoolBefore / 100) + shareOfPoolContributed
        
        tokenA_newPrice = tokenB_price * tokenB_newQntty / tokenA_newQntty
        tokenB_newPrice = tokenA_price * tokenA_newQntty / tokenB_newQntty
        
        tokenA_priceImpact = (tokenA_newPrice - tokenA_price) / (tokenA_price * 100)
        tokenB_priceImpact = (tokenB_newPrice - tokenB_price) / (tokenB_price * 100)
        
        # Displaying results in a new window
        result_window = tk.Toplevel(root)
        result_window.title("Results")
        
        result_text = f"""
        {tokenA} new quantity in pool: {tokenA_newQntty:.5f}
        {tokenB} new quantity in pool: {tokenB_newQntty:.5f}
        
        Contribution value of {tokenA}: {tokenA_contributionValue:.5f} $
        Contribution value of {tokenB}: {tokenB_contributionValue:.5f} $
        Total contribution value: {contributionValue:.5f} $
        Pool value after adding assets: {poolValueAfter:.5f}
        
        New price of {tokenA}: {tokenA_newPrice:.5f}
        New price of {tokenB}: {tokenB_newPrice:.5f}
        New value of {tokenA} in the pool: {tokenA_newValue:.5f}
        New value of {tokenB} in the pool: {tokenB_newValue:.5f}
        
        {tokenA} price impact: {(tokenA_priceImpact * 100):.2f} %
        {tokenB} price impact: {(tokenB_priceImpact * 100):.2f} %
        """
        
        lbl_result = tk.Label(result_window, text=result_text, justify=tk.LEFT)
        lbl_result.pack(padx=20, pady=20)
        
    except ValueError:
        messagebox.showerror("Input Error", "Please enter valid numbers.")

# Main window
root = tk.Tk()
root.title("Token Pool Calculator")

tk.Label(root, text="Token A Name:").grid(row=0, column=0, sticky=tk.W, padx=10, pady=5)
entry_tokenA = tk.Entry(root)
entry_tokenA.grid(row=0, column=1, padx=10, pady=5)

tk.Label(root, text="Token B Name:").grid(row=1, column=0, sticky=tk.W, padx=10, pady=5)
entry_tokenB = tk.Entry(root)
entry_tokenB.grid(row=1, column=1, padx=10, pady=5)

tk.Label(root, text="Current quantity of Token A:").grid(row=2, column=0, sticky=tk.W, padx=10, pady=5)
entry_tokenA_currenQntty = tk.Entry(root)
entry_tokenA_currenQntty.grid(row=2, column=1, padx=10, pady=5)

tk.Label(root, text="Current quantity of Token B:").grid(row=3, column=0, sticky=tk.W, padx=10, pady=5)
entry_tokenB_currenQntty = tk.Entry(root)
entry_tokenB_currenQntty.grid(row=3, column=1, padx=10, pady=5)

tk.Label(root, text="Price Ratio:").grid(row=4, column=0, sticky=tk.W, padx=10, pady=5)
entry_priceRatio = tk.Entry(root)
entry_priceRatio.grid(row=4, column=1, padx=10, pady=5)

tk.Label(root, text="Current Pool Value (in dollars):").grid(row=5, column=0, sticky=tk.W, padx=10, pady=5)
entry_poolValueBefore = tk.Entry(root)
entry_poolValueBefore.grid(row=5, column=1, padx=10, pady=5)

tk.Label(root, text="Amount of Token A to add:").grid(row=6, column=0, sticky=tk.W, padx=10, pady=5)
entry_tokenA_added = tk.Entry(root)
entry_tokenA_added.grid(row=6, column=1, padx=10, pady=5)

tk.Label(root, text="Amount of Token B to add:").grid(row=7, column=0, sticky=tk.W, padx=10, pady=5)
entry_tokenB_added = tk.Entry(root)
entry_tokenB_added.grid(row=7, column=1, padx=10, pady=5)

tk.Label(root, text="Share of Pool Before (%):").grid(row=8, column=0, sticky=tk.W, padx=10, pady=5)
entry_shareOfPoolBefore = tk.Entry(root)
entry_shareOfPoolBefore.grid(row=8, column=1, padx=10, pady=5)

btn_calculate = tk.Button(root, text="Calculate", command=calculate_results)
btn_calculate.grid(row=9, columnspan=2, pady=20)

root.mainloop()