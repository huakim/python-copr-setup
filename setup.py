from setuptools import setup
# import os
try:
    import variant
    variant = variant.__dict__
except ImportError:
    variant = {}

value = variant.get('name', 'gui')
urlval = variant.get('urlval', value)
url = variant.get('url', f"https://github.com/huakim/python-copr_{urlval}")
script = variant.get('script', f"copr-{urlval}")

args = {}
if value == "gui":
    args["packages"] = ["copr_gui.__dynamic", "copr_gui.static", "copr_gui"]
    args["install_requires"] = ["copr", "bidict", "json5"]
else:
    pkgname = f"copr_gui.generic.{value}"
    args["packages"] = [pkgname]
    #    args['package_dir'] = {pkgname: f'copr_gui/generic/{value}'}
    args["install_requires"] = ["copr_gui", value]
    args["entry_points"] = {
        "console_scripts": [f"{script}=copr_gui.generic.{value}.launcher:main"]
    }

urlval = value

setup(
    description="Copr package build gui tools",
    summary="Copr package build gui tools",
    version="0.1.6",
    license="GPLv3",
    name=f"copr_{value}",
    python_name=f"python-copr-{value}",
    url=f"https://github.com/huakim/python-copr_{urlval}",
    archive_name=f"copr_{value}",
    **args,
)
