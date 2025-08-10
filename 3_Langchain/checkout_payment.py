import sys

def process_credit_card():
    print("\n--- Credit Card Payment ---")
    card_number = input("Enter card number: ")
    expiry = input("Enter expiry date (MM/YY): ")
    cvv = input("Enter CVV: ")
    print(f"Processing credit card payment for card ending in {card_number[-4:]}...")
    print("Payment successful!\n")

def process_digital_wallet():
    print("\n--- Digital Wallet Payment ---")
    wallet = input("Enter digital wallet provider (e.g., PayPal, Apple Pay): ")
    email = input("Enter wallet email/ID: ")
    print(f"Processing {wallet} payment for {email}...")
    print("Payment successful!\n")

def process_bank_transfer():
    print("\n--- Bank Transfer Payment ---")
    account = input("Enter bank account number: ")
    routing = input("Enter routing number: ")
    print(f"Processing bank transfer from account {account[-4:]}...")
    print("Payment successful!\n")

def main():
    print("Welcome to Checkout!")
    print("Please select a payment method:")
    print("1. Credit Card")
    print("2. Digital Wallet")
    print("3. Bank Transfer")
    choice = input("Enter the number of your choice: ")

    if choice == '1':
        process_credit_card()
    elif choice == '2':
        process_digital_wallet()
    elif choice == '3':
        process_bank_transfer()
    else:
        print("Invalid choice. Please restart and select a valid payment method.")
        sys.exit(1)

    print("Thank you for your payment!")

if __name__ == "__main__":
    main() 