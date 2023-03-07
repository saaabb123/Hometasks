# from bs4 import BeautifulSoup

# with open('file.xml') as f:
#     bs = BeautifulSoup(f,"xml")
#     content = bs.find_all("name")
#     for name in content:
#         print(name.text)

class Cat:
    paws = 4
    
    def run(self):
        print('Cat runs!')

    def meow(self):
        print('Meow!')
        self.run()
        print(self.paws)


barsik = Cat()

barsik.meow()
