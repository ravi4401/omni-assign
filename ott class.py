class StreamingPlatform:
    def __init__(self, name, domain=None, live=None):
        self.name = name
        self.domain = domain
        self.live = live

    def __str__(self):
        return f"Name: {self.name}\nDomain: {self.domain}\nLive: {self.live}\n"


#StreamingPlatform class 
disney = StreamingPlatform(name="Disney", domain="Entertainment", live="Sports")
jio_tv = StreamingPlatform(name="Jio TV", domain="Education", live="Python")
amazon = StreamingPlatform(name="Amazon", domain="E-commerce", live="Selling")
flipkart = StreamingPlatform(name="Flipkart", live="Buying")
star_maa = StreamingPlatform(name="Star Maa", domain="Asking")

print("ott_disney:")
print(disney)

