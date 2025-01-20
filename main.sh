dnf install -y python3-build python3-py2pack
python3 -m build -n -s . -o .
py2pack generate --localfile *.tar.gz
rpmbuild "-D_srcrpmdir ${outdir}" "-D_sourcedir ${outdir}" --bs "python-corp_gui.spec"

