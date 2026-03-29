from datetime import timedelta
from django.utils import timezone

def calculate_priority(deadline):
    """
    Auto-calculate priority based on deadline.
    Returns: 'HIGH' if deadline < 1 day, 'MEDIUM' if deadline < 3 days, 'LOW' otherwise.
    """
    if not deadline:
        return 'LOW'
        
    now = timezone.now()
    time_left = deadline - now
    
    if time_left < timedelta(days=1):
        return 'HIGH'
    elif time_left < timedelta(days=3):
        return 'MEDIUM'
    else:
        return 'LOW'
