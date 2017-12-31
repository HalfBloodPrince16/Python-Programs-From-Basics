import random
import urllib.request

def downloader(url):
    name = random.randrange(0,1000)
    fullname = str(name)+".jpg"
    urllib.request.urlretrieve(url,fullname)
    return;

downloader("https://www.google.co.in/imgres?imgurl=https%3A%2F%2Fstatic.pexels.com%2Fphotos%2F67636%2Frose-blue-flower-rose-blooms-67636.jpeg&imgrefurl=https%3A%2F%2Fwww.pexels.com%2Fsearch%2Fflower%2F&docid=5UbOpOqf9qM23M&tbnid=KMrijfvWvKaMNM%3A&vet=10ahUKEwjywcbg5bTYAhUNTo8KHcdkDmwQMwi7ASgBMAE..i&w=4928&h=3264&bih=615&biw=1185&q=images&ved=0ahUKEwjywcbg5bTYAhUNTo8KHcdkDmwQMwi7ASgBMAE&iact=mrc&uact=8")