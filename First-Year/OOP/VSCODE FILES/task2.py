class NewspaperHeadlines:
    def __init__(self):
        self.headlines = []
        self.subscribers = []

    def allHeadline(self):
        return self.headlines

    def latestHeadline(self):
        if( len (self.headlines) == 0) :
            return ''
        return self.headlines[-1]

    def addHeadline(self, headline):
        self.headlines.append(headline)
        self._update_subscribers()

    def subscribe(self, subscriber):
        self.subscribers.append(subscriber)

    def _update_subscribers(self):
        for subscribe in self.subscribers:
            subscribe()
            
class NewspaperSubscriber:
    def __init__(self, NewspaperHeadlines):
        self.NewspaperHeadlines = NewspaperHeadlines
    def __call__(self):
        #print(self.NewspaperHeadlines.allHeadline())
        print('Latest headline:', self.NewspaperHeadlines.latestHeadline())
    

h = NewspaperHeadlines()
s = NewspaperSubscriber(h)

h.subscribe(s)
h.addHeadline("Severe weather warning for tomorrow.")
h.addHeadline("Sever weather warning cancelled.")
