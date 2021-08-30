import requests
from bs4 import BeautifulSoup

# Using BeautifulSoup
def jobSearch(keyword):
    # Getting page HTML
    words = keyword.split(" ")
        
    if (len(words) < 2):
        URL = "https://hk.jobsdb.com/hk/search-jobs/{}".format(keyword)
    else:
        URL = "https://hk.jobsdb.com/hk/search-jobs/{}".format("-".join(words))
    page = requests.get(URL)

    # Parsing content using beautifulsoup
    soup = BeautifulSoup(page.content, "html.parser")

    # Select job data
    jobElements = soup.find_all("div", class_="sx2jih0 zcydq84g zcydq83g zcydq86g zcydq85g zcydq81w zcydq82o zcydq8cg zcydq8c4")
    # jobElements = jobElements[:50] # For testing, use smaller sample
    jobs = []
    for job in jobElements:
        jobTitle = job.find("div", class_="sx2jih0 _2j8fZ_0 sIMFL_0 _1JtWu_0").text.strip()
        # print(jobTitle)
        company = job.find("span", class_="sx2jih0 zcydq82c _18qlyvc0 _18qlyvcv _18qlyvc1 _18qlyvc8").text.strip()
        # print(company)
        if (job.find_all("span", class_="sx2jih0 zcydq82c zcydq8r iwjz4h0")):
            location = job.find("span", class_="sx2jih0 zcydq82c zcydq8r iwjz4h0").text.strip()
        else:
            location = "(Location not available)"
        # print(location)
        link = "Details: https://hk.jobsdb.com" + job.find("a")["href"]
        # print(link)
        jobInfo = "\n".join([jobTitle, company, location, link])
        jobs.append(jobInfo)
    jobList = "\n\n".join(jobs)
    return(jobList)

# Enter what kind of job you want to search here
print(jobSearch(""))