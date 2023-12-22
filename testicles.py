from pathlib import Path


empty_bottle = Path("/home/vansha/Desktop/spare_folder")

for this in empty_bottle.glob("*/**"):
    eminem = this.parts
    print(type(eminem))

