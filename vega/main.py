from vega.brain import think

print("VEGA is online. Type 'exit' to quit.")

while True:
    user_input = input("You: ")
    if user_input.lower() == "exit":
        print("VEGA shutting down.")
        break

    reply = think(user_input)
    print("VEGA:", reply)
