from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from django.http import JsonResponse
from .models import Board, BoardImage
from .forms import BoardCreateForm

@login_required
def board_list(request):
    """Display user's boards"""
    boards = Board.objects.filter(user=request.user)
    return render(request, 'boards/board_list.html', {
        'boards': boards
    })

@login_required
def board_create(request):
    """Create a new board"""
    if request.method == 'POST':
        form = BoardCreateForm(request.POST)
        if form.is_valid():
            board = form.save(commit=False)
            board.user = request.user
            board.save()
            messages.success(request, f'Board "{board.title}" created successfully!')
            return redirect('board_detail', pk=board.pk)
    else:
        form = BoardCreateForm()
    
    return render(request, 'boards/board_create.html', {'form': form})

@login_required
def board_detail(request, pk):
    """Display a specific board with its images"""
    board = get_object_or_404(Board, pk=pk, user=request.user)
    images = board.images.all().order_by('-uploaded_at')
    
    return render(request, 'boards/board_detail.html', {
        'board': board,
        'images': images
    })

@login_required
def upload_images(request, board_pk):
    """Handle image uploads to a board"""
    board = get_object_or_404(Board, pk=board_pk, user=request.user)
    
    if request.method == 'POST' and request.FILES.getlist('images'):
        uploaded_count = 0
        for image_file in request.FILES.getlist('images'):
            board_image = BoardImage.objects.create(
                board=board,
                image=image_file,
                original_filename=image_file.name
            )
            uploaded_count += 1
        
        messages.success(request, f'{uploaded_count} image(s) uploaded successfully!')
        return redirect('board_detail', pk=board.pk)
    
    return redirect('board_detail', pk=board.pk)
