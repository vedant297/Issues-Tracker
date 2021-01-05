# Issues-tracker
System Requirements(pip3 modules required for server to run):
 - bs4
 - flask
 - urllib
 - datetime

Implementation Details:
Given the link for the github repository, my server extracts the issues for that Project/Repository and classifies them into 3 categories:
- Today.
- Last week.
- Earlier than a week.

For the server/backend part, python framework flask has been used.
For scraping issues from the website beautifulSoup library has been used.

How to use on localhost:
After cloning the server, run the flask_app.py file(python3), which will start the server for same.
Use the localhost url provided by the code's output, to extract the issues from a Repository.

Special Note:
You need to provide the link to the github repository and not the link for issues page for a Repository.
