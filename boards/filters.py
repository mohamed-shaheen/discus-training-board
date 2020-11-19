import django_filters
from .models import Topic




class TopicFilter(django_filters.FilterSet):
    subject = django_filters.CharFilter(lookup_expr='icontains')
    #board = django_filters.CharFilter(lookup_expr='icontains')
    class Meta:
        model = Topic
        fields = ['subject']
        #exclude = []

