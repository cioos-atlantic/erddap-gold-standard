#!/bin/bash
DATASET_XML_DIR="./config/datasets_xml/"
DATASET_XML_FILE="./config/datasets.xml"
​
echo '<?xml version="1.0" encoding="UTF-8" ?>' > ${DATASET_XML_FILE}
echo "<erddapDatasets>" >> ${DATASET_XML_FILE}
cat ${DATASET_XML_DIR}*.xml >> ${DATASET_XML_FILE}
echo "</erddapDatasets>" >> ${DATASET_XML_FILE}