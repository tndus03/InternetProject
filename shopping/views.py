from django.shortcuts import render
from .models import Puzzle

# Create your views here.
def index(request):
    puzzles = Puzzle.objects.all().order_by('-pk')

    return render(
        request,
        'shopping/index.html',
        {
            'puzzles' : puzzles,
        }
    )

def single_post_page(request, pk):
    puzzle = Puzzle.objects.get(pk=pk)

    return render(
        request,
        'shopping/single_post_page.html',
        {
            'puzzle': puzzle,
        }
    )