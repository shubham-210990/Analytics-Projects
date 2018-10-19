#set the directory
setwd('C:\\Users\\Shubham\\Downloads\\Praxis\\ML - GN')

data = read.csv('Attrition.csv')
View(data)

install.packages('rpart')
library(rpart)

tree = rpart(Attrition~BusinessTravel + Department + EducationField
             + EnvironmentSatisfaction + JobInvolvement + Gender
             + MaritalStatus+OverTime + TotalWorkingYears
             + YearsAtCompany,data=data)

plot(tree)
text(tree)

tree


