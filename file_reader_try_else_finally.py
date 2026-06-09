def read_numbers(path):
    lines_read = 0
    numbers = []

    try:
        with open(path, "r") as f:
            for line in f:
                numbers.append(float(line.strip()))
                lines_read += 1

    except FileNotFoundError:
        return ("error", f"File not found: {path}", lines_read)

    except PermissionError:
        return ("error", f"Permission denied: {path}", lines_read)

    except ValueError:
        return ("error", "Invalid number on a line", lines_read)

    except Exception as e:
        return ("error", str(e), lines_read)

    else:
        total = sum(numbers)
        return ("ok", total, lines_read)

    finally:
        print("Done reading")