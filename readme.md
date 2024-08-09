## FlaskBook Backend API

* Live Link : todo
* [Frontend repo](https://github.com/AlFahimBinFaruk/FlaskBook_Client)

### Client Requirements
### As a Guest user, I can
- [ ] View Homepage, Blogs(pagination), User Profile
- [X] Signup
- [X] Login

### As an Admin user, I can
- [X] Login
- [X] Register - new admin can only be registered from backend.
- [X] View & edit my profile
- [ ] Upload, Update, Delete, Read My contents.
- [X] CRUD Users
- [ ] CRUD Roles (Only 2 roles Admin, User)
- [ ] CRUD user contents
- [ ] Logout

### As a Registered user, I can
- [X] Login
- [X] View & Edit or Delete My profile info
- [ ] Upload, Update, Delete, Read My contents.
- [ ] Read others contents.
- [ ] Comment, Delete my comments, and Upvote on every post's (including mine).
- [ ] Logout


### Technology
* Language : Python - version 3
* Framework : Flask
* Database : MongoDB

### Database Models
![Database Model image](https://drive.google.com/uc?export=view&id=1sRqNj3UHpOGM1HlIFY_UlnKoiq0wak4H)

### Screen shots
![Image](https://drive.google.com/uc?export=view&id=1xbwXOZi2K5WhGzdgbSnNGiUed2caHWOI)
![Image](https://drive.google.com/uc?export=view&id=1EhulLHXOdgtHUbC-4AvZ1tfdh5F0tMrb)
![Image](https://drive.google.com/uc?export=view&id=1mKVB6skYHfKET23gTd3v2xVduap6HjX8)
![Image](https://drive.google.com/uc?export=view&id=1D4YxzzLFbka1c4U2v2d__qKFxRGRR2ma)
![Image](https://drive.google.com/uc?export=view&id=1oQOjt8zpazbC0Hqe92N0ZRbpaUEPPQ8n)
![Image](https://drive.google.com/uc?export=view&id=1nOjRK0ctSwAO73cvnQpyudFlEa1WK10-)
![Image](https://drive.google.com/uc?export=view&id=1COF1NIc2ppfJbO4erMY4gqzZp8I7xm5Y)


### API Routes
* To register - POST
```text
/api/user/register

-body
{
    "first_name":"john",
    "last_name":"doe",
    "email":"john@gmail.com",
    "password":"123456"
}
```
* To login : will get and jwt token. - POST
```text
/api/user/login

-body
{
    "email":"john@gmail.com",
    "password":"123456"
}
```
* To Logout - will logout user/admin - GET
```text
/api/user/logout
```
* Get all user list : secured, authorized to admin only - GET
```text
/api/user/all?page=1,per_page=10
```
* Get individual user details : secured, only authorized admin and user himself and access it - GET
```text
/api/user/details{user_id}
```
* Update user information : secured, only authorized admin and user himself and access it - PUT
```text
/api/user/update/{user_id}

-body
{
    "email":"fahim@gmail.com"
}
```
* Get my details - GET
```text
/api/user/details/my-profile
```
* Update my profile - PUT
```text
/api/user/update/my-profile

-body
{
    "first_name":"fahim"
}
```
* Change my password
```text
/api/user/update/change-password
```

* Delete a user : secured, only authorized admin and user himself and access it - DELETE
```text
/api/user/delete/{user_id}
```
* Get all blog List - all visitors can access it, it will have pagination - GET
```text
/api/blog/all
```
* Get Individual user all blog List - all visitors can access it, it will have pagination - GET
```text
/api/blog/my/all
```
* Get individual blog details : all visitors can access it - GET
```text
/api/blog/details/{blog_id}
```
* Add new blog : only authorized users and admin can do it - POST
```text
/api/blog/add-new

-body
{
    "title":"test 1",
    "description":"test 1 desc"
}
```
* Update blog : only user who uploaded it or authorized admin can do it - PUT
```text
/api/blog/update/{id}

-body
{
    "title":"test 1 updated",
    "description":"test 1 desc"
}
```
* Delete blog : only user who uploaded it or authorized admin can do it - DELETE
```text
/api/blog/delete/{blog_id}
```
* Upvote : only registered user/admin can do it - POST
```text
/api/vote/upvote/{blog_id}
```
* Down vote : only registered user/admin can do it - POST
```text
/api/vote/downvote/{blog_id}
```
* Get comment list : GET
```text
/api/comment/all/{blog_id}
```
* Add new Comment : only registered user/admin can do it - POST
```text
/api/comment/add-new

-body
{
    "blog_id":"66b61b9e87b2c5efc3979d65",
    "body":"test comment"
}
```
* Update comment : only registered user and admin can do it - PUT
```text
/api/comment/update/{comment_id}

-body
{
    "body":"test comment updated"
}
```
* Delete comment : only registered user and admin can do it - DELETE
```text
/api/comment/delete/{comment_id}
```

### How to Build and Run





























