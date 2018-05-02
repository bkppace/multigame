cd
cd Desktop

#two dots between numbers indicates range, at least in bash script

if touch file.txt
then echo "The deed is done." > file.txt
else echo "Job failed."
fi

sleep 5; textutil -convert .pdf *.txt
