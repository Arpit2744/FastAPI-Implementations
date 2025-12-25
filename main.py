from fastapi import FastAPI
from enum import Enum

class ModelName(str,Enum):
    alexnet = "alexnet"
    resnet = "resnet"
    lenet = "lenet"
    

app = FastAPI()

@app.get("/") #post,delete,
async def root():
    return {"message": "hello world"}

@app.get("/items/{item_id}")
async def read_item(item_id:int): #You can use the same type declarations with str, float, bool and many other complex data types.
    return {"item_id": item_id}

@app.get("/users/me")
async def read_user_me():
    return {"user_id": "the current user"}

@app.get("/users/{user_id}")
async def read_user(user_id:str):
    return {"user_id":user_id}

"""
Order matters¶
When creating path operations, you can find situations where you have a fixed path.

Like /users/me, let's say that it's to get data about the current user.

And then you can also have a path /users/{user_id} to get data about a specific user by some user ID.

Because path operations are evaluated in order, you need to make sure that the path for /users/me is declared before the
one for /users/{user_id}:

Otherwise, the path for /users/{user_id} would match also for /users/me, "thinking" that it's receiving a parameter user_id with a value of "me".

Similarly, you cannot redefine a path operation:
"""

@app.get("/models/{model_name}")
async def get_model(model_name:ModelName):
    if model_name is ModelName.alexnet:
        return {"model_name": model_name, "message": "deep learning ftw!"}
    if model_name.value == "lenet":
        return {"model_name": model_name, "message": "LeCNN all the images"}
    return {"model_name": model_name, "message": "have some residuals"}

@app.get("/files/{file_path:path}")
async def read_file(file_path: str):
    return {"file_path":file_path}

"""
Path convertor¶
Using an option directly from Starlette you can declare a path parameter containing a path using a URL like:

/files/{file_path:path}
In this case, the name of the parameter is file_path, and the last part, :path, 
tells it that the parameter should match any path.
"""

## Query Parameters

"""
When you declare other function parameters that are not part of
the path parameters, they are automatically interpreted as "query" parameters.
"""

fake_items_db = [{"item_name": "foo"},{"item_name": "Bar"},{"item_name": "apple"}]

@app.get("/items/")
async def read_item(skip: int=0,limit: int=10):
    return fake_items_db[skip : skip + limit]

"""
The query is the set of key-value pairs that go after the ? in a URL,
 separated by & characters.

For example, in the URL:


http://127.0.0.1:8000/items/?skip=0&limit=10
...the query parameters are:

skip: with a value of 0
limit: with a value of 10
"""



