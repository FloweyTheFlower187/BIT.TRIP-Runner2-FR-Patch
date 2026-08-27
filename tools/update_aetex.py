import os
import struct

AETEX_FOLDER = "."
DDS_FOLDER = "dds_output"
OUTPUT_FOLDER = "aetex_updated"

os.makedirs(OUTPUT_FOLDER, exist_ok=True)

for filename in os.listdir(AETEX_FOLDER):
    if not filename.lower().endswith(".aetex"):
        continue

    aetex_path = os.path.join(AETEX_FOLDER, filename)
    dds_name = os.path.splitext(filename)[0] + ".dds"
    dds_path = os.path.join(DDS_FOLDER, dds_name)

    if not os.path.exists(dds_path):
        print(f"Skipping {filename}: {dds_name} not found.")
        continue

    with open(aetex_path, "rb") as f:
        aetex_data = f.read()

    # Read DDS offset (little-endian uint32 at 0x2C)
    dds_offset = struct.unpack_from("<I", aetex_data, 0x2C)[0]

    with open(dds_path, "rb") as f:
        dds_data = f.read()

    # Preserve everything before the DDS, replace everything after
    new_aetex = aetex_data[:dds_offset] + dds_data

    output_path = os.path.join(OUTPUT_FOLDER, filename)
    with open(output_path, "wb") as f:
        f.write(new_aetex)

    print(f"Updated {filename} using {dds_name}")

print("Done!")