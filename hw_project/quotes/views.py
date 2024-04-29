from django.shortcuts import redirect, render, get_object_or_404
from django.core.paginator import Paginator
from django.contrib.auth.decorators import login_required
from .forms import TagForm, QuoteForm, AuthorForm
from .models import Tag, Quote, Author
from django.db.models import Count




def main(request, page=1):
    quotes = Quote.objects.all().order_by('id')
    per_page = 10
    paginator = Paginator(quotes, per_page)
    quotes_on_page = paginator.page(page)

    return render(request, "quotes/index.html", context={"quotes": quotes_on_page, 'paginator': paginator})






def list_author(request, author_name):
    author = get_object_or_404(Author, fullname=author_name)
    return render(request, 'author.html', {'author': author})

def tag_detail(request, tag_name):
    tag = get_object_or_404(Tag, name=tag_name)
    quotes = Quote.objects.filter(tags=tag).order_by("-created_at")
    return render(request, 'quotes/tag_detail.html', {'tag': tag, 'quotes': quotes})


def author_quotes(request, author_name):
    author = get_object_or_404(Author, name=author_name)
    quotes = Quote.objects.filter(authors=author)
    return render(request, 'quotes/author_quote.html', {'author': author, 'quotes': quotes})

@login_required
def tag(request):
    if request.method == 'POST':
        form = TagForm(request.POST)
        if form.is_valid():
            tag = form.save(commit=False)
            tag.author=request.user
            tag.save()
            return redirect(to='quotes:main')
        else:
            return render(request, 'quotes/tag.html', {'form': form})

    return render(request, 'quotes/tag.html', {'form': TagForm()})


@login_required
def add_quote(request):
    if request.method == 'POST':
        form = QuoteForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('/')
    else:
        form = QuoteForm()

    return render(request, 'quotes/quote.html', {'form': form})

@login_required
def detail(request, quote_id):
    quote = get_object_or_404(Quote, pk=quote_id, author=request.user)
    return render(request, 'quotes/detail.html', {"quote": quote})


@login_required
def set_quote(request, quote_id):
    Quote.objects.filter(pk=quote_id, author=request.user).update(done=True)
    return redirect(to='quotes:main')


@login_required
def delete_quote(request, quote_id):
    Quote.objects.get(pk=quote_id, author=request.user).delete()
    return redirect(to='quotes:main')


@login_required
def add_author(request):
    if request.method == 'POST':
        form = AuthorForm(request.POST)
        if form.is_valid():
            author = form.save(commit=False)
            author.user = request.user
            author.save()
            return redirect('/')
    else:
        form = AuthorForm()
    return render(request, 'quotes/add_author.html', {'form': form})

@login_required
def add_tag(request):
    if request.method == 'POST':
        form = TagForm(request.POST)
        if form.is_valid():
            tag = form.save(commit=False)
            tag.user = request.user
            tag.save()
            return redirect('/')
    else:
        form = TagForm()
    return render(request, 'quotes/add_tag.html', {'form': form})

