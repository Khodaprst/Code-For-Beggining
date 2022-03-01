from django.shortcuts import render
from datetime import date
from django.http import HttpRequest

all_posts = [
    {
        'slug': 'learning-django',
        'title': 'django course',
        'author': 'Amir Khodaparast',
        'image': 'django.jpg',
        'date': date(2022, 2, 10),
        'short_description': 'this is django course from zero to hero',
        'content': """
            just started & so exited!
        """
    },
    {
        'slug': 'learning-python',
        'title': 'python course',
        'author': 'Amir Khodaparast',
        'image': 'python.jpg',
        'date': date(2022, 2, 9),
        'short_description': 'this is python course from zero to hero',
        'content': """
            Programming Python since 2018 started with Jadi Mirmirani in Maktabkhooneh.com, and also Ali Mesforoush on that site and then by Nabegheha.com;
            I'm really hope this programming take me to a better place to build new future.
            -AmirHosein Khodaparast.
        """
    },
    {
        'slug': 'learning-machine-learning',
        'title': 'ml course',
        'author': 'Amir Khodaprst',
        'image': 'ml.png',
        'date': date(2022, 2, 2),
        'short_description': 'this is ml course from zero to hero',
        'content': """
            learning ml since november 2021 and so exited to master of it.
            Lorem ipsum dolor sit amet, consectetur adipisicing elit. Ad aliquid dicta, eius eos eum eveniet
            perspiciatis quod soluta veritatis? Alias atque ducimus facere odit pariatur! Alias, aspernatur consequuntur
            deleniti est fugit officiis porro quia saepe tenetur, veniam veritatis voluptatem voluptatum?
        """
    },
]


def get_date(post):
    return post['date']


def index(request):
    sorted_posts = sorted(all_posts, key=get_date)
    latest_posts = sorted_posts[-2:]
    return render(request, 'blog/index.html', {
        'latest_posts': latest_posts
    })


def posts(request):
    return render(request, 'blog/all-posts.html', {
        'all_posts': all_posts
    })

def instagram(request):
    render(request, 'templates/Instagram.html')
def E_mail(request):
    render(request, 'templates/Email.html')
def Telegram(request):
    render(request, 'templates/telegram.html')

def single_post(request, slug):
    post = next(post for post in all_posts if post['slug'] == slug)
    return render(request, 'blog/post-detail.html', {
        'post': post
    })