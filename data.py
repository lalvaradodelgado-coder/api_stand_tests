def get_user_body(first_name):
    return {
        "firstName": first_name,
        "phone": "+1 555 123-4567",
        "address": "123 Main St, City, Country"
    }

headers = {"Content-Type": "application/json"}