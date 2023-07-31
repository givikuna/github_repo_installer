# running this is very optional, just run the githubrepoinstaller.py if you just want the repos to be installed, this is just what I'm using

cd ..
touch projects
mv github_repo_installer/githubrepoinstaller.py projects
cd projects
python3 githubrepoinstaller.py
rm githubrepoinstaller.py
cd ..
rm -rf github_repo_installer
