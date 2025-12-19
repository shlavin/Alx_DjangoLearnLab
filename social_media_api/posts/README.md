API Endpoints Documentation 📘
🔹 Posts
Method	Endpoint	Description
GET	/api/posts/	List posts (paginated)
POST	/api/posts/	Create post
GET	/api/posts/{id}/	Retrieve post
PUT	/api/posts/{id}/	Update own post
DELETE	/api/posts/{id}/	Delete own post


TESTING RESULTS
POST: http://127.0.0.1:8000/api/posts/
{
    "id": 1,
    "author": "john",
    "title": "My First Post",
    "content": "Hello World!",
    "comments": [],
    "created_at": "2025-12-19T04:03:37.564880Z",
    "updated_at": "2025-12-19T04:03:37.564925Z"
}

POST: http://127.0.0.1:8000/api/comments/

{
  "post": 1,
  "content": "Nice post!"
}