import subprocess
import yaml

# Load config
with open('config/config.yaml', 'r') as f:
    config = yaml.safe_load(f)

def run_script(script_name):
    result = subprocess.run(['python', script_name], capture_output=True, text=True)
    print(result.stdout)
    if result.returncode != 0:
        print(result.stderr)

scripts = [
    'scripts/face_detect.py',
    'scripts/depth.py',
    'scripts/background_removal.py',
    'scripts/reconstruct_3d.py'
]

for script in scripts:
    run_script(script)
