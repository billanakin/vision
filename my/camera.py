import subprocess

def capture_image(output_image_path):
    subprocess.run(["raspistill", "-q", "100", "-rot", "180", "-o", output_image_path])
