LICENSES = {
	'MIT' : (
		'Copyright (c) {year} {fullname}\n'
		'Permission is hereby granted, free of charge, to any person\n'
		'obtaining a copy of this software and associated documentation\n'
		'files (the "Software"), to deal in the Software without\n'
		'restriction, including without limitation the rights to use,\n'
		'copy, modify, merge, publish, distribute, sublicense, and/or sell\n'
		'copies of the Software, and to permit persons to whom the\n'
		'Software is furnished to do so, subject to the following\n'
		'conditions:\n\n'
		'The above copyright notice and this permission notice shall be\n'
		'included in all copies or substantial portions of the Software.\n\n'
		'THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND,\n'
		'EXPRESS OR IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES\n'
		'OF MERCHANTABILITY, FITNESS FOR A PARTICULAR PURPOSE AND\n'
		'NONINFRINGEMENT. IN NO EVENT SHALL THE AUTHORS OR COPYRIGHT\n'
		'HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER LIABILITY,\n'
		'WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING\n'
		'FROM, OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR\n'
		'OTHER DEALINGS IN THE SOFTWARE.\n'
	)
}


# link : [txt](url), image : ![txt](url), shell : ```sh\n{code}\n```
# italic : _txt_, bullets: * (\t*)
README = (
		'# {name}\n> ..short description..\n\n..longer description..\n\n'
		'## Installation\n..description..\n\n'
		'## Development setup\n..description..\n\n'
		'## Usage examples\n..description\n\n'
		'## Release History\n..description..\n\n'
		'## Meta\n{creator} - {mail}\n\nFind me: {social}\n\n'
		'Distributed under the {licens} license. See ``LICENSE.txt``.\n\n'
		'## Contributing\n..description..\n\n'
	)


GITIGNORE = (
	'# Local\n/local_*\n/data/*\n!/data/_*\n\n'
	'# Editors\n.vscode/\n.idea/\n\n'
	'# Vagrant\n.vagrant/\n\n'
	'# Mac/OSX\n.DS_Store\n\\n'
	'# Windows\nThumbs.db\n\n'
	'# Byte-compiled / optimized / DLL files\n__pycache__/\n*.py[cod]\n*$py.class\n\n'
	'# C extensions\n*.so\n\n'
	'# Distribution / packaging\n.Python\nbuild/\ndevelop-eggs/\ndist/\n'
		'downloads/\neggs/\n.eggs/\nlib/\nlib64/\nparts/\nsdist/\nvar/\n'
		'wheels/\n*.egg-info/\n.installed.cfg\n*.egg\nMANIFEST\n\n'
	'# PyInstaller\n*.manifest\n*.spec\n\n'
	'# Installer logs\npip-log.txt\npip-delete-this-directory.txt\n\n'
	'# Unit test / coverage reports\nhtmlcov/\n.tox/\n.nox/\n.coverage\n'
		'.coverage.*\n.cache\nnosetests.xml\ncoverage.xml\n*.cover\n'
		'.hypothesis/\n.pytest_cache/\n\n'
	'# Translations\n*.mo\n*.pot\n\n'
	'# Django stuff\n*.log\nlocal_settings.py\ndb.sqlite3\n\n'
	'# Flask stuff\ninstance/\n.webassets-cache\n\n'
	'# Scrapy stuff\n.scrapy\n\n'
	'# Sphinx documentation\ndocs/_build/\n\n'
	'# PyBuilder\ntarget/\n\n'
	'# Jupyter Notebook\n.ipynb_checkpoints\n\n'
	'# IPython\nprofile_default/\nipython_config.py\n\n'
	'# pyenv\n.python-version\n\n'
	'# celery beat schedule file\ncelerybeat-schedule\n\n'
	'# SageMath parsed files\n*.sage.py\n\n'
	'# Environments\n.env\n.venv\nenv/\nvenv/\nENV/\nenv.bak/\nvenv.bak/\n\n'
	'# Spyder project settings\n.spyderproject\n.spyproject\n\n'
	'# Rope project settings\n.ropeproject\n\n'
	'# mkdocs documentation\n/site\n\n'
	'# mypy\n.mypy_cache/\n.dmypy.json\ndmypy.json\n'
	)


SETUP = {
		'py': 'import setuptools\n\nsetuptools.setup()\n',
		'cfg': (
				'[metadata]\n'
				'name = local_{name}\n'
				'version = {version}\n'
				'long_description = file: README.md\n'
				'license = {licens}\n\n'
				'[options]\n'
				'packages =\n'
				'\t{name}\n'
				'#install_requires =\n'
				'\t# ...\n\n'
				'[options.packages.find]\n'
				'#exclude =\n'
				'#\ttests*\n'
			)
	}
