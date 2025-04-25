
import django
from django.conf import settings
from django.template import engines

# Step 1: Configure Django settings
settings.configure(
    DEBUG=True,
    TEMPLATES=[{
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': ['templates'],  # template folder
    }]
)

# Step 2: Initialize Django
django.setup()

# Step 3: Load the template
django_engine = engines['django']
template = django_engine.get_template('sample.html')

# Step 4: Context data to pass into the template
context = {
    'title': 'Django Template Demo',
    'name': 'Dhruvit'
}

# Step 5: Render the template
rendered_html = template.render(context)

# Step 6: Output the rendered HTML
print(rendered_html)
