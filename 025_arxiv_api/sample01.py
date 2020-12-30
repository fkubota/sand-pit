import arxiv

get_article_func = arxiv.query(query='cs',
                               max_results=100,
                               sort_by='submittedDate',
                               iterative=True)


for article in get_article_func():
    url = article['arxiv_url']
    title = article['title']
    abst = article['summary']
    day = article["published_parsed"].tm_mday

