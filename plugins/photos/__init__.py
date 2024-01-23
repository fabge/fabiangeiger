from pelican import signals
from pathlib import Path

def generate_photos_page(generator):
    content_path = generator.settings.get('PATH')
    photos_path = content_path + '/photos'

    for page in generator.pages:
        if page.metadata.get('template') == 'photos':
            photos = []
            for photo in Path(photos_path).iterdir():
                if photo.suffix in ['.jpg', '.jpeg', '.png']:
                    print(photo.relative_to(content_path))
                    photos.append(f'/{photo.relative_to(content_path)}')
            page.photos = sorted(photos, reverse=True)

def register():
    signals.page_generator_finalized.connect(generate_photos_page)
