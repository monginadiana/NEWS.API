class Source:
    '''
    Source class to define source Objects
    '''

    def __init__(self,id,name,description,url,category,country,language):
        self.id =id
        self.name = name
        self.description = description
        self.url = url
        self.category = category
        self.country = country
        self.language = language
class Articles:
    '''
    Articles class to define articles objects
    '''
    def __init__(self,author,title,description,urlToImage, url, publishedAt):
        
        self.author = author
        self.title = title
        self.description = description
        self.url= url
        self.urlToImage = urlToImage
        self.publishedAt = publishedAt