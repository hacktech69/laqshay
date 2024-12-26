
from deepface import DeepFace

# Paths to the images
image_with_glasses = "with glass.jpg" 
image_without_glasses = "no glass.jpg"   

try:
    # Perform face comparison
    result = DeepFace.verify(image_with_glasses, image_without_glasses)

    # Check the verification result
    if result["verified"]:
        print("The faces match! They are the same person.")
    else:
        print("The faces do not match. They are different persons.")
except Exception as e:
    print(f"An error occurred: {e}")
