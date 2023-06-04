#coding=utf-8
# 功能:爬前程无忧网站
# 创建者:俺
import csv,urllib.request,re,requests,os # 导入模块

def qianchengwuyou(job_name, pages,cookie):
    try:
        os.makedirs("前程无忧\\")
    except Exception as e:
        print(f"文件夹已创建\n{e}")
    with open(f'前程无忧\\{job_name}.csv', mode='a', encoding='utf-8', newline='') as f: 
        csv_w = csv.DictWriter(f, fieldnames=['岗位', '公司', '学历', '工作经验', '月薪', '待遇', '岗位链接'])
        csv_w.writeheader()  # 写入标题
        
        for page in range(1,pages+1):
            job_name = urllib.parse.quote(job_name)  # 将汉字编码为URL编码
            url = f'https://we.51job.com/api/job/search-pc?api_key=51job&timestamp=1685494731&\
keyword={job_name}&searchType=2&function=&industry=&jobArea=000000&jobArea2=&landmark=&metro=&salary=&workYear=&degree=&companyType=&companySize=&jobType=&issueDate=&sortType=0&\
pageNum={page}&requestId=b340935dc543bf27150fc65f985b9757&pageSize=20&source=1&accountId=211428919&pageCode=sou%7Csou%7Csoulb&u_atoken=d93ec7ff-3026-4392-b362-07d78723002b&u_asession=01AUV9y6IguLvqDAGId08zrHovErSJeeB_HbJnqBHkLzK5b35qq4czJHtkC-Ay17lAX0KNBwm7Lovlpxjd_P_q4JsKWYrT3W_NKPr8w6oU7K9p-zYy0ZLGdoA3rDHy3m-fYAieK8g9kWtgqoeh4E6vb2BkFo3NEHBv0PZUm6pbxQU&u_asig=05NvLLX17Yh0EcOR5Ex57VXRCAQi0EGynecsTtDEtbSMW2rG_343uvZ2KCEvHwIKrTLwqZoHDSwQF1sk-eOeQ2_KIvZ3YTQk-7ZJljFJoiVLX_PAyMrYq5of0E-gEyQWzzImDM0HP0PFoNd8lR9HcgThidLPn14g3tA7bnsYv5yST9JS7q8ZD7Xtz2Ly-b0kmuyAKRFSVJkkdwVUnyHAIJzUGQ_GOuXo4W_Wm4v7LblNqgn5Nto23N5_HqN8mmxRykLTc6IvlIB0PEAiUn81TNPu3h9VXwMyh6PgyDIVSG1W9-EL58he-HABy_Tqg7XJMd6UBi2EXEzpguGgi5tijWlgb4amiDmymU7j5ycviTotX16iDsF45IyWhB4G5Jof6QmWspDxyAEEo4kbsryBKb9Q&u_aref=vnsqyUGxBSxhDhu65tyUYE3ZDlc%3D'
            headers = {
                'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebK:it/537.36 (KHTML, like Gecko) Chrome/113.0.0.0 Safari/537.36',
                'cookie' : cookie,
                'Referer' : url
            }
            # 不登录只能爬一页
            response = requests.get(url=url, headers=headers)
            jobs = re.findall(
                '"workYearString":"(.*?)","degreeString":"(.*?)","industryType1Str".*?"fullCompanyName":"(.*?)","companyLogo".*?"jobHref":"(.*?)","companyHref".*?"jobName":"(.*?)","jobTags":(.*?),"jobNumString".*?"provideSalaryString":"(.*?)","issueDateString"',
                response.text)
            
            for job in jobs:
                csv_w.writerow({'岗位': job[4],
                                '公司': job[2],
                                '学历': job[1],
                                '工作经验': job[0],
                                '月薪': job[6],
                                '待遇': job[5],
                                '岗位链接': job[3]})
    print("\n爬取成功")

if __name__ == "__main__" :
    job_name = input("请输入需要查找的职位名称:")
    pages = eval(input("请输入需要爬取的页面数量:"))
    cookie = input("请输入登录后的cookie:\n")
    qianchengwuyou(job_name,pages,cookie)