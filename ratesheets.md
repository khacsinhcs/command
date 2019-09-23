# Ratesheet parsing

## Challenge

### Parser
#### Format
* Mutipal format (pdf, xml, excel, html)
* Adjustment: table format, list format
#### Change format
* Change frequently
* Handle failure
#### Multi state
Some lender publish rate and adj for each state
#### Heavy Business logic
* lender define diffent program adj. Some special adj apply short spefic case break format of ratesheet file
* many loans type: comfi, jumbo, ...

### Quote engine
### Calculate performence
* quote many lenders/time
* Lender has many rates
* Rate can be apply many adj base on user profile
--> easy to hit perf issue
#### Hard to test
* Hard to proven that quote engine correct

## Requirement:
* Handle format change quickly
* 
### 