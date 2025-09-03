# Chris McCathern
# Exercise#1 Ticket Pr-Sale Prorgam
# Function to handle one buyer's ticket purchase

def buy_tickets(remaining):
    # Ask the buyer how many tickets they want
    tickets_requested = int(input("How many tickets would you like (1–4)? "))

    # Check if valid (cannot exceed 4 or available tickets)
    if tickets_requested < 1 or tickets_requested > 4:
        print("❌ You can only buy between 1 and 4 tickets.")
        return 0, remaining  # no purchase

    if tickets_requested > remaining:
        print(f"❌ Only {remaining} tickets left. You cannot buy {tickets_requested}.")
        return 0, remaining  # no purchase

    # Successful purchase
    remaining -= tickets_requested
    print(f"✅ You bought {tickets_requested} ticket(s). {remaining} ticket(s) remaining.\n")
    return 1, remaining  # count 1 buyer


# Function to run the ticket pre-sale system
def ticket_presale():
    total_tickets = 10
    buyers = 0  # accumulator

    print("🎬 Welcome to the Cinema Ticket Presale!")
    print("Maximum 4 tickets per buyer. Only 20 tickets available.\n")

    # Loop until tickets are gone
    while total_tickets > 0:
        buyer_count, total_tickets = buy_tickets(total_tickets)
        buyers += buyer_count  # accumulate number of buyers

    print("\n🎟️ All tickets have been sold!")
    print(f"Total buyers: {buyers}")


# Run the program
ticket_presale()
