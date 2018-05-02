#creates and moves into directory titled New Git.
mkdir "New Git"
cd New\ Git
#creates and gives permission for new .sh file for automated adding, committing, and pushing of changes. Title is ACH.sh
echo "
git add .
git commit -m "another"
git push
git status" >ACP.sh
chmod +x *.sh
#does most of git repository set up. Echos next steps for copy paste.
echo "# Whatever" >> README.md
git init
git add README.md
git commit -m "first commit"
echo "git remote add origin https:"
echo "git push -u origin master"
