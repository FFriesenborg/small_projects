#import os  
#os.system("pdflatex Automating-Cover-Letters/main.tex")

from analyse_ATS_CV import read_cv
cv_information=read_cv(r'Automating-Cover-Letters\20250314_CV_Fabian_Fischer_ATS.pdf')