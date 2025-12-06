from django.shortcuts import render, get_object_or_404, redirect
from events.models import Event, Category, Participant
from events.forms import EventForm, CategoryForm, ParticipantForm, ParticipantSelectionForm
from django.utils import timezone
from django.db.models import Q, Count

# home
def home(request):
    return render(request, 'home.html')

# dashboard
def dashboard(request):
    today = timezone.now().date()
    agg = Event.objects.aggregate(total_participants=Count('participants', distinct=True))
    total_participants = agg.get('total_participants') or 0

    total_events = Event.objects.count()
    upcoming_events = Event.objects.filter(date__gte=today).count()
    past_events = Event.objects.filter(date__lt=today).count()

    view = request.GET.get('view', 'all')

    events_qs = Event.objects.select_related('category').prefetch_related('participants').order_by('date')

    if view == 'upcoming':
        events = events_qs.filter(date__gte=today)
    elif view == 'past':
        events = events_qs.filter(date__lt=today)
    else:
        events = events_qs

    todays_events = events_qs.filter(date=today)

    context = {
        'total_participants': total_participants,
        'total_events': total_events,
        'upcoming_events': upcoming_events,
        'past_events': past_events,
        'events': events,
        'todays_events': todays_events,
        'view': view,
    }
    return render(request, 'dashboard.html', context)


# event
def event_list(request):
    query = request.GET.get('q', '').strip()
    category_id = request.GET.get('category', '').strip()
    start = request.GET.get('start', '').strip()
    end = request.GET.get('end', '').strip()

    events = Event.objects.select_related('category').prefetch_related('participants').order_by('date')

    # search
    if query:
        events = events.filter(Q(name__icontains=query) | Q(location__icontains=query))

    # category filter
    if category_id:
        try:
            events = events.filter(category_id=int(category_id))
        except ValueError:
            pass

    # date range filter
    if start and end:
        events = events.filter(date__range=[start, end])
    elif start:
        events = events.filter(date__gte=start)
    elif end:
        events = events.filter(date__lte=end)

    categories = Category.objects.all()

    context = {
        'events': events,
        'request': request,
        'categories': categories,
        'selected_category': category_id,
        'start_date': start,
        'end_date': end,
        'query': query,
    }
    return render(request, 'event_list.html', context)


def event_detail(request, id):
    event = get_object_or_404(Event.objects.select_related('category').prefetch_related('participants'), id=id)
    return render(request, 'event_detail.html', {'event': event})

def event_create(request):
    if request.method == 'POST':
        form = EventForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('event_list')
    else:
        form = EventForm()
    return render(request, 'event_form.html', {'form': form})

def event_update(request, id):
    event = get_object_or_404(Event, id=id)
    if request.method == 'POST':
        form = EventForm(request.POST, instance=event)
        if form.is_valid():
            form.save()
            return redirect('event_detail', id=id)
    else:
        form = EventForm(instance=event)
    return render(request, 'event_form.html', {'form': form})

def event_delete(request, id):
    event = get_object_or_404(Event, id=id)
    event.delete()
    return redirect('event_list')


# category
def category_list(request):
    categories = Category.objects.all()
    return render(request, 'category_list.html', {'categories': categories})

def category_create(request):
    if request.method == 'POST':
        form = CategoryForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('category_list')
    else:
        form = CategoryForm()
    return render(request, 'category_form.html', {'form': form})

def category_update(request, id):
    category = get_object_or_404(Category, id=id)
    if request.method == 'POST':
        form = CategoryForm(request.POST, instance=category)
        if form.is_valid():
            form.save()
            return redirect('category_list')
    else:
        form = CategoryForm(instance=category)
    return render(request, 'category_form.html', {'form': form})

def category_delete(request, id):
    category = get_object_or_404(Category, id=id)
    category.delete()
    return redirect('category_list')

# participant
def participant_list(request):
    participants = Participant.objects.all()
    return render(request, 'participant_list.html', {'participants': participants})

def participant_create(request):
    if request.method == 'POST':
        form = ParticipantForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('participant_list')
    else:
        form = ParticipantForm()
    return render(request, 'participant_form.html', {'form': form})

def participant_update(request, id):
    participant = get_object_or_404(Participant, id=id)
    if request.method == 'POST':
        form = ParticipantForm(request.POST, instance=participant)
        if form.is_valid():
            form.save()
            return redirect('participant_list')
    else:
        form = ParticipantForm(instance=participant)
    return render(request, 'participant_form.html', {'form': form})

def participant_delete(request, id):
    participant = get_object_or_404(Participant, id=id)
    participant.delete()
    return redirect('participant_list')

# Add participants to event
def event_add_participants(request, id):
    event = get_object_or_404(Event, id=id)
    
    if request.method == 'POST':
        form = ParticipantSelectionForm(request.POST, event=event)
        if form.is_valid():
            existing_participants = form.cleaned_data.get('existing_participants', [])
            for participant in existing_participants:
                event.participants.add(participant)
            
            if form.cleaned_data.get('add_new'):
                new_name = form.cleaned_data.get('new_participant_name')
                new_email = form.cleaned_data.get('new_participant_email')
                
                participant, created = Participant.objects.get_or_create(
                    email=new_email,
                    defaults={'name': new_name}
                )
                event.participants.add(participant)
            
            return redirect('event_detail', id=id)
    else:
        form = ParticipantSelectionForm(event=event)
    
    context = {
        'event': event,
        'form': form,
    }
    return render(request, 'event_add_participants.html', context)

# search
def search_events(request):
    query = request.GET.get('q', '').strip()
    results = Event.objects.select_related('category').prefetch_related('participants').filter(
        Q(name__icontains=query) | Q(location__icontains=query)
    ) if query else Event.objects.none()
    return render(request, 'search_results.html', {'results': results, 'query': query})
