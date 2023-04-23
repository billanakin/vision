import subprocess
import re
from my.image_net_classlist import image_net_classlist

def classify_image(image_path):
    proc = subprocess.Popen(["/home/anakinz/Vision/openvino_build/armv7l/Release/hello_classification", "/home/anakinz/Vision/trained_models/alexnet/FP32/alexnet.xml", image_path, "MYRIAD"], stdout=subprocess.PIPE)
    output = proc.stdout.read().decode("utf-8")
    rx_sequence = re.compile(r'(^\d+)\W+(0\.\d+)', re.MULTILINE)
    classifications = []
    for match in rx_sequence.finditer(output):
        classid = match[1]
        classid_description = image_net_classlist[classid]
        score = round(float(match[2]), 2)
        classifications.append([classid, classid_description, score])
    return classifications
