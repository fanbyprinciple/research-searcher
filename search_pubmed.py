from Bio import Entrez

def search_pubmed(query, email, max_results=200):
    Entrez.email = email  # Always provide your email when using Entrez
    handle = Entrez.esearch(db="pubmed", term=query, retmax=max_results)
    record = Entrez.read(handle)
    handle.close()

    # Fetch details of the articles
    id_list = record['IdList']
    handle = Entrez.efetch(db="pubmed", id=id_list, retmode="xml")
    records = Entrez.read(handle)['PubmedArticle']
    handle.close()
    
    # Parse records to extract titles and URLs
    articles = []
    for article in records:
        title = article['MedlineCitation']['Article']['ArticleTitle']
        pmid = article['MedlineCitation']['PMID'].rstrip()
        url = f"https://pubmed.ncbi.nlm.nih.gov/{pmid}/"
        articles.append({'title': title, 'url': url})

    return articles

# Usage
email = "ayana98pillai@gmail.com"
query = "learning in pair of fishes"
results = search_pubmed(query, email)
for result in results:
    print(result['title'])
    print(result['url'])
    print()  # Adds a newline for better readability between articles
