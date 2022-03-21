import globals, vt

globals.cmd("Defender")
client = vt.Client("d0bab7a1c0b445725ff5ec801a2c59478d3526d4d740a708cbc1fc0c39d55a8c")
with open("/", "rb") as f:
    analysis = client.scan_file(f, wait_for_completion=True)