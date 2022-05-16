import xml.etree.ElementTree as ET
import os

DATASET_XML_DIR = "erddap/content/datasets.xml"
SPLITTED_DATASET_XML_DIR = "erddap/content/datasets"

if not os.path.exists(DATASET_XML_DIR):
    os.makedirs(DATASET_XML_DIR)

erddap = ET.iterparse(DATASET_XML_DIR)
for event, elem in erddap:
    if elem.tag == "dataset":
        datasetid = elem.attrib["datasetID"]
        filename = format(f"{datasetid}.xml")
        with open(os.path.join(SPLITTED_DATASET_XML_DIR, filename), "wb") as f:
            f.write(ET.tostring(elem))
