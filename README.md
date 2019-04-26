Abstract

A web application to simplify the calculation of Course Outcomes of Continuous Internal Assessment, AAT , Assignment and Semester End Examinations. The web application when fed with the Continuous Internal Assessment marks of the students, would result in the Course Attainment of the individual Course Outcome of that subject which can be used for Department Metrics purpose. The aim of this application is to automate the whole process and require zero manual calculations or errors. It also provides the related data analytics of the uploaded data in the form of User understandable tables, statistics and charts. The result is printable as a document.


Introduction

Course Outcomes are formed based on the subject knowledge and the Blooms taxonomy. There are six possible Course outcomes. To know the performance of a particular course for that semester, the course attainment must be calculated. This will showcase the performance of the students in that particular subject in that semester. The calculation required to do this is humongous as the data involved here is also huge. Each students’ marks of each question in each CIA (Continuous Internal Assessment) must be considered for the calculation purposes and the course outcome must be derived.

Since this calculation is time consuming, a way to automate this was necessary. Here comes the role of the web application – DSCE Calci – which our Web Application project that makes this complete process automated and simple, where just the upload of the document containing the marks of the students would result in the course attainment of that particular course. 

Once the document has been uploaded, just in a click away, the web application will provide the Course Attainment, the minimum marks scored in that CO, the number of students who scored that marks, the maximum marks scored in that CO, the number of students who scored that marks and the number of other students.

This calculation will be performed on Internals marks, Assignment marks, AAT Marks and External SEE marks. The overall Course Outcome is calculated based on the standards of the department.

All of this information will be provided in tabular format and in terms of Pie Chart graphs for each CO.


Design:
 
The components of the design in this web application includes:
1.	User Interface:  The web user interface provides a clear GUI to the user who can then easily interact with the application. He can navigate between the web pages, provide the input as the document and get the output in the form of statistics and pie charts.
2.	Router: The app router will route the user URLs and requests to the respective assigned pages with the necessary data.
3.	Calculation file: The calculation python file has the computational formulae to calculate the CO attainment, the max, the min and the number of such students respectively. It also generates the pie chart after the calculation of the data.
4.	Jinja Engine: Jinja is the view engine that is used here to render the web pages.





Implementation:
The web application has been implemented using a Python web framework Flask. Flask is a web framework which is used to develop web applications using Python as the backend.
The responsibilities of Flask in this project are:
1.	Routing: 
a.	The flask application takes care of directing the user requests to the respective page with the data. 
b.	It serves to two basic kinds of request.
i.	GET request
ii.	POST request
c.	The GET request is served when the user types a URL and needs a web page to be served.
d.	The POST request is used when form is submitted, in this case when we submit the document from which the calculations have to be done.
2.	Computation Call:
a.	The flask is responsible to call the computational file which is written in Python. This Python file consists of the calculations that needs to be performed.









Testing / Result and Analysis

Testing: 
	Inputs: doc.xls 
		   The file which has all the internal marks, the AAT marks, the Assignment marks, the external SEE marks for all the students of that batch in that subject.
	Output to compare with: Manually calculated Course Outcomes.
	Output: Program calculated course outcomes.

Result:
	The manually calculated course outcomes are the same as the program calculated course outcomes.
Hence the testing is successful and the program works in the requirement specified manner.









Conclusion:
 	This web application can be used to automate the calculation of Course outcomes with just the upload of the excel document. This will considerably increase the accuracy and speed in this domain as the data is multiple in number and huge in terms of size.

Future Enhancements:
	The application can be extended to support other departments of the college.














References:

Documentation:
         [1] Flask Documentation: http://flask.pocoo.org/docs/1.0/
[2] Jinja Documentation: http://jinja.pocoo.org/docs/2.10/
[3] Python Documentation: https://docs.python.org/3/
