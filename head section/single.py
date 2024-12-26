{%block seo_head%}
<title>{{ blog.meta_title }}</title>
<meta property="og:title" content="{{ blog.meta_title }}">
<meta name="twitter:title" content="{{ blog.meta_title }}">
{% if blog.index_status %}
<meta name="robots" content="index, follow, max-image-preview:large, max-snippet:-1, max-video-preview:-1">
{% else %}
<meta name="robots" content="noindex, nofollow">
{% endif %}
<meta name="description" content="{{blog.meta_description}}">
<meta property="og:description" content="{{blog.meta_description}}">
<meta name="twitter:description" content="{{blog.meta_description}}">
<meta itemprop="description" content="{{blog.meta_description}}">
<meta itemprop="name" content="{{ blog.meta_title }}">
<meta property="og:type" content="article" />
<meta property="article:published_time" content="{{blog.published_date|date:'Y-m-d\TH:i:sO'}}" />
<meta property="article:modified_time" content="{{blog.modification_date|date:'Y-m-d\TH:i:sO'}}" />
<meta name="author" content="Abdul Aouwal">
<meta property=" og:image:alt" content="{{ blog.meta_title }}">
<meta property="og:image:type" content="image/jpeg">
<meta name="twitter:card" content="summary_large_image">
{% if blog.featured_image %}
<meta name="twitter:image" content="https://zetechdigital.com{{blog.featured_image.url}}">
<meta property="og:image" content="https://zetechdigital.com{{blog.featured_image.url}}">
<meta itemprop="image" content="https://zetechdigital.com{{blog.featured_image.url}}">
{% else %}
<meta name="twitter:image" content="https://zetechdigital.com{% static  'images/zetech.jpg' %}">
<meta property="og:image" content="https://zetechdigital.com{% static  'images/zetech.jpg'%}">
<meta itemprop="image" content="https://zetechdigital.com{% static  'images/zetech.jpg' %}">
{% endif %}
<link rel="canonical" href="{{ request.build_absolute_uri }}">
{%endblock%}
