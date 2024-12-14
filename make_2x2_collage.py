from PIL import Image

def create_collage(images, collage_size=(2, 2), output_filename='collage2.jpg', space=10, frame_color=(255, 255, 255), overall_frame_width=20):
    # Load images
    loaded_images = [Image.open(img) for img in images]

    # Assuming all images are the same size, get dimensions
    img_width, img_height = loaded_images[0].size

    # Calculate collage dimensions including spaces
    collage_width = (img_width * collage_size[0]) + (space * (collage_size[0] - 1))
    collage_height = (img_height * collage_size[1]) + (space * (collage_size[1] - 1))

    # Total dimensions for the collage with the overall frame
    total_width = collage_width + (overall_frame_width * 2)
    total_height = collage_height + (overall_frame_width * 2)

    # Create a new blank image for the collage with frame color
    collage = Image.new('RGB', (total_width, total_height), frame_color)

    # Paste images into the collage with specified space
    for index, img in enumerate(loaded_images):
        x = overall_frame_width + (index % collage_size[0]) * (img_width + space)
        y = overall_frame_width + (index // collage_size[0]) * (img_height + space)
        collage.paste(img, (x, y))

    # Save the collage to a file
    collage.save(output_filename)
    print(f'Collage saved as: {output_filename}')

# List of image file paths
image_files = ['1.jpeg', '2.jpeg', '3.jpeg', '4.jpeg']

# Create the collage with space, overall frame, and a white frame
create_collage(image_files, space=40, overall_frame_width=40)
