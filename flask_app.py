
# A very simple Flask Hello World app for you to get started with...

from flask import *
from processing import countIssues

app = Flask(__name__)

'''@app.route('/')
def hello_world():
    return 'Hello from Flask!'
    '''


@app.route('/', methods=['GET'])
def adder_page_get():
    return render_template('index1.html')
@app.route('/', methods=['POST'])
def adder_page_post():
    url = str(request.form["url"])
    issues_today,issues_week,issues_ago = countIssues(url)
    total_issues = issues_today+issues_week+issues_ago
    print(total_issues,issues_today,issues_ago,issues_week)
    return render_template('index.html',v1=str(issues_today),v2=str(total_issues), v3=str(issues_week),v4=str(issues_ago))

app.run(debug=True)