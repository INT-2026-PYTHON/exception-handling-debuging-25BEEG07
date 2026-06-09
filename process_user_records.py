def process_records(records):
    clean_records = []
    error_log = []

    for index, record in enumerate(records):
        try:
            # May raise KeyError or TypeError
            name = record["name"]
            age = int(record["age"])
            score = float(record["score"])

        except (KeyError, TypeError) as e:
            error_log.append(
                (index, type(e).__name__, str(e))
            )

        except ValueError as e:
            error_log.append(
                (index, type(e).__name__, str(e))
            )

        else:
            # Runs only if no exception occurred
            clean_records.append({
                "name": name,
                "age": age,
                "score": score
            })

    return clean_records, error_log


def process_strict(records):
    try:
        clean_records, error_log = process_records(records)

        if error_log:
            raise RuntimeError(
                f"{len(error_log)} record(s) failed to process"
            )

        return clean_records

    except RuntimeError:
        # Re-raise the exception after it has been logged/handled
        raise


# -------------------------------------------------
# Driver Code
# -------------------------------------------------

records = [
    {"name": "Alice", "age": "25", "score": "88.5"},
    {"name": "Bob",   "age": "abc", "score": "70"},
    {"name": "Carol", "age": "30"},          # missing score
    "not a dict",                            # wrong type
    {"name": "Dan",   "age": "40", "score": "55.5"},
]

clean_records, error_log = process_records(records)

print("Clean Records:")
print(clean_records)

print("\nError Log:")
print(error_log)

try:
    process_strict(records)

except RuntimeError as e:
    print(f"\nStrict mode raised: {type(e).__name__}: {e}")