 HOW TO TEST
🧪 Test Registration

Go to: http://127.0.0.1:8000/register/

Create a new user

You should be redirected to login

🧪 Test Login

Go to: http://127.0.0.1:8000/login/

Log in using registered credentials

Redirected to /profile/

🧪 Test Profile Update

Change username or email

Submit form

Success message displayed

🧪 Test Logout

Visit /logout/

Session ends securely

Tagging and Search System Documentation
1. Tagging System

Purpose:
Tags allow users to categorize blog posts, making it easier to organize content and find posts on similar topics.

How It Works:

Each post can have multiple tags associated with it.

Tags are stored in a many-to-many relationship with posts.

Tags are displayed on the post detail page as clickable badges.

User Instructions:

Adding Tags to a Post:

When creating or editing a post, enter tag names in the tags input field of the post form.

Multiple tags can be added, separated by commas.

If a tag does not exist, it will be automatically created.

Viewing Posts by Tag:

On the post detail page, tags appear as clickable badges.

Clicking a tag navigates to a page listing all posts that have that tag.

URL format: /tags/<tag_name>/

Editing Tags:

When editing a post, you can add new tags or remove existing ones using the same input field.

2. Search System

Purpose:
The search system allows users to quickly find posts based on keywords in the title, content, or associated tags.

How It Works:

The search bar is available in the site’s header (visible on all pages).

Users can enter a keyword and submit the search form.

The backend filters posts using the search keyword against:

Post titles

Post content

Tags associated with posts

User Instructions:

Performing a Search:

Enter the keyword in the search input field at the top of the page.

Click the Search button or press Enter.

Viewing Results:

The search results page displays all matching posts with links to their detail pages.

If no posts match the query, a message will indicate that no results were found.

URL format: /search/?q=<keyword>

3. Integration and Notes

Both features are integrated seamlessly with existing posts:

Tags are shown on post detail pages.

Search is accessible site-wide via the header form.

Permissions are respected: all users can view posts by tag and perform searches.

The search is case-insensitive and supports partial matches.

When creating or editing posts, only authenticated users can assign tags.