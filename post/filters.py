from post.models import Post
import django_filters


class PostFilter(django_filters.FilterSet):
    year_created = django_filters.NumberFilter(name='post_date_created',
                                               label='year created',
                                               lookup_expr='year',)
    month_created = django_filters.NumberFilter(name='post_date_created',
                                                label='month created',
                                                lookup_expr='month',)
    day_created = django_filters.NumberFilter(name='post_date_created',
                                              label='day created',
                                              lookup_expr='day', )
    class Meta:
        model = Post
        fields = [
            'year_created',
            'month_created',
            'day_created',
        ]
