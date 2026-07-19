def format_balance(balance, token_symbol="ETH"):
    return f"{balance:.4f} {token_symbol}"

# Mock balance update
print(f"Current Wallet Balance: {format_balance(1.234567, 'BASE')}")
