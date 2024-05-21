## FlaskBook Backend API

* Live Link : todo
* Frontend repo : todo

### Client Requirements
As a Guest user, I can
* View Homepage, Blogs, User Profile
* Signup, Login

As an Admin user, I can
* Login
* Register - new admin can only be registered from backend.
* View & edit my profile
* Upload, Update, Delete , Read My contents.
* CRUD Users
* CRUD Roles(Only 2 roles Admin,User)
* CRUD user contents
* Logout

As a Registered user, I can
* Login
* View & Edit or Delete My profile info
* Upload, Update, Delete , Read My contents.
* Read others contents.
* Comments, Delete my comments and Upvote on every post's (including mine).
* Logout

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
```
* To login : will get and jwt token. - POST
```text
/api/user/login
```
* To Logout - will logout user/admin - GET
```text
/api/user/logout
```
* Get all user list : secured, authorized to admin only - GET
```text
/api/user/all
```
* Get individual user details : secured, only authorized admin and user himself and access it - GET
```text
/api/user/{id}
```
* Update user information : secured, only authorized admin and user himself and access it - PUT
```text
/api/user/update/{id}
```
* Update user role : only authorized admin can do it - PUT
```text
/api/user/update/role/{id}
```
* Delete a user : secured, only authorized admin and user himself and access it - DELETE
```text
/api/user/delete/{id}
```
* Get all blog List - all visitors can access it, it will have pagination - GET
```text
/api/blog/all
```
* Get Individual user all blog List - all visitors can access it, it will have pagination - GET
```text
/api/user/{id}/blog/all
```
* Get individual blog details : all visitors can access it - GET
```text
/api/blog/{id}
```
* Add new blog : only authorized users and admin can do it - POST
```text
/api/blog/add-new
```
* Update blog : only user who uploaded it or authorized admin can do it - PUT
```text
/api/blog/update/{id}
```
* Delete blog : only user who uploaded it or authorized admin can do it - DELETE
```text
/api/blog/delete/{id}
```
* Upvote : only registered user/admin can do it - POST
```text
/api/blog/upvote/{post_id}
```
* Down vote : only registered user/admin can do it - POST
```text
/api/blog/downvote/{post_id}
```
* Add new Comment : only registered user/admin can do it - POST
```text
/api/blog/comment/{post_id}
```
* Update comment : only registered user and admin can do it - PUT
```text
/api/blog/comments/update/{post_id}/{comment_id}
```
* Delete comment : only registered user and admin can do it - DELETE
```text
/api/blog/comments/delete/{post_id}/{comment_id}
```

### How to Build and Run





























