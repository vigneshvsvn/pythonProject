"""
✅ main.py skeleton
✅ Sample schema.xsd
✅ Sample transform.xslt
✅ 2 XML files (1 valid, 1 invalid) zipped in input.zip
✅ Logging and file handling setup

mkdir -p xml_tool/data xml_tool/output/transformed xml_tool/logs
cd xml_tool
touch main.py

"""

import os
import zipfile
import logging
from pathlib import Path
from lxml import etree

# Paths
BASE = Path(__file__).parent
ZIP_PATH = BASE / "data" / "input.zip"
XSD_PATH = BASE / "data" / "schema.xsd"
XSLT_PATH = BASE / "data" / "transform.xslt"
OUTPUT_DIR = BASE / "output" / "transformed"
LOG_FILE = BASE / "logs" / "run.log"

# Setup logging
logging.basicConfig(filename=LOG_FILE, level=logging.INFO, format="%(asctime)s - %(levelname)s - %(message)s")

# Load Schema
logging.info("Loading XSD schema")
with open(XSD_PATH, 'rb') as f:
    schema_doc = etree.XML(f.read())
    schema = etree.XMLSchema(schema_doc)

# Load XSLT
logging.info("Loading XSLT")
with open(XSLT_PATH, 'rb') as f:
    xslt_root = etree.XML(f.read())
    transform = etree.XSLT(xslt_root)

# Ensure output directory
OUTPUT_DIR.mkdir(parents=True, exist_ok=True)

# Process each XML file in the ZIP
with zipfile.ZipFile(ZIP_PATH, 'r') as zip_ref:
    for name in zip_ref.namelist():
        if not name.endswith(".xml"):
            continue

        logging.info(f"Processing file: {name}")
        xml_data = zip_ref.read(name)
        xml_doc = etree.XML(xml_data)

        # Validate
        if not schema.validate(xml_doc):
            logging.error(f"Validation failed for {name}")
            continue
        logging.info(f"{name} is valid")

        # Transform
        result = transform(xml_doc)
        output_file = OUTPUT_DIR / (Path(name).stem + ".html")
        with open(output_file, 'wb') as f:
            f.write(etree.tostring(result, pretty_print=True, method="html"))
        logging.info(f"Saved transformed file: {output_file.name}")