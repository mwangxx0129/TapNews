'''
test news_api_client
'''
import news_api_client as client

def test_basic():
    '''
    test news_api_client
    '''
    news = client.getNewsFromSource()
    print news
    assert len(news) > 0
    news = client.getNewsFromSource(sources=['cnn'], sort_by='top')
    assert len(news) > 0
    print 'test_basic passed!'

if __name__ == "__main__":
    test_basic()
    