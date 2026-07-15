import os
import struct

INPUT_FOLDER = "."
OUTPUT_FOLDER = "dds_output"

os.makedirs(OUTPUT_FOLDER, exist_ok=True)

for filename in os.listdir(INPUT_FOLDER):
    if not filename.lower().endswith(".aetex"):
        continue

    input_path = os.path.join(INPUT_FOLDER, filename)

    with open(input_path, "rb") as f:
        # Read DDS offset stored at 0x2C
        f.seek(0x2C)
        dds_offset = struct.unpack("<I", f.read(4))[0]

        # Read DDS data
        f.seek(dds_offset)
        dds_data = f.read()

    output_name = os.path.splitext(filename)[0] + ".dds"
    output_path = os.path.join(OUTPUT_FOLDER, output_name)

    with open(output_path, "wb") as out:
        out.write(dds_data)

    print(f"Converted {filename} -> {output_name} (DDS offset: 0x{dds_offset:X})")
    
print("Done!")