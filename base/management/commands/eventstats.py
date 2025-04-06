from django.core.management.base import BaseCommand
from django.utils import timezone
from base.models import Event, Type
from django.db.models import Count, Avg

class Command(BaseCommand):
    help = 'Show event statistics and analytics'

    def handle(self, *args, **options):
        total_events = Event.objects.count()
        active_events = Event.objects.filter(date__gte=timezone.now()).count()
        avg_participants = Event.objects.annotate(
            num_interested=Count('interested')
        ).aggregate(Avg('num_interested'))['num_interested__avg'] or 0
        
        popular_type = Type.objects.annotate(
            num_events=Count('event')
        ).order_by('-num_events').first()

        self.stdout.write("\nEvent Statistics\n")
        self.stdout.write(f"• Total events: {total_events}")
        self.stdout.write(f"• Avg. participants/event: {avg_participants:.1f}")
        
        if popular_type:
            self.stdout.write(f"• Most popular type: {popular_type.name} ({popular_type.num_events} events)")
        else:
            self.stdout.write("• No event types available")
            
        self.stdout.write("")