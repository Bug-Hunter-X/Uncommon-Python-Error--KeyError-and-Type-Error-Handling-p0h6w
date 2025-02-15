def function_with_uncommon_error(data):
    try:
        # Simulate an uncommon error: accessing a key that might not exist
        result = data['nonexistent_key'] * 2
        return result
    except KeyError:
        # Handle the KeyError gracefully
        return 0
    except TypeError as e:
        # Handle type errors
        print(f"Type Error: {e}")
        return None
    except Exception as e:
        #Handle any other exceptions
        print(f"An unexpected error occurred: {e}")
        return None