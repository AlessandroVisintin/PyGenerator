import shutil
import site
from pathlib import Path

from PyGenerator import constants as const


def update_syspath(path:str) -> None:
	"""
	
	Add project permanently to sys.path
	
	Args:
		path : absolute path to project.
	
	"""
	
	# get userdir position
	userdir = site.getusersitepackages()
	# create directory if not exists
	Path(userdir).mkdir(parents=True, exist_ok=True)
	# create script file
	usercustomize = f'{userdir}/usercustomize.py'
	syspath = f'{userdir}/syspath.txt'
	if not Path(usercustomize).is_file():
		with open(usercustomize, 'w') as f:
			f.write('import sys\n\n')
			f.write('syspath = []\n')
			f.write(f'with open("{syspath}", "r") as f:\n')
			f.write('syspath = [line.strip() for line in f if not line == "\n"]\n')
			f.write('sys.path.extend(syspath)\n')
	# add path to file	
	with open(syspath, 'a+') as f:
		f.write(f'{Path(path).resolve()}\n')


def license(metadata:dict) -> str:
	"""
	
	Returns the license with custom values.
	
	Args:
		metadata : Information about the project 
			(See project() for details on its structure)
			
			Expects:
				project.license : name of the license
				
				'MIT':
					creator.name : name of project creator
					project.year : year of creation

	Returns:
		generated license
	
	Raises:
		KeyError, ValueError
	"""
	
	if metadata['project']['license'] == 'MIT':
		return const.LICENSES['MIT'].format(
			fullname=metadata['creator']['name'], year=metadata['project']['year'])
	else:
		raise ValueError('License not found')
			
		
	
def project(metadata:dict, path:str, 
				syspath:bool=False, overwrite:bool=False) -> None:
	""" 
	
	Generate new project folder
	
	Args:
		metadata : dictionary with project information
			creator :
				 name (string) : name of the creator
				 mail (string) : mail of the creator
				 social (dict) : {name : url, ...}
			project :
				name (string) : name of the project (folder-friendly)
				year (integer) : year of creation 
				version (string) : version of the project
				license (string) : name of the license
		path : path where to create the project folder.
		syspath : add project to syspath. Default to False.
		overwrite : overwrites folder if True, stop otherwise.
	
	Raises:
		KeyError

	"""

	prj = metadata["project"]["name"]
	src = f'{path}/{prj}'
	
	if Path(src).is_dir():
		if not overwrite:
			print(f'{src} already exists.')
			return
		shutil.rmtree(src)

	name = Path(f'{src}/{prj}') 
	name.mkdir(parents=True, exist_ok=True)
	file = name / '__init__.py'
	with file.open("w") as f:
		pass
	file = name / f'{prj}.py'
	with file.open("w") as f:
		pass

	tests = Path(f'{src}/tests')
	tests.mkdir(parents=True, exist_ok=True)
	file = tests / f'{prj}_tests.py'
	with file.open("w") as f:
		pass

	file = Path(src) / '.gitignore' 
	with file.open("w") as f:
		f.write(const.GITIGNORE)

	file = Path(src) / 'LICENSE.txt' 
	with file.open("w") as f:
		f.write(license(metadata))

	file = Path(src) / 'README.md' 
	with file.open("w") as f:
		social = [f'[{k}]({v})'for k,v in metadata['creator']['social'].items()]
		f.write(const.README.format(
					name = prj,
					creator = metadata['creator']['name'],
					mail = metadata['creator']['mail'],
					social = ' '.join(social),
					licens = metadata['project']['license'],
				))

	file = Path(src) / 'setup.cfg'
	with file.open("w") as f:
		f.write(const.SETUP['cfg'].format(
				name = prj,
				version = metadata['project']['version'],
				licens = metadata['project']['license']
			))

	file = Path(src) / 'setup.py' 
	with file.open("w") as f:
		f.write(const.SETUP['py'])
	
	if syspath:
		update_syspath(src)
