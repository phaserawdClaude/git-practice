print("DEX bot started")

rpc = "main"

try:
    raise ConnectionError("Main RPC is unavailable")
except ConnectionError:
    rpc = "backup"
    print("Using backup RPC")
print("Changed on GitHub")
