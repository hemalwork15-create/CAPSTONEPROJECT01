from behave import given, when, then
import requests
import os

BASE_URL = "http://127.0.0.1:8000"

@given("the FastAPI app is running")
def step_impl(context):
    try:
        r = requests.get(f"{BASE_URL}/docs")
        assert r.status_code == 200
    except:
        raise Exception("FastAPI app is not running on http://127.0.0.1:8000")

@when('I upload a document with title "{title}", category_id {cat_id:d}, uploader_id {user_id:d}')
def step_impl(context, title, cat_id, user_id):
    sample_file = "sample.pdf"
    if not os.path.exists(sample_file):
        with open(sample_file, "wb") as f:
            f.write(b"Sample PDF content")
    
    files = {"file": open(sample_file, "rb")}
    data = {
        "title": title,
        "category_id": cat_id,
        "uploader_id": user_id
    }
    context.response = requests.post(f"{BASE_URL}/documents/", data=data, files=files)

@then("the response should indicate success")
def step_impl(context):
    assert context.response.status_code == 200 or context.response.status_code == 201

@then("the document should exist in the document list")
def step_impl(context):
    r = requests.get(f"{BASE_URL}/documents/")
    assert r.status_code == 200
    documents = r.json()
    titles = [doc['title'] for doc in documents]
    assert "Linear Algebra Notes" in titles
    

