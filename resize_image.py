import cv2

input_image_path = 'car.jpg' 


output_image_path = 'car1.jpg' 

new_width = 1912
new_height = 900

img = cv2.imread(input_image_path)

if img is None:
    print(f"Error: Could not load image at {input_image_path}")
else:
    
    upscaled_img = cv2.resize(img, (new_width, new_height), interpolation=cv2.INTER_CUBIC)

    cv2.imwrite(output_image_path, upscaled_img)

    print(f"Image upscaled and saved as {output_image_path}")

