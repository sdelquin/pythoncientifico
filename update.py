import datetime
import os
import shlex
import shutil
import subprocess
from pathlib import Path

timestamp = datetime.datetime.now().strftime('%y%m%dT%H%M')
backup_folder = Path('backup')

if not backup_folder.exists():
    os.makedirs(backup_folder)
    readme = backup_folder / 'README'
    readme.write_text('''Esta carpeta contiene una copia de seguridad de los
notebooks cada vez que se actualiza el repositorio. Es posible que algunas
imágenes no se vean bien o algunas sentencias no funcionen porque la ruta a
los ficheros es relativa al raíz del proyecto.''')

backup_folder /= f'backup_{timestamp}'
os.makedirs(backup_folder, exist_ok=True)

for notebook in Path('.').glob('*.ipynb'):
    shutil.copy(notebook, backup_folder)

cmd = 'git checkout -- .'
subprocess.run(shlex.split(cmd))

cmd = 'git pull'
subprocess.run(shlex.split(cmd))
