from urllib.request import urlopen as uReq
from bs4 import BeautifulSoup as soup
import datetime
import string
def countIssues(url):
    #for storing issue count
    issues_today = 0
    issues_week = 0
    issues_ago = 0
    # add issues to url to the repository url
    my_url = url.strip('/') + '/issues'

    second_part_url = '?page='
    third_part_url = '&q=is%3Aissue+is%3Aopen'
    client_data = uReq(my_url+second_part_url+str(1)+third_part_url)
    page_html = client_data.read()
    client_data.close()
    page_soup = soup(page_html,'html.parser')
    # print(page_soup)
    containers = page_soup.findAll("div",{"class":"pagination"})
    containers_2 = page_soup.findAll("span",{"class":"Counter"})
    total_issues = str(containers_2[0].contents[0])
    # total_issues = "abc123"
    for char in string.punctuation:
        total_issues = total_issues.replace(char,'')
    
    try:
        total_issues = int(total_issues)
        brute = False
    except:
        brute = True
    total_pages = containers[0].find('em',{'class':'current'})['data-total-pages']
    total_pages = int(total_pages)
    to_cont = True
    for number_page in range(1,total_pages+1):
        if not to_cont:
            break
        client_data = uReq(my_url+second_part_url+str(number_page)+third_part_url)
        page_html = client_data.read()
        client_data.close()
        page_soup = soup(page_html,'html.parser')
        containers = page_soup.findAll("div",{"class":"d-table table-fixed width-full Box-row--drag-hide position-relative"})
        for i in range(len(containers)):
            container = containers[i]
            temp1 = container.findAll("div",{"class":"mt-1 text-small text-gray"})
            final = temp1[0].findAll("relative-time")[0]
            diff = datetime.datetime.now() - datetime.datetime.strptime(final["datetime"], "%Y-%m-%dT%H:%M:%SZ")
            days,seconds = diff.days, diff.seconds
            hours =  days*24+ (seconds// 3600)
            if hours <=24:
                issues_today+=1
            elif hours>=24 and hours <=128:
                issues_week+=1
            else:
                if not brute:
                    to_cont = False
                    break
                else:
                    issues_ago +=1
        if not brute:
            issues_ago = total_issues - issues_today - issues_week

    return issues_today,issues_week,issues_ago
