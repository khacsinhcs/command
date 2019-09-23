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
#### Performence
* quote many lenders/time
* Lender has many rates
* Rate can be apply many adj base on user profile
--> easy to hit perf issue
#### Verify
* Hard to proven that quote engine is correct

## Requirement:
* Manage mutipal format
* Handle format change quickly
* Provide the way to define meta data to ratesheet. Easy to share with non-tech people
### 