import secrets, sys

def get_result(count):
    i = 0
    results = []
    while i < count:
        choice = secrets.choice([True, False])
        results.append("Heads" if choice else "Tails")
        i += 1

    return results

if __name__ == "__main__":
    requested_executions = 1

    if len(sys.argv) == 2:
        requested_executions = int(sys.argv[1])

    results = get_result(requested_executions)

    print(results)
