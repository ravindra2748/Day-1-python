from django.utils import timezone
from datetime import timedelta
from .models import User

last_month = timezone.now() - timedelta(days=30)
inactive_users = User.objects.exclude(order__created_at__gte=last_month)
