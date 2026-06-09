def safe_get(items, index):
    try:
        return ("ok", items[index])

    except IndexError:
        return ("error", "Index out of range")

    except TypeError:
        return ("error", "Index must be an int")

    except Exception as e:
        return ("error", f"Unexpected error: {e}")