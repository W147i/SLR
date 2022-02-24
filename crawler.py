from selenium import webdriver

urls = []
urls.append("https://arxiv.org/")
urls.append("https://ieeexplore.ieee.org/Xplore/home.jsp")
urls.append("https://www.sciencedirect.com/")
urls.append("https://onlinelibrary.wiley.com/")
urls.append("https://www.sciencedirect.com/")
urls.append("https://dl.acm.org/")

browser = webdriver.Chrome()
for i in urls: 
    browser.get(i)
browser.find