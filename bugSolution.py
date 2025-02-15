def function_with_uncommon_error(data):
    try:
        # Check if the key exists before accessing it.
        result = data.get('nonexistent_key', 0) * 2  # Returns 0 if key is not found
        return result
    except TypeError as e:
        print(f"Type Error: {e}")
        return None
    except Exception as e:
        print(f"An unexpected error occurred: {e}")
        return None