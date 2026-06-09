def safe_divide(a, b):
    try:
        # Convert inputs to numbers
        a = float(a)
        b = float(b)

        # Debugging aid:
        # print(type(a), type(b))

        result = a / b
        return ("ok", result)

    except ValueError:
        return ("error", "Inputs must be numbers")

    except ZeroDivisionError:
        return ("error", "Cannot divide by zero")

    except Exception as e:
        return ("error", f"Unexpected error: {e}")

    finally:
        print("Calculation finished")