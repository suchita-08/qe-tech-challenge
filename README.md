# qe-tech-challenge

Explanation about the framework structure:
1.	qe-tech-challenge --> main directory
2.	qe-tech-challenge/pagemodules/ -->  page wise modules present here (class and methods)
3.	qe-tech-challenge/comman/ --> commonly used utility and methods present here
4.	qe-tech-challenge/test_data.xlsx --> file is used to store test data
5.	qe-tech-challenge/test_main_file.py -->  script that needs to be executed.

Used Jenkins as CI tool which runs on local machine.

Jenkins Configurations:
1.	Create a new job with Freestyle project.
2.	Configure the job as
    1.	Source Code Management --> select “Git” --> Enter “Repository URL”, “Credential” and “Branches to build”
    2.	Build --> Select “Execute shell” -->  py.test test_main_file.py -v --html="report.html"
    3.	Build --> Select “Execute shell” 
        git add "logfile.log"
        git add "report.html"
        git commit -m "file added"
    4.	Post-build Actions --> Select “Git Publisher” --> “select push option”, Enter “Branches” details
3.	Save

Steps to run:
1.	Go to created job --> Build Now
2.	Once the build completes, logfile “logfile.log” and html report “report.html” are generated and pushed to github repository.

Additinally, To run any specific test --> Add these steps as build step “py.test test_main_file.py::test_3 -v --html="report.html"”

