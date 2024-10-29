import webbrowser

# 读取txt文件
with open(r"E:\\240821项目跟进\\项目5-免疫相关的肠癌风险预后模型构建及验证-宋荣峰\\articles.txt") as file:
    articles_lists = file.readlines()
    # print(articles_lists[5])


# for article in articles_lists[31:37]:
#     article = article.strip()
#     if article:
#         search_url = f"https://pubmed.ncbi.nlm.nih.gov/?term={article}&filter=pubt.review"
#         webbrowser.open(search_url)