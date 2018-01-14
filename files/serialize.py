def serialize_image(image = None):
    if image != None:
        return {
            'image_url': image.image.url,
            'image_width': image.image_width,
            'image_height': image.image_height,
            'image_id': image.pk
            }
