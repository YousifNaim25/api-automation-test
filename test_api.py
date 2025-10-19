import requests

def test_api():
    url = "https://jsonplaceholder.typicode.com/todos/1"
    response = requests.get(url)
    
    # تحقق من أن الاستجابة ناجحة
    assert response.status_code == 200, f"Status code failed: {response.status_code}"
    
    data = response.json()
    # تحقق من وجود مفتاح "title"
    assert "title" in data, "Title key missing"
    
    print("API test passed ✅")

if __name__ == "__main__":
    test_api()
