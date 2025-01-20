dnf install -y python3-build python3-py2pack
python3 -m build -n -s . -o .
var="$(cat variant.txt)"
py2pack generate --localfile "copr_${var}"*.tar.gz
rpmbuild "-D_srcrpmdir ${outdir}" "-D_sourcedir $PWD" --bs "python-copr_${var}.spec"

