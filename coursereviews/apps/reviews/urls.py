from django.conf.urls import patterns, url

from reviews import api

urlpatterns = patterns('reviews.views',
    url(r'^review/new$', 'create', name='new_review'),  # noqa
    url(r'^review/(?P<review_id>\d+)$', 'edit', name='edit_review'),
    url(r'^review/(?P<review_id>\d+)/delete$', 'delete', name='delete_review'),

    url(r'^course/(?P<course_slug>[-\w\d]+)$', 'course_detail', name='course_detail'),
    url(r'^professor/(?P<prof_slug>[-\w\d]+)$', 'prof_detail', name='prof_detail'),
    url(r'^course/(?P<course_slug>[-\w\d]+)/(?P<prof_slug>[-\w\d]+)$',
        'prof_course_detail',
        name='prof_course_detail'),

    url(r'^search$', 'search', name="search"),

    url(r'^beta/catalog', 'catalog', name='catalog'),
)

urlpatterns += patterns('reviews.api',
    url(r'^api/(?P<pk>\d+)/comment$', api.Comment.as_view()),  # noqa

    # GET all departments
    url(r'^api/departments$',
        api.Departments.as_view()),

    # GET all courses for a department
    url(r'^api/courses$',
        api.Courses.as_view()),

    # GET all professors for a department
    url(r'^api/professors$',
        api.Professors.as_view()),

    url(r'^api/search$',
        api.Search.as_view()),

    url(r'^api/review/options$',
        'new_review_course_options',
        name='new_review_course_options'),

    url(r'^api/course/(?P<course_slug>[-\w\d]+)/stats$',
        'course_detail_stats',
        name='course_detail_stats'),
    url(r'^api/professor/(?P<prof_slug>[-\w\d]+)/stats$',
        'prof_detail_stats',
        name='prof_detail_stats'),
    url(r'^api/course/(?P<course_slug>[-\w\d]+)/(?P<prof_slug>[-\w\d]+)/stats$',
        'prof_course_detail_stats',
        name='prof_course_detail_stats'),
    url(r'^api/(?P<review_id>\d+)/vote$', 'vote', name='vote_review'),
    url(r'^api/(?P<review_id>\d+)/flag$', 'flag', name='flag_review'),
)
