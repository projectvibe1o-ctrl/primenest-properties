from pathlib import Path
from PIL import Image

source = Path('/home/ubuntu/webdev-static-assets')
target = Path('/home/ubuntu/primenest-properties/client/public/assets')
target.mkdir(parents=True, exist_ok=True)

raster_assets = {
    'primenest-hero.png': ('primenest-hero.webp', 1600, 900),
    'primenest-property-courtyard.png': ('primenest-property-courtyard.webp', 900, 675),
    'primenest-property-apartment.png': ('primenest-property-apartment.webp', 900, 675),
    'primenest-property-villa.png': ('primenest-property-villa.webp', 900, 675),
}

for source_name, (target_name, max_width, max_height) in raster_assets.items():
    image = Image.open(source / source_name).convert('RGB')
    image.thumbnail((max_width, max_height), Image.Resampling.LANCZOS)
    image.save(target / target_name, 'WEBP', quality=82, method=6)

mark = Image.open(source / 'primenest-mark.png').convert('RGBA')
mark.thumbnail((512, 512), Image.Resampling.LANCZOS)
mark.save(target / 'primenest-mark.png', 'PNG', optimize=True)
