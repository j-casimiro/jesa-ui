import os
import shutil
import argparse
from jesa_ui.utils import COMPONENTS

def install_component(name: str, target_dir: str):
    os.makedirs(target_dir, exist_ok=True)

    if name not in COMPONENTS:
        print(f"component '{name}' not found.")
        return
    
    source = COMPONENTS[name]
    dest = os.path.join(target_dir, f'{name}.j2')

    if os.path.exists(dest):
        print(f"component '{name}' already exists at {dest}.")
        return

    shutil.copyfile(source, dest)
    print(f"installed '{name}' component to {dest}.")


def main():
    parser = argparse.ArgumentParser(description="install jesa-ui components.")
    parser.add_argument('command', choices=['install'], help="command to run")
    parser.add_argument('component', help="component name (e.g. 'button')")
    parser.add_argument('--to', default="./components", help="target dir to install into")

    args = parser.parse_args()

    if args.command == 'install':
        install_component(args.component, args.to)