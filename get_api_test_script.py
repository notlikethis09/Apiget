import requests

# General function to send GET and validate respons
def send_get_request(url):
    response = requests.get(url)
    return response

# Function to validate data type 
def validate_response_data_types(response):
    data = response.json()
    
    try:
        for post in data:
            assert isinstance(post["userId"], int)
            assert isinstance(post["id"], int)
            assert isinstance(post["title"], str)
            assert isinstance(post["body"], str)
        
        print("Test case passed: Data types are as expected.")
    except AssertionError as e:
        print(f"Test case failed: {str(e)}")

if __name__ == "__main__":
    # URL endpoint API
    api_url = "https://jsonplaceholder.typicode.com/posts"
    
    # Request get
    response = send_get_request(api_url)
    
    # Check status code
    if response.status_code == 200:
        print("API Request Successful")
        
        # Validate data type
        validate_response_data_types(response)
    else:
        print(f"API Request Failed with status code: {response.status_code}")
